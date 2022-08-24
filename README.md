# HOTBOX

Welcome to the hotbox project!

This is a web application that allows the user to add songs to a playing queue in real time. 
All users can query the platform to add new songs, and the songs will be added to the queue in real time.
This is a pet project that I created to develop my skills with python/flask/socketio/VUEjs.
The app is currently not deployed on a server due to maintenance costs. 

## Installation:

Clone the repository

create a `.env` file that looks like this:
```
PYTHONPATH=/app
PYTHONUNBUFFERED=1

FLASK_APP=start.py
FLASK_DEBUG=1
HOST=0.0.0.0
PORT=5000
SECRET_KEY=replaceme # To encrypt socketio messages


# Postgres:
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


##  Managing dependencies:

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

# Add new songs:
Get tracks from playlist in json forat:
https://developer.spotify.com/console/get-playlist-tracks/
Copy json file to container:
`docker cp <file> <container-name>:/app/<file>`
Run the followin command:
`flask com add_songs <file>`
