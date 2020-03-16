setup:
	npm install --prefix=./themes/blind

dev:
	npm --prefix=./themes/blind run watch & hugo server -D --watch

deploy:
	# Install frontend build system and dependancies
	npm install --prefix=./themes/blind
	# Build static css
	npm --prefix=./themes/blind run build
	# Build templates
	hugo
	 # Delete original images (full size)
	rm $$(find content/art_post -type f -wholename "*images*" | sed s,content,./public,g | xargs)
	# Ship http server configuration
	cp Caddyfile public
	 # Send to server
	rsync -vrz ./public/* jotoole@142.93.40.182:~/james-o.tools/
	# Restart the http server
	ssh jotoole@142.93.40.182 'cd james-o.tools; caddy reload'
