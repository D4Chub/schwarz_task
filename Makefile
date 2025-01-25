run:
	docker compose up -d --build

load_data:
	docker compose exec web python manage.py loaddata test_data.json

test:
	docker compose exec web python manage.py test
