# Environment variables in Compose

[中文版](README.md)

* [Youtube Tutorial - Docker Basic Tutorial - Making good use of Environment variables in docker-compose](https://youtu.be/JwbI1aNKbtY)

How to make good use of Environment variables in docker-compose :pencil2:

[Environment variables in Compose](https://docs.docker.com/compose/environment-variables/#substitute-environment-variables-in-compose-files)

Environment variables can be set in many places. If multiple environment variables appear at the same time, the priority is as follows:

1. Compose file
2. Shell environment variables
3. Environment file
4. Dockerfile
5. Variable is not defined

First, let's look at `Shell environment variables`

```cmd
export ODOO_TAG=12.0
export POSTGRES_TAG=10.9
```



Additional note: if you want to remove the settings, you can execute

```cmd
unset ODOO_TAG
unset POSTGRES_TAG
```

To check if the settings are successful, you can use the following command

```cmd
echo $ODOO_TAG
echo $POSTGRES_TAG
```

View all environment variables

```cmd
export -p
```

Then execute the following command to check if the settings are correct

```cmd
docker-compose config
```



Notice the ODOO_TAG and POSTGRES_TAG? :smile:

The values here are exactly the same as what we just set.

Now let's look at [docker-compose.yml](https://github.com/twtrubiks/docker-tutorial/blob/master/docker-env-tutorial/docker-compose.yml)

```yml
......
services:
  web:
    image: odoo:${ODOO_TAG:-13:0}
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./config:/etc/odoo
      - ./addons:/mnt/extra-addons
  db:
    image: postgres:${POSTGRES_TAG:-10.9}
......
```

`${ODOO_TAG:-13:0}`: means if ODOO_TAG is not filled or ODOO_TAG is empty, the default value is 13:0

`${POSTGRES_TAG:-10.9}`: means if POSTGRES_TAG is not filled or POSTGRES_TAG is empty, the default value is 10.9

For more information, see [variable-substitution](https://docs.docker.com/compose/compose-file/#variable-substitution#variable-substitution).

There is also the `Environment file` method.

This mainly involves creating a `.env` file and storing the information in it, but be careful here :exclamation:

`Shell environment variables` > `Environment file`

So if you want to use `.env`, remember to unset :exclamation:

[.env](https://github.com/twtrubiks/docker-tutorial/blob/master/docker-env-tutorial/.env)



Then use `docker-compose config`



The information from `.env` has been successfully set.
