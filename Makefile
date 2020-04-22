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
	docker stop $(docker ps -qa)
	docker system prune
	# remove images
	
test:

build:
	docker-compose up --build

deps:
	docker exec -t hotbox-app poetry show

com:
	if [ -z "$(com)" ]; then \
		docker exec -t hotbox-app flask com; \
	else \
		docker exec -t hotbox-app flask com "$(com); \
	fi

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
	#docker exec -it hotbox-db psql -U 
	docker-compose run db psql --host=db --username=hotbox-user --dbname=hotbox-db

health:
	curl http://localhost:5000/health

flask_shell:
	docker exec -it hotbox-app flask shell
