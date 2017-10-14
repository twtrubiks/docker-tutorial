# docker-tutorial

 Docker 基本教學 - 從無到有 Docker-Beginners-Guide

 教你用 [Docker](https://www.docker.com/) 建立 [Django](https://github.com/django/django) + [PostgreSQL](https://www.postgresql.org/) 📝

* [Youtube Tutorial PART 1](xxxx)
* [Youtube Tutorial PART 2 - 用 Docker 實戰 Django 以及 Postgre](xxx)

## 簡介

[Docker](https://www.docker.com/)

![](https://i.imgur.com/gDcSwcs.png)

算是近幾年才開始紅的技術，蠻多公司都有使用 Docker，而且真的很方便，值得大家去了解一下 :smile:

### 什麼是 Docker

技術原理我們這邊就不提了，簡單提一下他的好處。

我們先來看看官網的說明

Comparing Containers and Virtual Machines

![](https://i.imgur.com/IqiGyoJ.png)

從這張圖可以看出 Containers 並沒有 OS ，容量自然就小，而且啟動速度神快

詳細可參考 [https://www.docker.com/what-container](https://www.docker.com/what-container)

Virtual Machines 是什麼？

類似 [https://www.virtualbox.org/](https://www.virtualbox.org/)，我們可能用它裝裝看其他作業系統，例如說

我是 MAC，但我想玩 Windows，我就會在 MAC 中裝 VM 並且灌 Windows 系統。

### 為什麼要使用 Docker

潮～ 不解釋 :satisfied:

#### 更有效率的利用資源

比起像是 [https://www.virtualbox.org/](https://www.virtualbox.org/)，Docker 的利用率更高，我們可以設定更多

的 Containers ，而且啟動速度飛快！！:flushed:

#### 統一環境

相信大家都有每次搞電腦的環境都搞的很煩的經驗 :angry:

假設今天公司來了個新同事，就又要幫他建立一次環境 :expressionless:

不然就是，我的電腦 run 起來正常阿～ 你的怎麼不行，是不是 xxx 版本的關係阿 :joy:

相信大家多多少少都遇過上面這些事情，我們可以透過 Docker 來解決這些問題，

保持大家環境一致，而且要建立的時候也很快 :smile:。

#### 對於 DevOps 的好處

對於 [DevOps](https://zh.wikipedia.org/wiki/DevOps) 來說，最希望的就是可以設定一次，將來在其他地方都可以快速建立環境且正常執行。

### Docker 概念

我建議大家去了解一下 Docker 中的幾個名詞，分別為 Image，Container，Registry

這邊我就不再解釋惹，留給大家做作功課:stuck_out_tongue:

## 安裝

Windows

請先到 Docker 官網

[https://www.docker.com/docker-windows](https://www.docker.com/docker-windows)

下載 stable 版本

![](https://i.imgur.com/ecAxMNX.png)

接下來就是無腦安裝，安裝完後他會叫你登出電腦，點下去後就會幫你登出電腦

![](https://i.imgur.com/3eeEptv.png)

接著如果你的電腦沒有啟用 [Hyper-V](https://msdn.microsoft.com/zh-tw/library/hh831531(v=ws.11).aspx) ，他會叫你重啟電腦
(一樣，點下去就對惹)

![](https://i.imgur.com/xCbQI1k.png)

重新開機後，你就會發現可愛的 Docker 在右下角蹦出來惹

![](https://i.imgur.com/zMgf36E.png)

我們可以再用 cmd 確認一下是否有成功安裝

```cmd
docker --version
docker-compose --version
```

![](https://i.imgur.com/k1o3GIz.png)

裝完了之後，建議大家再多裝一個 [Kitematic](https://kitematic.com/)，他是 GUI 介面的，方便你使用 Docker，

我知道打指令我知道打指令很潮，但還是建議裝一下。

直接對著你的 Docker 圖示右鍵，就可以看到 [Kitematic](https://kitematic.com/)

![](https://i.imgur.com/gdVFFMT.png)

![](https://i.imgur.com/sQRU8RC.png)

下載回來直接解壓縮雙點擊即可使用

![](https://i.imgur.com/9zsU23B.png)

記得再設定一個東西 Shared Drives

![](https://i.imgur.com/70OjgXN.png)

MAC

MAC 我本身也有，但因為更早之前就裝了，步驟就沒記錄了，基本上大同小異

[https://www.docker.com/docker-mac](https://www.docker.com/docker-mac)

## 指令介紹

接著介紹一些 Docker 的指令，

Docker 的指令真的很多，這裡就介紹我比較常用的或是實用的指令

查看目前 images

```cmd
docker images
```

刪除 Image

```cmd
docker rmi [OPTIONS] IMAGE [IMAGE...]
```

查看目前運行的 container

```cmd
docker ps
```

查看目前全部的 container（ 包含停止狀態的 container ）

```cmd
docker ps -a
```

停止運行中的 container
（ container ID 寫幾個就可以了，和 Git 的概念是一樣的 ，

不了解 Git 可以參考 [Git-Tutorials GIT基本使用教學](https://github.com/twtrubiks/Git-Tutorials)）

```cmd
docker stop [OPTIONS] CONTAINER [CONTAINER...]
```

重新啟動 Container

```cmd
docker restart [OPTIONS] CONTAINER [CONTAINER...]
```

删除 Container

```cmd
docker rm [OPTIONS] CONTAINER [CONTAINER...]
```

進入 Container

```cmd
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
docker exec -it <Container ID> bash
```

打指令比較潮，或是說你也可以透過 [Kitematic](https://kitematic.com/) 進入

[](https://i.imgur.com/Yui1UZb.png)

當我們進入了 Container 之後，有時候想看一下裡面 Linux 的版本，

這時候可以使用以下指令查看

```cmd
cat /etc/os-release
```

查看 Container 詳細資料

```cmd
docker inspect [OPTIONS] NAME|ID [NAME|ID...]
```

再來要介紹 docker-compose，可參考官網 [https://docs.docker.com/compose/](https://docs.docker.com/compose/)

![](https://i.imgur.com/Aq13Bk0.png)

Compose 是定義和執行多 Container 管理的工具，不懂我在說什麼:question::question::question:

試著想想看，通常一個 Web 都還會有 DB，甚至可能還有 [Redis](https://redis.io/) 或 [Celery](http://www.celeryproject.org/)，

所以說我們需要有 Compose 來管理這些，透過 `docker-compose.yml` ( YML 格式 ) 文件。

`docker-compose.yml` ( YML 格式 ) 文件 的寫法可參考 [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)

Compose 的 Command-line 很多和 Docker 都是類似的

可參考 [https://docs.docker.com/glossary/?term=compose](https://docs.docker.com/glossary/?term=compose)

查看目前 Container

```cmd
docker-compose ps
```

加上 `-q` 的話，只顯示 id

```cmd
docker-compose ps -q
```

啟動 Service 的 Container

```cmd
docker-compose start  [SERVICE...]
```

停止 Service 的 Container ( 不會刪除 Container )

```cmd
docker-compose stop [options] [SERVICE...]
```

重啟 Service 的 Container

```cmd
docker-compose restart [options] [SERVICE...]
```

Builds, (re)creates, starts, and attaches to containers for a service

```cmd
docker-compose up [options] [--scale SERVICE=NUM...] [SERVICE...]
```

加個 `-d`，會在背景啟動，一般建議正式環境下使用。

```cmd
docker-compose up -d
```

`up` 這個功能很強大，建議可以參考 [https://docs.docker.com/compose/reference/up/](https://docs.docker.com/compose/reference/up/)

docker-compose down

```cmd
docker-compose down [options]
```

`down` 這個功能也建議可以參考 [https://docs.docker.com/compose/reference/down/](https://docs.docker.com/compose/reference/down/)

在指定的 Service 中執行一個指令

```cmd
docker-compose run [options] [-v VOLUME...] [-p PORT...] [-e KEY=VAL...] SERVICE [COMMAND] [ARGS...]
[ARGS...]
```

舉個例子

```cmd
docker-compose run web bash
```

在 web Service 中執行 `bash` 指令

可參考 [https://docs.docker.com/compose/reference/run/](https://docs.docker.com/compose/reference/run/)

 觀看 Service logs

```cmd
docker-compose logs [options] [SERVICE...]
```

其他指令

刪除所有 dangling images

```cmd
docker rmi $(docker images -q -f dangling=true)
docker rmi $(docker images  --quiet --filter dangling=true)
```

停止所有正在運行的 Container

```cmd
docker stop $(docker ps -q)
```

## 用 Docker 實戰 Django 以及 Postgre

* [Youtube Tutorial PART 2 - 用 Docker 實戰 Django 以及 Postgre](xxx)

上面介紹了那麼多，來實戰一下是必須的 :satisfied:

我們使用 [Django-REST-framework 基本教學 - 從無到有 DRF-Beginners-Guide](https://github.com/twtrubiks/django-rest-framework-tutorial) 來當範例

只有幾個地方必須修改一下，

將 `settings.py`  裡面的 db 連線改成 [PostgreSQL](https://www.postgresql.org/)

```pyhon
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password123',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

建議也將 `ALLOWED_HOSTS = []` 改為 `ALLOWED_HOSTS = ['*']`

補充一下 :heart:

`docker-compose.yml` 和 `Dockerfile` 裡面的指令也是有很多可以學習的 :wink:

這裡就不細講了:blush:

設定完了之後，接下來我們就可以啟動他了

```cmd
docker-compose up
```

接下來你會看到類似的畫面

![](https://i.imgur.com/GJWIgEP.png)

![](https://i.imgur.com/dVRRyrM.png)

假如你出現了類似的畫面

![](https://i.imgur.com/cCEmVBq.png)

代表 database 還在建立的時候，你的 web ( Django ) 就去連接他，

所以導致連接不上，這時候我們可以先終止他 ( 按 Ctrl+C )

接著在重新 `docker-compose up`

我們成功啟動了 ( db 連線也正常 )

![](https://i.imgur.com/iuCxLMY.png)

但你仔細看上圖，你會發現他說你還沒 migrate

接下來我們開啟另一個 cmd 進入 web 的 service

透過剛剛介紹的指令進入 service

```cmd
docker ps
docker exec -it <Container ID> bash
```

或是說也可以從 [Kitematic](https://kitematic.com/)進入

進入後我們可以開始 migrate

```cmd
python manage.py makemigrations musics
python manage.py migrate
```

![](https://i.imgur.com/zMmZKuL.png)

順便在建立一個 superuser

```cmd
python manage.py createsuperuser
```

接著我們可以試著使用 GUI 介紹連接 db

因為我們是用 [PostgreSQL](https://www.postgresql.org/)  ，可以透過 [pgadmin](https://www.pgadmin.org/) 連線

![](https://i.imgur.com/c9XfJQ3.png)

我們剛剛 migrate 的東西有存在

![](https://i.imgur.com/DhfxCMi.png)

我們不需要再重新啟動

直接可以開開心心的去瀏覽 [http://127.0.0.1:8000/api/music/](http://127.0.0.1:8000/api/music/)

大家一定會看到很熟悉的畫面

![](https://i.imgur.com/pzqZbdz.png)

接著依照自己剛剛設定的帳密登入進去即可

![](https://i.imgur.com/l6RZXsQ.png)

![](https://i.imgur.com/xeJtRJc.png)

以上整個環境，都是在 Docker 中 :open_mouth:

如果我們再 Ctrl+C 退出，重新啟動一次  `docker-compose up`

這次就不會再和你說你沒有 migrate 了

![](https://i.imgur.com/zIBkL3t.png)

## 查看 port 佔用狀況

這個推薦給大家，有時候會遇到 port 被佔用，用指令查比較方便

Windows

查看所有 port 的佔用狀況

```cmd
netstat -ano
```

查看指定 port 的佔用狀況，例如現在想要查看 port 5432 佔用的狀況

```cmd
netstat -aon|findstr "5432"
```

查看 PID 對應的 process

```cmd
tasklist|findstr "2016"
```

停止 PID 為 6093 的 process

```cmd
taskkill /f /PID 6093
```

停止 vscode.exe process

```cmd
taskkill /f /t /im vscode.exe
```

MAC

將 port 為 8000 的 process 全部停止

```cmd
sudo lsof -t -i tcp:8000 | xargs kill -9
```

查看指定 port 的佔用狀況，例如現在想要查看 port 5432 佔用的狀況

```cmd
lsof -i tcp:5432
```

## 後記：

Docker 算是我最近才開始接觸的，所以也算是新手，如果我有任何講錯的，歡迎和我說，我會在修改  :grinning:

我發現 Docker 可以玩的真的很多，像是可以考慮建立一個 CI Server，用 Jenkins 所提供的各種服務，

或是說也可以到 [Google Cloud Platform](https://cloud.google.com/?hl=zh-tw) 玩玩 Docker。

最後，希望大家在學習 Docker 的過程中，遇到不懂的，可以去找資料並且了解他，
順便補足一些之前不足的知識。

## 執行環境

* Mac
* Python 3.6.2
* windows 10

## Reference

* [https://docs.docker.com/](https://docs.docker.com/)

## License

MIT license
