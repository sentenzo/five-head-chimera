lint:
	poetry run isort backend frontend
	poetry run black backend frontend
	poetry run pylint backend frontend

export_requirements:
	poetry export --only backend --without-hashes -f requirements.txt --output backend/requirements.txt

up: export_requirements
	docker-compose up --build -d

down:
	docker-compose down

