runserver:
	poetry run python manage.py runserver

translate:
	poetry run django-admin compilemessages

makemigrations:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

makemigrations_statuses:
	poetry run python3 manage.py makemigrations statuses
	poetry run python3 manage.py migrate