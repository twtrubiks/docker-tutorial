# 介紹 docker-compose-profiles

可參考官方文檔 [Using profiles with Compose](https://docs.docker.com/compose/profiles/)

簡單說, 可以透過它去管理你的 compose,

直接看例子 [docker-compose.yml](docker-compose.yml)

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

如果你執行 `docker compose up` 預設就只會啟動 nginx,

如果你想再啟動 pgadmin4, 可以使用 `docker compose up pgadmin4`.

如果想一開始就把 debug 的也啟動, 可以使用 `docker compose --profile debug up`

profile 可以定義很多個, 也可以一次啟用很多次,

例如 `docker compose --profile dev --profile debug up`

關閉容器的時候, 只執行 `docker compose down` 只會關掉預設的,

必須執行 `docker compose --profile dev --profile debug down` 才會關閉全部容器.