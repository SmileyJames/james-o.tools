setup:
	npm install --prefix=./themes/blind

dev:
	npm --prefix=./themes/blind run watch & hugo server -D --watch
