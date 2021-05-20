migrate:
	python manage.py migrate

serve:
	python manage.py runserver

migrations:
	python manage.py makemigrations ${app}
	
admin:
	python manage.py createsuperuser

shell:
	python manage.py shell