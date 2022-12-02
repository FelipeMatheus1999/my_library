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

run:
	@echo "--> Starting server. in port 8000..."
	docker-compose up
