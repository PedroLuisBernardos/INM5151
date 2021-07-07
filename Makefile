all: migrate run

install:
	pip install -r requirements.txt --user

run: install
	flask run

traduct:
	flask translate --help

migrate:
	flask db migrate -m "update"
	flask db upgrade