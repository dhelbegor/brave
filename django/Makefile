ARGS = $(filter-out $@,$(MAKECMDGOALS))
MAKEFLAGS += --silent
.DEFAULT_GOAL := help

PROJECTNAME = web

DOCKER_EXEC = docker exec -it
DOCKER_IEXEC = docker exec -i $(PROJECTNAME)
MANAGE = $(DOCKER_EXEC)web ./manage.py

init:
	docker-compose up -d --remove-orphans --build

logs:
	docker-compose logs -f "${ARGS}"

install:
	docker-compose exec web pipenv install "${ARGS}"

cmd:
	$(DOCKER_EXEC) web $(ARGS)
