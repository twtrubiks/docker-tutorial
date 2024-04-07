# 介紹 docker-compose-override

官方文檔可參考 [Merge Compose files](https://docs.docker.com/compose/multiple-compose-files/merge/)

通常一般我們使用都只會用 [docker-compose.yml](docker-compose.yml),

但其實 docker 會再去該路徑底下找是否有 [docker-compose.override.yml](docker-compose.override.yml),

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