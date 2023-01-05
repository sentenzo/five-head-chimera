lint:
	poetry run isort backend dbwriter
	poetry run black backend dbwriter
	poetry run pylint backend dbwriter

export_requirements:
	poetry export --only backend --without-hashes -f requirements.txt --output backend/requirements.txt
	poetry export --only dbwriter --without-hashes -f requirements.txt --output dbwriter/requirements.txt

up: export_requirements
	docker-compose up --build -d

down:
	docker-compose down

local_backend:
	poetry run python ./backend/service/app.py --logging=info

prune:
	docker image prune