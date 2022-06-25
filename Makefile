install:
	poetry install

lint:
	poetry run flake8 task_manager

test:
	poetry run coverage run --source='.' manage.py test task_manager

runserver:
	poetry run python manage.py runserver

messages:
	poetry run django-admin makemessages -l ru

compile:
	poetry run django-admin compilemessages

migrations:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

coverage:
	poetry run coverage xml
