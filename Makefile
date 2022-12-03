build:
	@echo "--> Building my_library containers..."
	DOCKER_BUILDKIT=1; docker-compose build

build-no-cache:
	@echo "--> Building my_library containers..."
	DOCKER_BUILDKIT=1; docker-compose build --no-cache

down:
	@echo "--> Come Down my_library containers..."
	docker-compose down

install-requirements:
	@echo "--> Installing requirements..."
	pip install -r requirements/base.in
	pip install -r requirements/dev.in
	pip install -r requirements/test.in

compile:
	@echo "--> Removing .txt files..."
	rm -r requirements/base.txt
	rm -r requirements/dev.txt
	rm -r requirements/test.txt

	@echo "--> Running pip-compile..."
	pip-compile requirements/base.in
	pip-compile requirements/dev.in
	pip-compile requirements/test.in

migrations:
	@echo "--> Make Migrations..."
	docker-compose run app python manage.py makemigrations

migrate:
	@echo "--> Make Migrations..."
	docker-compose run app python manage.py migrate

superuser:
	@echo "--> Make Super User..."
	docker-compose run app python manage.py createsuperuser

run:
	@echo "--> Starting server in port 8000..."
	docker-compose up

shell:
	@echo "--> Staring shell..."
	docker-compose run app python manage.py shell

test:
	@echo "--> Running tests..."
	docker-compose run app $(path) pytest -s -v --disable-warnings
	docker-compose down

test-no-cache:
	docker-compose run app bash -c "rm -rf .pytest_cache"
	@echo "--> Running tests..."
	docker-compose run app $(path) pytest -s -v --disable-warnings
	docker-compose down
