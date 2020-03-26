run:
	docker-compose up --build
	# install deps
stop:
	docker-compose down
remove:
	# Stop all running project images (make stop)
	# Remove all project images
	# Prompt warning message (y/n)
	docker stop $(docker ps -qa)
	
test:

build:

deps:

install:
	docker exec -t container_name poetry self update

	if [ -z "$(dep)" ]; then \
		docker exec -t container_name poetry install; \
	else \
		docker exec -t container_name poetry add "$(dep)"; \
	fi

shell:

dbshell:
