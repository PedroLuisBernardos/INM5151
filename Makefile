all: run

install:
	pip install -r requirements.txt --user

run: compile install
	flask run

compile:
	flask translate compile

traduct:
	flask translate --help

migrate:
	flask db migrate -m "update"
	flask db upgrade

init-db:
	rm -rf migrations/
	rm app.db
	flask db init
	flask db migrate -m "Initialisation de la bd"
	flask db upgrade