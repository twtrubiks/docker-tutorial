# Introduction to docker-compose-profiles

[中文版](README.md)

You can refer to the official documentation [Using profiles with Compose](https://docs.docker.com/compose/profiles/)

Simply put, you can use it to manage your compose.

Let's look at an example directly [docker-compose.yml](docker-compose.yml)

```yml
services:

    nginx:
        container_name: nginx
        image: nginx:1.24.0
        restart: always
        ports:
          - "83:80"

    pgadmin4:
        ......
        profiles:
          - debug

    redis:
      ......
      profiles:
        - dev
```

If you execute `docker compose up`, by default only nginx will be started.

If you want to start pgadmin4 as well, you can use `docker compose up pgadmin4`.

If you want to start the debug profile from the beginning, you can use `docker compose --profile debug up`.

You can define multiple profiles and enable multiple profiles at once.

For example, `docker compose --profile dev --profile debug up`.

When shutting down the containers, executing `docker compose down` will only shut down the default ones.

You must execute `docker compose --profile dev --profile debug down` to shut down all containers.
