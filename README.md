# HOTBOX

Welcome to the hotbox project!

## Installation:

Clone the repository

create a `.env` file that looks like this:
```
PYTHONPATH=/app
PYTHONUNBUFFERED=1

FLASK_APP=start.py
FLASK_ENV=development
FLASK_DEBUG=1

POSTGRES_DB=hotbox-db
POSTGRES_USER=hotbox-user
POSTGRES_PASSWORD=hotbox-password
```

Install Docker
```
apt install docker.io
systemctl start docker
systemctl enable docker
```
Install docker-compose (https://docs.docker.com/compose/install/)

Start the server
`make run`

Check the server is running propperly:
```
$ curl localhost:5000/health
$ {'status': 'Running'}
```


##  Managing ependencies:

### Upgrading dependencies:
Open a shell for the project's container:
`make shell`
Upgrade a single package:
`poetry update <package_name>`

Upgrade all project dependencies (risky):
`poetry update`

### Installing new dependencies: 
`make install dep=<package_name>`

## Troubleshooting:

run `docker stop $(docker ps -qa)` to stop ALL running docker containers
Remove all Docker images:
`docker system prune`
Run the prject again:
`make run`

## Deployment
# Deploying app to Heroku
Push changes to container registry:
`heroku container:push web`
Release those changes:
 `heroku container:release web`
 Open the app in the browser:
`heroku open`
View logs:
 `heroku logs --tail`
