DOCKER_COMPOSE := docker-compose
DOCKER := docker
TAG := fastapi_image

.PHONY: build
build:
	$(DOCKER) build -t $(TAG) .

.PHONY: db_run
db_run:
	$(DOCKER_COMPOSE) up postgresql_db -d
	$(DOCKER_COMPOSE) up pgadmin -d

.PHONY: fastapi_run
fastapi_run: build
	$(DOCKER_COMPOSE) run app_fastapi
