## Environment variables in Compose

* [Youtube Tutorial - Docker 基本教學 - 在 docker compose 中善用 Environment variables](https://youtu.be/JwbI1aNKbtY)

在 docker compose 中如何善用 Environment variables:pencil2:

[Environment variables in Compose](https://docs.docker.com/compose/environment-variables/#substitute-environment-variables-in-compose-files)

Environment variables 可以設定在很多地方, 假如同時出現多個環境變數, 優先順序如下,

1. Compose file
2. Shell environment variables
3. Environment file
4. Dockerfile
5. Variable is not defined

先來看 `Shell environment variables`

```cmd
export ODOO_TAG=12.0
export POSTGRES_TAG=10.9
```

![alt tag](https://i.imgur.com/5tBbt2c.png)

額外補充, 如果想要移除設定, 可執行

```cmd
unset ODOO_TAG
unset POSTGRES_TAG
```

如果要查看是否有設定成功, 可使用以下指令

```cmd
echo $ODOO_TAG
echo $POSTGRES_TAG
```

查看全部的 environment variables

```cmd
export -p
```

然後執行以下指令檢查是否設定正確

```cmd
docker-compose config
```

![alt tag](https://i.imgur.com/cTc0KtV.png)

注意到 ODOO_TAG 和 POSTGRES_TAG 了嗎:smile:

這邊的值和剛剛設定的一模一樣。

然後來看一下 [docker-compose.yml](https://github.com/twtrubiks/docker-tutorial/blob/master/docker-env-tutorial/docker-compose.yml)

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

`${ODOO_TAG:-13:0}`: 代表如果沒有填 ODOO_TAG 或是 ODOO_TAG 值為空, 預設帶入 13:0

`${POSTGRES_TAG:-10.9}` : 代表如果沒有填 POSTGRES_TAG 或是 POSTGRES_TAG 值為空, 預設帶入 10.9

更多資訊可參考 [variable-substitution](https://docs.docker.com/compose/compose-file/#variable-substitution#variable-substitution)。

還有一種是 `Environment file`,

主要是建立一個 `.env` 檔案, 將資訊存在裡面, 但這邊要注意:exclamation:

`Shell environment variables` > `Environment file`

所以如果要使用 `.env`, 記得要 unset:exclamation:

[.env](https://github.com/twtrubiks/docker-tutorial/blob/master/docker-env-tutorial/.env)

![alt tag](https://i.imgur.com/J0jRsld.png)

然後使用 `docker-compose config`

![alt tag](https://i.imgur.com/S0kWOsn.png)

成功設定成 `.env` 的資訊了。
