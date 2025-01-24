run:
	docker compose up -d --build

test:
	docker compose exec web python manage.py test
