# 介紹 docker-compose-override

[English Version](README_en.md)

* [Youtube Tutorial - Odoo + Docker 進階技巧：善用 override.yml 批次更新多個 DB](https://youtu.be/oR_wM8rQKYI)

## 說明

官方文檔可參考 [Merge Compose files](https://docs.docker.com/compose/multiple-compose-files/merge/)

通常一般我們使用都只會用 [docker-compose.yml](docker-compose.yml)

但其實 docker 會去該路徑底下找是否有 [docker-compose.override.yml](docker-compose.override.yml),

來看一個例子,

當你執行 `docker compose up -d` 時,

docker 會去自動去找對應的 `docker-compose.override.yml`,

不相同的部份, 結果是兩個的相加, 以這個例子來說, 你會發現 nginx 容器內的

80 port (`docker-compose.yml`定義) 和 81 port (`docker-compose.override.yml`) 都被打開了,

如果是相同的部份, 是覆蓋, 看誰後面執行, 像是這個範例中, $TEST 會輸出 "world"

```cmd
❯ docker exec -it nginx bash
root@73377e053ab4:/# echo $TEST
"world"
```

上面說的看誰後面執行的意思是, 本質上, 如果你沒有特別設定,

執行

```cmd
docker compose up -d
```

等同下面的

```cmd
docker compose -f docker-compose.yml -f docker-compose.override.yml up -d
```

然後如果你把他顛倒過來, 環境變數的輸出就會不一樣了.

## 實戰

這邊使用 odoo 搭配 docker 來實戰一下這個例子 [odoo18_example_docker_override](odoo18_example_docker_override/)

今天有一個需求, 我想要在 odoo 底下的每個 db, 都安裝 mail 這個 addons,

也就是以下指令的概念 (但實際上 odoo 一次只能更新一個 db)

```python
python3 odoo-bin -i mail -d odoo1,odoo2 -c odoo.conf
```

所以, 為了完成這個需求, 必須搭配 override 的概念,

因為我原本的 docker-compose.yml 我不希望改動.

[docker-compose.override.yml](odoo18_example_docker_override/docker-compose.override.yml) 為

```yml
services:
  web:
    # command: odoo -u mail -d ${DB_NAME}
    command: odoo -i mail -d ${DB_NAME}
```

然後透過一個 bash 檔案

```bash
#!/bin/bash

# 要更新的 db
DATABASES=("odoo1" "odoo2" "odoo3")

for DB in "${DATABASES[@]}"
do
    echo "Updating addons for database: $DB"

    # 設定環境變數 DB_NAME 並執行 docker compose
    DB_NAME=$DB docker compose up -d

    # 等待 Odoo 完成資料庫更新
    sleep 5  # 視需求調整等待時間
done

echo "All databases have been updated."
```

這個 bash 檔案名稱, 每次會設定環境變數 DB_NAME, 並且執行 docker compose 去完成安裝更新.

也就是去呼叫 `docker-compose.override.yml`,

執行指令

```cmd
chmod +x auto.sh
./auto.sh
```

再重新啟動一次 (因為要還原 odoo command 的指令),

可以修改檔案 `docker-compose.override.yml` (因為不要再讓 docker 執行到它),

或是使用 `docker compose -f docker-compose.yml up`.
