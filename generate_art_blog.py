import os
import csv
from collections import namedtuple
from shutil import copyfile


def slugify(s):
    return '_'.join(s.replace("'", '').lower().split(' '))


def template(o, slug):
    return (
            '\n'
            '---\n'
            f'title: {o.title}\n'
            f'date: {o.datetime}\n'
            f"author: James O'Toole\n"
            f'medium: {o.medium}\n'
            f'size: {o.width}mm x {o.height}mm\n'
            f'image: images/{o.image}\n'
            f'draft: false\n'
            '---\n'
            '\n'
            f'{o.description}\n')


def get_path(slug):
    return os.path.join('content/art_post', slug)


def mkdir(art, slug):
    path = get_path(slug)
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    try:
        os.mkdir(os.path.join(path, 'images'))
    except FileExistsError:
        pass


def write_markdown(art, slug):
    with open(os.path.join(get_path(slug), 'index.md'), 'w') as f:
        f.write(template(art, slug))


def copy_image(art, slug):
    path = get_path(slug)
    copyfile(
            os.path.join('image_dump', art.image),
            os.path.join(
                path, 'images',
                '.'.join([slug, art.image.split('.')[1]])))


def main():
    with open('art_images.csv') as art_file:
        art_images = csv.reader(art_file, delimiter=';')
        art_image_header = next(art_images)

        ArtImage = namedtuple('ArtImage', art_image_header)

        for _art in art_images:
            art = ArtImage(*_art)
            slug = slugify(art.title)
            print(slug, '...')
            mkdir(art, slug)
            write_markdown(art, slug)
            copy_image(art, slug)


if __name__ == '__main__':
    main()
