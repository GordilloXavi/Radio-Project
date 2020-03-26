# HOTBOX

Welcome to the hotbox project!

## Installation:

Clone the repository

Install Docker and docker-compose

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
