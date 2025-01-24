run:
	docker compose up --build

test:
	docker compose exec web python manage.py test
