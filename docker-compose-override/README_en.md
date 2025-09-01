# Introduction to docker-compose-override

[中文版](README.md)

* [Youtube Tutorial - Odoo + Docker Advanced Techniques: Using override.yml to Batch Update Multiple DBs](https://youtu.be/oR_wM8rQKYI)

## Description

You can refer to the official documentation at [Merge Compose files](https://docs.docker.com/compose/multiple-compose-files/merge/)

Usually, we only use [docker-compose.yml](docker-compose.yml).

But actually, docker will look for [docker-compose.override.yml](docker-compose.override.yml) in the same directory.

Let's look at an example.

When you execute `docker compose up -d`,

docker will automatically look for the corresponding `docker-compose.override.yml`.

For the different parts, the result is the sum of the two. In this example, you will find that inside the nginx container,

port 80 (defined in `docker-compose.yml`) and port 81 (defined in `docker-compose.override.yml`) are both opened.

For the same parts, it's an override, depending on which one is executed later. For example, in this sample, $TEST will output "world".

```cmd
❯ docker exec -it nginx bash
root@73377e053ab4:/# echo $TEST
"world"
```

What I mean by "depending on which one is executed later" is that, essentially, if you don't set it specifically,

executing

```cmd
docker compose up -d
```

is equivalent to the following

```cmd
docker compose -f docker-compose.yml -f docker-compose.override.yml up -d
```

And if you reverse the order, the output of the environment variable will be different.

## Hands-on

Here we use odoo with docker to practice this example [odoo18_example_docker_override](odoo18_example_docker_override/)

Today I have a requirement, I want to install the `mail` addon for every db under odoo.

This is the concept of the following command (but in reality, odoo can only update one db at a time)

```python
python3 odoo-bin -i mail -d odoo1,odoo2 -c odoo.conf
```

So, to accomplish this requirement, I must use the concept of override,

because I don't want to change my original `docker-compose.yml`.

[docker-compose.override.yml](odoo18_example_docker_override/docker-compose.override.yml) is

```yml
services:
  web:
    # command: odoo -u mail -d ${DB_NAME}
    command: odoo -i mail -d ${DB_NAME}
```

Then through a bash file

```bash
#!/bin/bash

# Databases to be updated
DATABASES=("odoo1" "odoo2" "odoo3")

for DB in "${DATABASES[@]}"
do
    echo "Updating addons for database: $DB"

    # Set the environment variable DB_NAME and execute docker compose
    DB_NAME=$DB docker compose up -d

    # Wait for Odoo to finish updating the database
    sleep 5  # Adjust the waiting time as needed
done

echo "All databases have been updated."
```

This bash file name will set the environment variable `DB_NAME` each time and execute `docker compose` to complete the installation and update.

That is, to call `docker-compose.override.yml`.

Execute the command

```cmd
chmod +x auto.sh
./auto.sh
```

Then restart again (because you need to restore the odoo command).

You can modify the file `docker-compose.override.yml` (so that docker will not execute it again),

or use `docker compose -f docker-compose.yml up`.
