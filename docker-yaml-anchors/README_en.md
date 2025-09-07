# Introduction to YAML Anchors

[中文版](README.md)

* [Youtube Tutorial - YAML Anchors (& * <<) and Docker Compose Hands-on Tutorial: Say Goodbye to Repetitive Configurations!](https://youtu.be/6QSfqTymeXc)

This feature is not from Docker, but a feature of YAML called YAML Anchors.

In short, through YAML Anchors, you can group repetitive parts together, so you don't have to write them many times.

Let's look at the definitions:

YAML Anchors (&)

Aliases (*)

Merge Key (<<)

Here is an example of how to use it [docker-compose.yml](docker-compose.yml)

First, let me explain why we always use the `x-` prefix.

The `x-` prefix is a convention, and Docker Compose will ignore top-level keys with the `x-` prefix.

It will not treat them as things like services, volumes, or networks.

Simply put, using it this way will not affect the normal parsing of Docker Compose.

```yml
# &x-config defines an anchor

# This is just to show that the top-level key can be defined arbitrarily, it doesn't need to have the same name as your anchor
# x-config: &x-config
# or
x-config-key: &x-config
  # key: value
  image: nginx
  restart: always
  logging:
    driver: "json-file"
    options:
      max-file: "1"
      max-size: "50m"
  # key: sequence or array
  volumes:
      - static:/my_tmp
      - ./local_static:/local_static

services:

  nginx1:
    # *x-config creates an alias to the content of that anchor
    # << merges mappings (i.e., key-value pairs), but if the same key is encountered during the merge process, the default behavior is to "overwrite"
    <<: *x-config
    container_name: nginx1
    ports:
      - "81:80"

  nginx2:
    <<: *x-config
    container_name: nginx2
    # Because the value of volumes is a sequence or array
    # and the default behavior is to "overwrite", the same key (volumes) in x-config will be completely overwritten
    volumes:
      - static_nginx_2:/tmp2
    ports:
      - "82:80"

  nginx3:
    <<: *x-config
    container_name: nginx3
    volumes:
      - static_nginx_3:/tmp3
      - static:/my_tmp  # Need to add this manually
      - ./local_static:/local_static # Need to add this manually
    ports:
      - "83:80"


volumes:
  static:
  static_nginx_2:
  static_nginx_3:
```

nginx1, nginx2, and nginx3 share `image`, `restart`, `logging`, and `volumes`.

This way, you don't have to write them repeatedly.

However, you need to be careful with `volumes`. As soon as you define a key in your local service that is the same as in the anchor (e.g., the `volumes` key),

like the `volumes` under nginx2, the shared part in `x-config` will **not take effect** in this container, because the entire `volumes` list is overwritten by the local definition.

That is, only `- static_nginx_2:/tmp2` will take effect.

So, as long as you have the same key (like `volumes` in this scenario), please rewrite it like nginx3, and manually add the shared parts back.
