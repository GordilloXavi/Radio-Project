run:
	docker-compose up --build
	# install deps
stop:
	docker-compose down
remove:
	# Stop all running project images (make stop)
	# Remove all project images
	# Prompt warning message (y/n)
	docker-compose down
	# remove images
	
test:

build:

deps:

install:
	#docker exec -t hotbox-app poetry self update

	if [ -z "$(dep)" ]; then \
		docker exec -t hotbox-app poetry install; \
	else \
		docker exec -t hotbox-app poetry add "$(dep)"; \
	fi

shell:
	docker exec -it hotbox-app  bash

dbshell:
	docker exec -it hotbox-db psql -U hotbox 

health:
	curl localhost:5000/health