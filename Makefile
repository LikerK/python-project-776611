install:
	poetry install

lint:
	poetry run flake8 task_manager

runserver:
	poetry run python manage.py runserver

translate:
	poetry run django-admin compilemessages

makemigrations:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate
