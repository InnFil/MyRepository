install:
	pip3 install flake8
	pip3 install black
	pip3 install isort

format:
	black app
	isort

lint:
	flake8

docker-compose:
	docker-compose build
	docker-compose up
