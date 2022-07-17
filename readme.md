# Mobo Suggest

##  Installation
First **clone** or **download** this project.
```sh
$ git clone git@github.com:mohammadsaleh81/mobo_suggest.git
```
Then create **docker network** and **volumes** as below.

```sh
$ docker volume create mobo_postgresql
$ docker volume create mobo_static_volume
$ docker volume create mobo_media_volume
```
```sh
$ docker network create nginx_network
$ docker network create mobo_network
```
You need to create .env file in the project root file with default values.
```sh
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```
Now run django and postgresql with **docker-compose**.
```sh
$ docker-compose up --build
```
Then run nginx container with **docker-compose**.
```sh
$ cd config/nginx/
$ docker-compose up --build
```
You can see mobo_suggest web page on http://localhost, Template and API's are accessable by  docker containers which you can see with below command.
```sh
$ docker ps -a
```
**Output** should be like this.
```sh
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
fc6cc9d6d3d7        nginx_nginx         "nginx -g 'daemon of…"   2 hours ago         Up 2 hours          0.0.0.0:80->80/tcp       nginx
05103904dcb8        ae80efb17475        "gunicorn --chdir bl…"   2 hours ago         Up 2 hours          0.0.0.0:8000->8000/tcp   mobo
4a183e90a9eb        postgres:10         "docker-entrypoint.s…"   2 hours ago         Up 2 hours          0.0.0.0:5432->5432/tcp   mobo_postgresql
```
**nginx** container as common web server, **mobo** container as django application and **mobo_postgresql** as postgreSQL database container.

## Contributing
Contributions are  **welcome**  and will be fully  **credited**. I'd be happy to accept PRs for template extending.
