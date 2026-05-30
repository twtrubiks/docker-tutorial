# docker-tutorial

[English Version](README_en.md)

 Docker 基本教學 - 從無到有 Docker-Beginners-Guide

 教你用 [Docker](https://www.docker.com/) 建立 [Django](https://github.com/django/django) + [PostgreSQL](https://www.postgresql.org/) 📝

* [Youtube Tutorial PART 1 - Docker 基本教學 - 從無到有 Docker-Beginners-Guide](https://youtu.be/Wg5m0-Jyox8)
* [目錄](https://github.com/twtrubiks/docker-tutorial#%E7%94%A8-docker-%E5%AF%A6%E6%88%B0-django-%E4%BB%A5%E5%8F%8A-postgre) - [Youtube Tutorial PART 2 - 用 Docker 實戰 Django 以及 Postgre](https://youtu.be/aZ6woJ7qekE)
* [目錄](https://github.com/twtrubiks/docker-tutorial#%E5%85%B6%E4%BB%96%E7%AE%A1%E7%90%86-docker-gui-%E7%9A%84%E5%B7%A5%E5%85%B7) - [Youtube Tutorial PART 3 - Docker 基本教學 - 透過 portainer 管理  Docker](https://youtu.be/VZjHmBcEcew)
* [目錄](https://github.com/twtrubiks/docker-tutorial#docker-registry) - [Youtube Tutorial PART 4 - Docker push image to Docker Hub 教學](https://youtu.be/dVBKwmqO5e4)

其他說明

* [Youtube Tutorial - Ubuntu(Linux) 如何安裝 docker](https://youtu.be/eS_HMBC_RaA)
* [目錄](https://github.com/twtrubiks/docker-tutorial#docker-compose-networks) - [Youtube Tutorial - docker-compose networks 說明](https://youtu.be/wmV9WfkpyGk)
* [目錄](https://github.com/twtrubiks/docker-tutorial#docker-container-%E5%85%A7%E5%A6%82%E4%BD%95%E9%80%A3%E6%8E%A5%E5%88%B0%E6%9C%AC%E6%A9%9F-localhost-%E6%9C%8D%E5%8B%99) - [Youtube Tutorial - Docker container 內如何連接到本機 localhost 服務](https://youtu.be/KbaHWdVej9U)
* [目錄](https://github.com/twtrubiks/docker-tutorial#docker-compose-updown-%E5%92%8C-restart-%E7%9A%84%E5%B7%AE%E7%95%B0) - [Youtube Tutorial - docker-compose up/down 和 restart 的差異](https://youtu.be/nX-sbLPz-MU)
* [目錄](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-auto-run-linux) - [Youtube Tutorial - Linux 教學 - 開機自動啟動 docker / compose](https://youtu.be/c4YIQHCDLnQ)
* [目錄](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-env-tutorial) - [Youtube Tutorial - Docker 基本教學 - 在 docker compose 中善用 Environment variables](https://youtu.be/JwbI1aNKbtY)
* [目錄](https://github.com/twtrubiks/docker-tutorial#%E5%A6%82%E4%BD%95%E6%B8%85%E9%99%A4-docker-container-log) - [Youtube Tutorial - 如何清除 Docker container log](https://youtu.be/SiG0tmwhqqg)
* [目錄](https://github.com/twtrubiks/docker-tutorial#json-file-logging-driver) - [Youtube Tutorial - Docker 中的 JSON File logging driver(container log)](https://youtu.be/wb9bONgnFn4)
* [目錄](https://github.com/twtrubiks/docker-tutorial#health-check) - [Youtube Tutorial - docker 教學 Health Check](https://youtu.be/QffnQZgvmwE)
* [目錄](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-compose-override) - 介紹 docker-compose-override
* [目錄](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-compose-profiles) - 介紹 docker-compose-profiles
* [目錄](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-yaml-anchors) - 介紹 YAML Anchors
* [目錄](https://github.com/twtrubiks/docker-tutorial/tree/master/cadvisor_tutorial) - 介紹 cadvisor - 可監控 docker 容器

## 簡介

[Docker](https://www.docker.com/)

![](https://i.imgur.com/gDcSwcs.png)

***Containers as a Service ( CaaS ) - 容器如同服務***

算是近幾年才開始紅的技術，蠻多公司都有使用 Docker，而且真的很方便，值得大家去了解一下 :smile:

如果你有環境上不統一的問題？ 請用 Docker :smile:

如果你有每次建立環境都快抓狂的問題？ 請用 Docker :blush:

如果你想要高效率、輕量、秒開的環境，請用 Docker :blush:

如果你不想搞死自己，請用 Docker :smile:

如果你想潮到出水，請一定要用 Docker :laughing:

### 什麼是 Docker

[Docker](https://www.docker.com/) 是一個開源專案，出現於 2013 年初，最初是 Dotcloud 公司內部的 Side-Project。

它基於 Google 公司推出的 Go 語言實作。（ Dotcloud 公司後來改名為 Docker ）

技術原理我們這邊就不提了，簡單提一下他的好處。

我們先來看看官網的說明

Comparing Containers and Virtual Machines ( 傳統的虛擬化 )

![](https://i.imgur.com/IqiGyoJ.png)

從這張圖可以看出 Containers 並沒有 OS ，容量自然就小，而且啟動速度神快

詳細可參考 [https://www.docker.com/what-container](https://www.docker.com/what-container)

Virtual Machines 是什麼？

類似 [https://www.virtualbox.org/](https://www.virtualbox.org/)，我們可能用它裝裝看其他作業系統，例如說

我是 MAC，但我想玩 Windows，我就會在 MAC 中裝 VM 並且灌 Windows 系統。

一個表格了解 Docker 有多棒 :+1:

Feauture  | Containers                  |  Virtual Machines ( 傳統的虛擬化 )
--      | ----------            | ----------
 啟動   | 秒開 | 最快也要分鐘
 容量 | MB        | GB
 效能 | 快        | 慢
 支援數量 | 非常多 Containers        | 10多個就很了不起了
 複製相同環境 | 快        | 超慢

不理解 :question: :question: :question:

我們來看一張圖，包準你懂

![](https://i.imgur.com/H8wmOUh.jpg)

圖的來源
[https://blog.jayway.com/2015/03/21/a-not-very-short-introduction-to-docker/](https://blog.jayway.com/2015/03/21/a-not-very-short-introduction-to-docker/)

### 為什麼要使用 Docker

潮～ 不解釋 :satisfied:

#### 更有效率的利用資源

比起像是 [https://www.virtualbox.org/](https://www.virtualbox.org/)，Docker 的利用率更高，我們可以設定更多

的 Containers, 而且啟動速度飛快！！ :flushed:

#### 統一環境

相信大家都有每次搞電腦的環境都搞的很煩的經驗 :angry:

假設今天公司來了個新同事，就又要幫他建立一次環境 :expressionless:

不然就是，我的電腦 run 起來正常阿～ 你的怎麼不行，是不是 xxx 版本的關係阿 :joy:

相信大家多多少少都遇過上面這些事情，我們可以透過 Docker 來解決這些問題，

保持大家環境一致，而且要建立的時候也很快 :smile:

#### 對於 DevOps 的好處

對於 [DevOps](https://zh.wikipedia.org/wiki/DevOps) 來說，最希望的就是可以設定一次，將來在其他地方都可以快速建立環境且正常執行。

### Docker 概念

建議大家先了解一下 Docker 中的幾個名詞，分別為

***Image***

映像檔，可以把它想成是以前我們在玩 VM 的 Guest OS（ 安裝在虛擬機上的作業系統 ）。

Image 是唯讀（ R\O ）

***Container***

容器，利用映像檔（ Image ）所創造出來的，一個 Image 可以創造出多個不同的 Container，

Container 也可以被啟動、開始、停止、刪除，並且互相分離。

Container 在啟動的時候會建立一層在最外（上）層並且是讀寫模式（ R\W ）。

這張圖解釋了 Image 是唯讀（ R\O ）以及 Container 是讀寫模式（ R\W ） 的關係

![](https://i.imgur.com/wVvrWwJ.png)

更多關係可參考 [https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/#images-and-layers](https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/#images-and-layers)

***Registry***

可以把它想成類似 [GitHub](https://github.com/)，裡面存放了非常多的 Image ，可在 [Docker Hub](https://hub.docker.com/) 中查看。

更詳細的我這邊就不再解釋惹，留給大家做作功課 :stuck_out_tongue:

## 安裝

Windows

請先到 Docker 官網

[https://www.docker.com/docker-windows](https://www.docker.com/docker-windows)

下載 stable 版本

![](https://i.imgur.com/ryKtNXm.jpg)

接下來就是無腦安裝，安裝完後他會叫你登出電腦，點下去後就會幫你登出電腦

![](https://i.imgur.com/EE7XmYM.jpg)

接著如果你的電腦沒有啟用 [Hyper-V](https://msdn.microsoft.com/zh-tw/library/hh831531(v=ws.11).aspx) ，他會叫你重啟電腦
(一樣，點下去就對惹)

( 更多可 Hyper-V 介紹請參考 [https://docs.microsoft.com/zh-tw/virtualization/hyper-v-on-windows/about/](https://docs.microsoft.com/zh-tw/virtualization/hyper-v-on-windows/about/) )

![](https://i.imgur.com/YG79VE1.jpg)

重新開機後，你就會發現可愛的 Docker 在右下角蹦出來惹

![](https://i.imgur.com/zMgf36E.png)

我們可以再用 cmd 確認一下是否有成功安裝

```cmd
docker --version
docker-compose --version
```

![](https://i.imgur.com/k1o3GIz.png)

記得再設定一個東西 Shared Drives

![](https://i.imgur.com/a6dqWU8.jpg)

裝完了之後，建議大家再多裝一個 [Kitematic](https://kitematic.com/)，他是 GUI 介面的，方便你使用 Docker，

( 後面會再介紹一個更贊的 GUI 介面 [portainer](https://github.com/portainer/portainer)  :grin: )

我知道打指令很潮，但還是建議裝一下。

直接對著你的 Docker 圖示右鍵，就可以看到 [Kitematic](https://kitematic.com/)

![](https://i.imgur.com/gdVFFMT.png)

![](https://i.imgur.com/SRaHNCP.jpg)

下載回來直接解壓縮雙點擊即可使用

![](https://i.imgur.com/9zsU23B.png)

MAC

MAC 我本身也有，但因為更早之前就裝了，步驟就沒記錄了，基本上大同小異

[https://www.docker.com/docker-mac](https://www.docker.com/docker-mac)

Linux

[Youtube Tutorial-Ubuntu(Linux) 如何安裝 docker](https://youtu.be/eS_HMBC_RaA)

這裡使用 Ubuntu 當作範例,

雖然在 ubuntu 中有 `snap` 可以非常快速的安裝 docker,

但在這邊我們不使用 `snap` 的方法安裝 :smile:

請參考官方文件步驟安裝,

Get Docker Engine - Community for Ubuntu

[Get Docker Engine - Community for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

安裝後步驟 (optional :exclamation:), 但建議參考一下

[Post-installation steps for Linux](https://docs.docker.com/install/linux/linux-postinstall/)

docker-compose 的安裝

[docker-compose install](https://docs.docker.com/compose/install/)

系統資源分配問題,

假如你是使用 windows 或是 mac 的 docker,

你會有一個界面可以設定你要分多少的 cpu 以及 ram 給你的 docker,

通常會在 Preferences -> Advanced, 有 GUI 界面,

![](https://i.imgur.com/CWMQHxs.png)

但如果是使用 linux, 就不會有這個界面, 因為在 Linux 中,

會自動依照系統的資源進行分配.

## 指令介紹

接著介紹一些 Docker 的指令，

Docker 的指令真的很多，這裡就介紹我比較常用的或是實用的指令

查看目前 images

```cmd
docker images
```

建立 image

```cmd
docker create [OPTIONS] IMAGE [COMMAND] [ARG...]
```

詳細的參數可參考 [https://docs.docker.com/engine/reference/commandline/create/](https://docs.docker.com/engine/reference/commandline/create/)

範例 ( 建立一個名稱為  busybox 的 image )

```cmd
docker create -it --name busybox busybox
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

新建並啟動 Container

```cmd
docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
```

舉個例子

```cmd
docker run -d -p 80:80 --name my_image nginx
```

`-d` 代表在 Detached（ 背景 ）執行，如不加 `-d`，預設會 foreground ( 前景 ) 執行

`-p` 代表將本機的 80 port 的所有流量轉發到 container 中的 80 port

`--name` 設定 container 的名稱

在舉一個例子

```cmd
 docker run -it --rm busybox
```

`--rm` 代表當 exit container 時，會自動移除 container。 ( incompatible with -d )

更詳細的可參考 [https://docs.docker.com/engine/reference/run/](https://docs.docker.com/engine/reference/run/)

啟動 Container

```cmd
docker start [OPTIONS] CONTAINER [CONTAINER...]
```

如果想讓他在前景跑順便觀看輸出 , 可以使用以下指令

```cmd
docker start -a [OPTIONS] CONTAINER [CONTAINER...]
```

`--attach` 或 `-a` 代表 Attach STDOUT/STDERR and forward signals.

更詳細的可參考 [https://docs.docker.com/engine/reference/commandline/start/](https://docs.docker.com/engine/reference/commandline/start/)

（ container ID 寫幾個就可以了，和 Git 的概念是一樣的 ，

不了解 Git 可以參考 [Git-Tutorials GIT基本使用教學](https://github.com/twtrubiks/Git-Tutorials) ）

停止 Container

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

`--volumes , -v` 加上這個參數，會移除掉連接到這個 container 的 volume。

可參考 [https://docs.docker.com/engine/reference/commandline/rm/](https://docs.docker.com/engine/reference/commandline/rm/)

進入 Container

```cmd
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
docker exec -it <Container ID> bash
```

使用 root 使用者進入　

```cmd
docker exec -u 0 -it <Container ID> bash
docker exec -u root -it <Container ID> bash
```

打指令比較潮，或是說你也可以透過 [Kitematic](https://kitematic.com/) 進入。

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

查看 log

```cmd
docker logs [OPTIONS] CONTAINER
```

`--follow` , `-f`  ,  Follow log output

更詳細的可參考 [https://docs.docker.com/engine/reference/commandline/logs/](https://docs.docker.com/engine/reference/commandline/logs/)


從最後 100 行開始追蹤,

```cmd
docker logs -f --tail 100 CONTAINER
```

或是

```cmd
docker logs -f -n 100 CONTAINER
```

可以透過 `--since` 從指定時間到現在的 log,

例如,

```cmd
docker logs --since 2023-04-13T09:20:00 <container_id>
```

從 10 分鐘前到現在的 log

```cmd
docker logs --since 10m CONTAINER
```

1 小時前到現在的 log

```cmd
docker logs --since 1h CONTAINER
```

如果想指定時間, 查看特定區間的 logs,

可以先使用 `-t` 找出 docker 的時間格式,

```cmd
docker logs -t CONTAINER
```

接著就可以使用 `--since` 或 `--until` 指定時間段,

一定要用 docker 的時間格式, 不然會無法生效.

這邊來個組合, 找出 8:10 ~ 8:30 的全部 log

```cmd
docker logs --since 2023-12-10T8:10:00.346748975Z  --until 2023-12-10T8:30:00.346748975Z  CONTAINER
```

也可以把 log 寫進去檔案中,

```cmd
docker logs CONTAINER >> access.log
```

如果上述指令沒有生效, 請修改成以下

```cmd
docker logs CONTAINER >& access.log
```

也可以先過濾 log 再寫進檔案中,

```cmd
docker logs CONTAINER | grep "29/Mar/2022" >> access_tmp.log
```

如果上述指令沒有生效, 請修改成以下

```cmd
docker logs CONTAINER 2>&1 | grep "29/Mar/2022" >& access_tmp.log
```

顯示容器資源 ( CPU , I/O ...... )

```cmd
docker stats [OPTIONS] [CONTAINER...]
```

也可以加上 `--no-stream`

```cmd
docker stats --no-stream
```

`--no-stream` Disable streaming stats and only pull the first result.

注意 :exclamation: :exclamation: 這邊得到的 memory usage 會比實際上的還要小,

因為這邊的值是再減去 cache usage memory.

相關 issues 可參考 [https://github.com/moby/moby/issues/32253](https://github.com/moby/moby/issues/32253)

```txt
On Linux, the Docker CLI reports memory usage by subtracting cache usage from the total memory usage.
```

詳細說明可參考 [https://docs.docker.com/engine/reference/commandline/stats/](https://docs.docker.com/engine/reference/commandline/stats/)

也可參考 [https://docs.docker.com/config/containers/runmetrics/](https://docs.docker.com/config/containers/runmetrics/)

查看 container 中正在執行的 processes

```CMD
docker top CONTAINER
```

停止指定的 CONTAINER 中全部的 **processes**

```cmd
docker pause CONTAINER [CONTAINER...]
```

執行 `docker pause` 之後，可以試這用 `docker ps` 查看，會發現

還是有在執行，這裡拿  `docker stop`  比較一下，差異如下。

 `docker stop` : process 級別。

 `docker pause`: container 級別。

恢復指定暫停的 CONTAINER 中全部的 **processes**

```cmd
docker unpause CONTAINER [CONTAINER...]
```

docker tag

```cmd
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```

範例

```cmd
docker tag 0e5574283393 twtrubiks/nginx:version1.0
```

更多可參考 [https://docs.docker.com/engine/reference/commandline/tag/](https://docs.docker.com/engine/reference/commandline/tag/)

儲存 (備份) image 成 tar 檔案

```cmd

[OPTIONS] IMAGE [IMAGE...]
```

範例

```cmd
docker save busybox > busybox.tar
```

或

```cmd
docker save --output busybox.tar busybox
```

或 ( 也可以一次備份多個 )

```cmd
docker save -o images.tar postgres:9.6 busybox
```

更多可參考 [https://docs.docker.com/engine/reference/commandline/save/](https://docs.docker.com/engine/reference/commandline/save/)

載入 image

```cmd
docker load [OPTIONS]
```

範例

```cmd
docker load < busybox.tar
```

或

```cmd
docker load -i busybox.tar
```

更多可參考 [https://docs.docker.com/engine/reference/commandline/load/](https://docs.docker.com/engine/reference/commandline/load/)

顯示 image 的 history，查詢 image 的每一層

```cmd
docker history [OPTIONS] IMAGE
```

在 docker 中，一層一層的概念很重要。

![](https://i.imgur.com/NmImVby.png)

更多可參考 [https://docs.docker.com/engine/reference/commandline/history/](https://docs.docker.com/engine/reference/commandline/history/)

剛剛有教大家如何儲存 (備份) images， 載入 images，

還有另外一種是 export 和 import containers，

docker export container 請參考 [https://docs.docker.com/engine/reference/commandline/export/](https://docs.docker.com/engine/reference/commandline/export/)。

docker import container 請參考 [https://docs.docker.com/engine/reference/commandline/import/](https://docs.docker.com/engine/reference/commandline/import/)。

其他指令

刪除所有 dangling images

```cmd
docker image prune
```

移除全部 unused images (不只 dangling images)

```cmd
docker image prune -a
```

更多資訊可參考 [image_prune](https://docs.docker.com/engine/reference/commandline/image_prune/)

停止所有正在運行的 Container

```cmd
docker container stop $(docker ps -q)
```

更多資訊可參考 [container_stop](https://docs.docker.com/engine/reference/commandline/container_stop/)

移除全部停止的 containers

```cmd
docker container prune
```

更多資訊可參考 [container_prune](https://docs.docker.com/engine/reference/commandline/container_prune/)

在主機（本機）和 container 之間複製檔案

```cmd
docker cp [OPTIONS] SRC_PATH CONTAINER:DEST_PATH
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH
```

範例 1 ( 把主機的 config.json 複製進 container 的 /app 目錄 )

```cmd
docker cp ./config.json my_container:/app/config.json
```

這邊要注意 container 中有沒有對應的目錄，如果沒有，要先到 container 中建立對應的資料夾，

不然會出現類似這樣的錯誤 `Error response from daemon: Could not find the file ...`，

可以先用以下指令在 container 中把資料夾建立起來

```cmd
docker exec my_container mkdir -p /app
```

範例 2 ( 把 container 裡的 log 抓出來到主機的 output 目錄 )

```cmd
docker cp my_container:/var/log/app.log ./output
```

如果只是想在本機和 container 之間移動資料，又不想特別建立 Volume，最快的方式就是使用 `docker cp`。

更多資訊可參考 [docker cp](https://docs.docker.com/engine/reference/commandline/cp/)

### ENTRYPOINT

教學說明請點選 [entrypoint-tutorial](https://github.com/twtrubiks/docker-tutorial/tree/master/entrypoint-tutorial)

### Volume

接下來要介紹 Volume，Volume 是 Docker 最推薦存放 persisting data（ 數據 ）的機制，

使用 Volume 有下列優點

* Volumes are easier to back up or migrate than bind mounts.
* You can manage volumes using Docker CLI commands or the Docker API.
* Volumes work on both Linux and Windows containers.
* Volumes can be more safely shared among multiple containers.
* Volume drivers allow you to store volumes on remote hosts or cloud providers, to encrypt the contents of volumes, or to add other functionality.
* A new volume's contents can be pre-populated by a container.

在 container 的可寫層中，使用 volume 是一個比較好的選擇，因為他不會增加 container 的容量，

volume 的內容存在於 container 之外。

也可參考下圖

![](https://i.imgur.com/fiIt0kS.png)

更詳細的可參考 [https://docs.docker.com/engine/admin/volumes/volumes/](https://docs.docker.com/engine/admin/volumes/volumes/)

查看目前的 volume

```cmd
docker volume ls [OPTIONS]
```

創造一個 volume

```cmd
docker volume create [OPTIONS] [VOLUME]
```

刪除一個 volume

```cmd
docker volume rm [OPTIONS] VOLUME [VOLUME...]
```

查看 volume 詳細資料

```cmd
docker volume inspect [OPTIONS] VOLUME [VOLUME...]
```

移除全部未使用的 volume

```cmd
docker volume prune [OPTIONS]
```

也可以建立 readonly 的 volumes (容器內 readonly)

`docker-compose.yml` 方法如下,

```yml
version: '3.5'
services:
  nginx:
    image: nginx
    ports:
      - "80:80"
    volumes:
      - "nfs-data:/data:ro,z"

volumes:
    nfs-data:
```

如果要可讀寫, 就設定 `rw`.

volumes 在容器內的確不能寫 (只能讀)

![alt tag](https://i.imgur.com/ve4572t.png)

使用以下的指令查看 Mounts, 觀察它的 Mode

```cmd
docker inspect <container ID>
```

![alt tag](https://i.imgur.com/ex8A3Y5.png)

也可以建立 NFS volumes,

`docker-compose.yml` 方法如下,

```yml
version: '3.5'
services:
  nginx:
    image: nginx
    ports:
      - "80:80"
    volumes:
      - "nfs-data:/data"

volumes:
    nfs-data:
      driver: local
      driver_opts:
        type: nfs
        o: nfsvers=4,addr=ip,rw
        device: ":/path/to/dir"
```

可以用以下指令查看設定

```cmd
docker volume ls
docker inspect <volume name>
```

![alt tag](https://i.imgur.com/8mzUGsg.png)

NFS 相關文章可參考 [linux-nfs-server - 如何在 ubuntu 啟用 NFS Server](https://github.com/twtrubiks/linux-note/tree/master/linux-nfs-server)

### network

建議大家花點時間研究 docker 中的 network，會蠻有幫助的 :smiley:

查看目前 docker 的網路清單

```cmd
docker network ls [OPTIONS]
```

詳細可參考 [https://docs.docker.com/engine/userguide/networking/](https://docs.docker.com/engine/userguide/networking/)

docker 中的網路主要有三種 Bridge、Host、None，預設皆為 Bridge 模式。

指定 network 範例 ( 指定使用  `host` 網路 )

```cmd
docker run -it --name busybox --rm --network=host busybox
```

建立 network

```cmd
docker network create [OPTIONS] NETWORK
```

移除 network

```cmd
docker network rm NETWORK [NETWORK...]
```

移除全部未使用的 network

```cmd
docker network prune [OPTIONS]
```

查看 network 詳細資料

```cmd
docker network inspect [OPTIONS] NETWORK [NETWORK...]
```

將 container 連接 network

```cmd
docker network connect [OPTIONS] NETWORK CONTAINER
```

更多詳細資料可參考 [https://docs.docker.com/engine/reference/commandline/network_connect/](https://docs.docker.com/engine/reference/commandline/network_connect/)

Disconnect container  network

```cmd
docker network disconnect [OPTIONS] NETWORK CONTAINER
```

更多詳細資料可參考 [https://docs.docker.com/engine/reference/commandline/network_disconnect/](https://docs.docker.com/engine/reference/commandline/network_disconnect/)

#### User-defined networks

這個方法是官方推薦的 :thumbsup:

透過內建的 DNS 伺服器，可以直接使用容器名稱，就可解析出 IP，不需要再使用 IP 讓容器互相

溝通，我們只需要知道容器的名稱就可以連接到容器。

更多詳細資料可參考 [https://docs.docker.com/engine/userguide/networking/#user-defined-networks](https://docs.docker.com/engine/userguide/networking/#user-defined-networks)

## docker-compose

再來要介紹 docker-compose，可參考官網 [https://docs.docker.com/compose/](https://docs.docker.com/compose/)

![](https://i.imgur.com/YxrrO7t.png)

Compose 是定義和執行多 Container 管理的工具，不懂我在說什麼 :question: :question: :question:

試著想想看，通常一個 Web 都還會有 DB，甚至可能還有 [Redis](https://redis.io/) 或 [Celery](http://www.celeryproject.org/)，

所以說我們需要有 Compose 來管理這些，透過 `docker-compose.yml` ( YML 格式 ) 文件。

`docker-compose.yml` 的寫法可參考 [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)

也可以直接參考官網範例 [https://docs.docker.com/compose/compose-file/#compose-file-structure-and-examples](https://docs.docker.com/compose/compose-file/#compose-file-structure-and-examples)

Compose 的 Command-line 很多和 Docker 都是類似的，

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

然後如果你有很多個 `docker-compose.yml` `docker-compose-dev.yml`,

你可以透過 `-f` 決定你要執行哪一個, 範例如下,

```cmd
docker-compose -f ./docker-compose-dev.yml up -d
```

`-f` `--file FILE` Specify an alternate compose file

(default: `docker-compose.yml`)

`up` 這個功能很強大，建議可以參考 [https://docs.docker.com/compose/reference/up/](https://docs.docker.com/compose/reference/up/)

如果你希望每次都重新 build image，可以加上

`--build` ( Build images before starting containers. )

```cmd
docker-compose up -d --build
```

docker-compose down

```cmd
docker-compose down [options]
```

`down` 這個功能也建議可以參考 [https://docs.docker.com/compose/reference/down/](https://docs.docker.com/compose/reference/down/)

舉個例子

```cmd
docker-compose down -v
```

加個 `-v` 就會順便幫你把 volume 移除（ 移除你在 `docker-compose.yml` 裡面設定的 volume ）

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

檢查 `docker-compose.yml` 格式是否正確

```cmd
docker-compose config
```

如下指令，和 `docker exec` 一樣

```cmd
docker-compose exec
```

範例 ( 進入 web 這個 service 的 bash )

```cmd
docker-compose exec web bash
```

顯示被使用到的 container 中的 images 清單

```cmd
docker-compose images
```

移除  service containers

```cmd
docker-compose rm
```

Pushes images 到 docker hub

```cmd
docker-compose push
```

目前這個指令其實我也搞不太懂，可參考 [https://github.com/docker/compose/issues/4283](https://github.com/docker/compose/issues/4283)

官網也解釋的沒有很清楚 [https://docs.docker.com/compose/reference/push/](https://docs.docker.com/compose/reference/push/)

### docker-compose up/down 和 restart 的差異

* [Youtube Tutorial - docker-compose up/down 和 restart 的差異](https://youtu.be/nX-sbLPz-MU)

先來談 `docker-compose up/down`,

假如今天你修改了 `docker-compose.yml` 又或是更新了 image,

當你要重建 docker , 有幾種方法,

方法一.

先停止 container, 執行 `docker-compose down` 再執行 `docker-compose up`.

方法二.

不需要停止 container, 直接執行 `docker-compose up -d`.

(他會自動幫你重建, 很方便, 不需要多一步先關閉 container )

結論, 只要你的 `docker-compose.yml` 有任何變動, 一定要執行 `docker-compose up` 才會生效.

再來談 `docker-compose restart`,

請看官方文件 [docker-compose restart](https://docs.docker.com/compose/reference/restart/), 如果你對 `docker-compose.yml` 修改, 然後使用這個指令, 是**不會**生效的,

但是, 如果你是改 code (可能是 python code), 那這個指令是有效的.

### docker-compose networks

* [Youtube Tutorial - docker-compose networks 說明](https://youtu.be/wmV9WfkpyGk)

這邊多補充 docker-compose networks 的觀念，因為剛好最近有用到 :smile:

```yml
version: '3.5'
services:

    db:
      container_name: 'postgres'
      image: postgres
      environment:
        POSTGRES_PASSWORD: password123
      ports:
        - "5432:5432"
        # (HOST:CONTAINER)
      volumes:
        - pgdata:/var/lib/postgresql/data/
      networks:
        - proxy

    web:
      build: ./api
      command: python manage.py runserver 0.0.0.0:8000
      restart: always
      volumes:
        - api_data:/docker_api
        # (HOST:CONTAINER)
      ports:
        - "8000:8000"
        # (HOST:CONTAINER)
      depends_on:
        - db
      networks:
        - proxy

volumes:
    api_data:
    pgdata:

networks:
    proxy:
      # external:
        name: my_network
```

先把 version 改成 3.5，因為這版本才開始有 networks name 的概念，在

db 以及 web 中都加了 networks ( 自己定義的 )，定義的地方在最後面，

proxy 是名稱 ( 類似 volumes 的概念 )，`external` option 的意思代表

是不是要參考外部別人已經定義好的 network ( 所以如果找不到就會報錯 )，

但如果不加上 `external` option，也就代表是自己定義的，會幫你自動建立

你所定義的 network，名稱為 my_network。

如果你都完全沒有定義 networks，預設就是資料夾的名稱_default 。

### docker-compose ports 和 expose 差異

在 docker-compose 中有兩種方法可以暴露容器 ports，

分別是 ports 和 expose，

#### ports

```yml
...
ports:
  - "5000:5000"  # 绑定 container 中的 5000 port 到 本機(HOST) 的 5000 port
  # (HOST:CONTAINER)

  - "5001:5000"  # 绑定 container 中的 5000 port 到 本機(HOST) 的 5001 port

  - "5000"       # 绑定 container 中的 5000 port 到本機的任意 port (本機會隨機被分配到一個 port)
...
```

隨機 port 範例，

這邊使用 dpage/pgadmin4 這個 images 來示範，

```cmd
docker run -p 80 \
    -e "PGADMIN_DEFAULT_EMAIL=xxxrubiks@gmail.com" \
    -e "PGADMIN_DEFAULT_PASSWORD=SuperSecret" \
    -d dpage/pgadmin4
```

如果我們執行兩次以上指令，你會發現本機被分配到兩個隨機的 ports (如下圖)，

![alt tag](https://i.imgur.com/kkcnuJI.png)

本機被隨機分配到 32768 以及 32769 port，

這邊不管我們怎麼設定 ports，這些 ports 都會暴露給本機 (HOST) 以及其他 containers，這點很重要 :exclamation: :exclamation:

也就是說，如果本機 5001 ports 被使用了，其他的 containers 就無法使用 5001 ports，

可能要改成5002 ports 之類的。

#### expoese

```yml
...
expose:
  - "4000"
  - "6000"
...
```

expose 是將 port 暴露給其他容器。

expose 和 ports 最大的差別就是在 expose 不會暴露 port 給本機(HOST)，

所以 本機(HOST)絕對無法被訪問，但 containers 內可以被訪問，

所以說如果今天你的容器想要在 本機(HOST) 被訪問，一定要使用 ports 方式。

***ports 和 expose 差異***

簡單說，就是 ports 可以被 本機(HOST) 和 containers 訪問 ; 而

expose 是本機(HOST) 無法被訪問，只有在 containers 中可以被訪問。

## Docker container 內如何連接到本機 localhost 服務

* [Youtube Tutorial - Docker container 內如何連接到本機 localhost 服務](https://youtu.be/KbaHWdVej9U)

![alt tag](https://i.imgur.com/kQLcALp.png)

假設今天在本機上有一個 A 服務, 他是使用 docker run 起來的,

而本機上還有一個 B 服務, 是用 vscode run 起來的 (非 docker),

這時候我有一個需求, 我想要將我的 A 服務連線到我的 B 服務,

也就是從 docker 內的服務連接到本機 localhost.

比較簡單的方法, 就是透過 docker 內的這個參數,

`host.docker.internal:host-gateway`.

在你的 yml 裡面加上,

```yml
version: '3.5'
services:

  web:
    ......
    extra_hosts:
      - "host.docker.internal:host-gateway"
......
```

這樣當你在容器內, 就可以順利訪問本機 :smile:

```cmd
curl http://host.docker.internal:8069
```

也可以參考 [docker compose 安裝 pgadmin4](https://github.com/twtrubiks/docker-pgadmin4-tutorial#docker-compose-%E5%AE%89%E8%A3%9D-pgadmin4),

假設今天不考慮使用網路的方法, 如果一個容器 db 是在 5432, 另一個容器是 pgadmin4,

這樣要怎麼透過 pgadmin4 連接到我的本機的 5432 呢 😵‍💫

答案就是使用 `host.docker.internal:host-gateway`.

## Docker Registry

![](https://i.imgur.com/uAXUtxT.png)

可以把它想成是一個類似 github 的地方，只不過裡面變成是存 docker 的東西，當然，

也可以自己架，但會有一些額外的成本，像是網路，維護等等，這部分就要自己衡量了 :grinning:

接下來教大家如何將 image push 到 Docker Registry :smiley:

* [Youtube Tutorial PART 4 - Docker push image to Docker Hub 教學](https://youtu.be/dVBKwmqO5e4)

首先，先登入 [Docker Registry](https://hub.docker.com/)  ( 註冊流程很簡單，我就跳過了 )

```cmd
docker login
```

![](https://i.imgur.com/lm9GWTj.png)

舉個例子，先 run 一個 busybox 的容器

```cmd
docker run -it busybox
```

接著在裡面新增一筆資料

```cmd
 echo 'text' > data.txt
```

![](https://i.imgur.com/KCeZGQh.png)

然後打開另一個 terminal ，使用 `docker ps` 查看目前容器的 id

![](https://i.imgur.com/mBIhGBW.png)

再來使用像 git 一樣的方式 commit

docker commit

```cmd
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
```

可參考 [https://docs.docker.com/engine/reference/commandline/commit/](https://docs.docker.com/engine/reference/commandline/commit/)

```cmd
docker commit -m "test" 4fb4ef51e917 twtrubiks/my_busybox
```

`-m` commit message ，和 git 一樣。

twtrubiks/my_busybox 則為我們定義的 REPOSITORY。

如果需要 tag , 也可以增加

```cmd
docker commit -m "test" 4fb4ef51e917 twtrubiks/my_busybox:v1
```

（ 如果沒定義 tag , 則會顯示 latest ）

這時候可以用 `docker images` 查看

![](https://i.imgur.com/R548ail.png)

最後 push

```cmd
docker push twtrubiks/my_busybox
```

![](https://i.imgur.com/2ExgYpB.png)

docker 是一層一層的概念，他只會 push 自己新增的幾層上去而已，

所以不用擔心整個 image 很大，要上傳很久 :relaxed:

最後可以到 [https://hub.docker.com/](https://hub.docker.com/) 確認是否有成功 :smile:

![](https://i.imgur.com/W5P3YQL.png)

## 用 Docker 實戰 Django 以及 Postgre

* [Youtube Tutorial PART 2 - 用 Docker 實戰 Django 以及 Postgre](https://youtu.be/aZ6woJ7qekE)

上面介紹了那麼多，來實戰一下是必須的 :satisfied:

我們使用 [Django-REST-framework 基本教學 - 從無到有 DRF-Beginners-Guide](https://github.com/twtrubiks/django-rest-framework-tutorial) 來當範例

有幾個地方必須修改一下，

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
（ 這只是方便，實務上不會這樣使用 ）

再來是兩個很重要的檔案，分別為 `Dockerfile` 和 `docker-compose.yml`

`Dockerfile`

```text
FROM python:3.8.12
LABEL maintainer twtrubiks
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api/
RUN pip install -r requirements.txt
```

詳細可參考 [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)

`docker-compose.yml`

```yml
version: '3'
services:

    db:
      container_name: 'postgres'
      image: postgres
      environment:
        POSTGRES_PASSWORD: password123
      ports:
        - "5432:5432"
        # (HOST:CONTAINER)
      volumes:
        - pgdata:/var/lib/postgresql/data/

    web:
      build: ./api
      command: python manage.py runserver 0.0.0.0:8000
      restart: always
      volumes:
        - api_data:/docker_api
        # (HOST:CONTAINER)
      ports:
        - "8000:8000"
        # (HOST:CONTAINER)
      depends_on:
        - db

volumes:
    api_data:
    pgdata:
```

詳細可參考 [https://docs.docker.com/compose/compose-file/#compose-file-structure-and-examples](https://docs.docker.com/compose/compose-file/#compose-file-structure-and-examples)

溫馨小提醒 1  :heart:

可能有人會問為什麼我是使用 `0.0.0.0`，而不是使用 `127.0.0.1` :question: :question:

```cmd
python manage.py runserver 0.0.0.0:8000
```

`127.0.0.1`，並不代表真正的 **本機**，我們經常認為他是本機是因為我們電腦的 `host` 預設都幫你設定好了 :smirk:

詳細的 `host` 設定教學可參考 [hosts-設定檔 以及 查詢內網 ip](https://github.com/twtrubiks/docker-django-nginx-uswgi-postgres-tutorial#hosts-設定檔-以及-查詢內網-ip)，

`0.0.0.0` 才是真正的代表，**當下 ( 本 ) 網路中的本機** :pencil2:

如果大家想更深入的了解，可 google 再進一步的了解 `127.0.0.1` 以及 `0.0.0.0` 的差異 :smile:

溫馨小提醒 2  :heart:

這邊要特別提一下 `depends_on` 這個參數，

詳細可參考 [https://docs.docker.com/compose/compose-file/#depends_on](https://docs.docker.com/compose/compose-file/#depends_on)，

上面連結中有一段說明很值得看

****depends_on does not wait for db and redis to be 「ready」 before starting web - only until they have been started. If you need to wait for a service to be ready, see Controlling startup order for more on this problem and strategies for solving it.****

以我的 [docker-compose.yml](https://github.com/twtrubiks/docker-tutorial/blob/master/docker-compose.yml) 為例，啟動順序雖然為 db -> web，**但他不會等待 db 啟動完成後才啟動 web**，

也就是說，還是有可能 **web 比 db 先啟動完成**，這樣就需要重啟 web service，否則會無法連上 db :sob:

如果真的要控制啟動順序，請參考 [Controlling startup order](https://docs.docker.com/compose/startup-order/)。

溫馨小提醒 3  :heart:

`docker-compose.yml` 其實使用 `docker run` 也是可以完成的，例如這個範例中，如果使用

`docker run` 來寫，會變成這樣。

首先，為了讓容器彼此可以溝通，我們先建立一個網路 ( User-defined networks )，

```cmd
docker network create my_network
```

db 容器

```cmd
docker run --name db -v pgdata:/var/lib/postgresql/data/ -p 5432:5432 --network=my_network -e POSTGRES_PASSWORD=password123 postgres
```

接下來先去 api 資料夾中 build 出 image

```cmd
docker build --tag web_image .
```

`--tag , -t` , tag 這個 image 名稱為 web_image

也可以是

```cmd
docker build -t user/repo:tag .
```

web 容器

```cmd
docker run --name web -v api_data:/docker_api -p 8000:8000 --network=my_network --restart always web_image python manage.py runserver 0.0.0.0:8000
```

以上這樣，和 `docker-compose.yml`  其實是一樣的 :open_mouth:

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

:exclamation: [commit](https://github.com/twtrubiks/docker-tutorial/commit/398cb2fc375af8926cfe1eeabda33da018437897) 已經更新為自動 migrate :exclamation:

但你仔細看上圖，你會發現他說你還沒 migrate

接下來我們開啟另一個 cmd 進入 web 的 service，

透過剛剛介紹的指令進入 service

```cmd
docker ps
docker exec -it <Container ID> bash
```

或是說也可以從 [Kitematic](https://kitematic.com/) 進入，

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

:exclamation: [commit](https://github.com/twtrubiks/docker-tutorial/commit/398cb2fc375af8926cfe1eeabda33da018437897) 已經更新為自動建立 superuser :exclamation:

請參考 [docker-compose.yml](https://github.com/twtrubiks/docker-tutorial/blob/master/docker-compose.yml) 中的 environment ( 如下 ),

`DJANGO_SUPERUSER_USERNAME` `DJANGO_SUPERUSER_PASSWORD` `DJANGO_SUPERUSER_EMAIL`

接著我們可以試著使用 GUI 介紹連接 db，

因為我們是用 [PostgreSQL](https://www.postgresql.org/)  ，可以透過 [pgadmin](https://www.pgadmin.org/) 連線

![](https://i.imgur.com/2Hdt7wU.png)

我們剛剛 migrate 的東西確實有存在

![](https://i.imgur.com/PEUfGRy.png)

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

## 其他管理 Docker GUI 的工具

* [Youtube Tutorial PART 3 - Docker 基本教學 - 透過 portainer 管理  Docker](https://youtu.be/VZjHmBcEcew)

除了 [Kitematic](https://kitematic.com/) 之外，還有其他不錯的推薦給大家，

這次要介紹的就是 [portainer](https://github.com/portainer/portainer) 功能強大又好用 :fire:

其實如果去看看 [Kitematic](https://github.com/docker/kitematic) 以及 [portainer](https://github.com/portainer/portainer) 的 github，

你會發現 [portainer](https://github.com/portainer/portainer) 感覺比較有在 maintenance :smile:

而且我使用了 [portainer](https://github.com/portainer/portainer) 之後，真心大推 :smiley:

安裝方法可參考 [https://portainer.io/install.html](https://portainer.io/install.html)

```cmd
docker volume create portainer_data
docker run --name=portainer -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```

`-d` `-p` 在前面的 `docker run` 有介紹過代表的含意，`--name` 只是命名而已。

`Note 1`: The -v /var/run/docker.sock:/var/run/docker.sock option is available on Linux environments only.

`Note 2`: The -v portainer_data:/data portainer/portainer option will persist Portainer data in portainer_data on the host where Portainer is running. You can specify another location on your filesystem.

（ 建立起來之後，就依照 container 的操作即可 ）

之後查看 [http://localhost:9000/](http://localhost:9000/) 就會看到下圖

然後設定帳號、密碼

![](https://i.imgur.com/exdMf2p.png)

選 Local or Remote

![](https://i.imgur.com/3mkNMxF.png)

畫面真的不錯看，而且資訊也很豐富 :heart_eyes:

![](https://i.imgur.com/ynoqTZT.png)

相信我，你使用完他之後，你會默默的邊緣化 [Kitematic](https://kitematic.com/) :smirk:

## 查看 port 佔用狀況

這個推薦給大家，有時候會遇到 port 被佔用，用指令查比較方便

Linux

安裝 net-tools

```cmd
sudo apt install net-tools
```

查看誰佔用 80 port

```cmd
sudo netstat -lnp | grep -w ':80'
```

`-l`, `--listening` display listening server sockets.

`-n`, `--numeric` don't resolve names.

`-p`, `--programs` display PID/Program name for sockets.

也可以使用 `lsof`

```cmd
sudo lsof -i :80
```

`-i` select IPv[46] files.

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

## 在 Linux 中自動啟動 docker

[在 Linux 中自動啟動 docker](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-auto-run-linux)

## 如何清除 Docker container log

[Youtube Tutorial - 如何清除 Docker container log](https://youtu.be/SiG0tmwhqqg)

docker 的 container log 都會在 `/var/lib/docker/containers` 裡面

( 前提是你使用官方的安裝方法, [Youtube Tutorial - Ubuntu(Linux) 如何安裝 docker](https://youtu.be/eS_HMBC_RaA))

如果你是使用 `snap` 安裝 docker, 路徑則會在 `/var/snap/docker/common/var-lib-docker/containers`.

![alt tag](https://i.imgur.com/sK5k4Iw.png)

log 是一個 json 的檔案

![alt tag](https://i.imgur.com/feSGmcm.png)

如果你一直不去管他, log 就會越來越大 :scream:

以下狀況這個 log 會被清除, 就是修改了 `docker-compose.yml` 或是

你執行了 `docker-compose down`, 這些 logs 都會被清除 (因為 containers 重新建立).

(`docker-compose stop` 不受影響, 因為只是暫停而已)

建立大家可參考 [docker-compose up/down 和 restart 的差異](https://github.com/twtrubiks/docker-tutorial#docker-compose-updown-%E5%92%8C-restart-%E7%9A%84%E5%B7%AE%E7%95%B0)

那你可能會問我, 如果我很長一段時間都不會修改 `docker-compose.yml` 以及執行

`docker-compose down` 該怎麼辦 :sob: (因為 log 可能會長很快)

這邊提供大家一個方法, 使用 linux 中的 truncate 指令(可參考 [ Linux 指令教學 - truncate](https://github.com/twtrubiks/linux-note#truncate))

刪除全部 container 的 logs

```cmd
truncate -s 0 /var/lib/docker/containers/*/*-json.log
```

但是有時候只希望針對(清除)某個 container 的 logs, 這時候就可以使用以下的指令

```cmd
truncate -s 0 $(docker inspect --format='{{.LogPath}}' <container_name_or_id>)
```

(`container_name_or_id` 請換上自己 container 的 id 或 name)

其中的 `docker inspect --format='{{.LogPath}}' <container_name_or_id>` 只是顯示路徑而已.

![alt tag](https://i.imgur.com/TKCCdio.png)

但還有一個更好的方法, 直接透過 docker 內的 JSON File logging driver.

## JSON File logging driver

[Youtube Tutorial - Docker 中的 JSON File logging driver(container log)](https://youtu.be/wb9bONgnFn4)

在 docker 中 json-file driver 是默認的 default logging driver, 詳細可參考 [json-file](https://docs.docker.com/config/containers/logging/json-file/)

所以我們可以透過這個設定限制 log 的大小,

```yaml
logging:
  driver: "json-file"
  options:
    max-file: "1"    # default 是 1
    max-size: "200m" # default 是 -1, 也就是沒有限制
```

設定完之後重新啟動 docker-compose, 可以使用以下的指令查看是否生效

```cmd
docker inspect --format '{{.HostConfig.LogConfig}}' CONTAINER
```

![alt tag](https://i.imgur.com/L6Z7bYX.png)

這樣設定完之後, 就不用再擔心 container log 吃掉大量的容量了 :smile:

## Health Check

* [Youtube Tutorial - docker 教學 Health Check](https://youtu.be/QffnQZgvmwE)

直接來看一個範例 [docker-compose.yml](https://github.com/twtrubiks/odoo-docker-tutorial/blob/15.0/docker-compose.yml)

```yml
version: '3.5'
services:
  web:
    image: odoo:17.0
    depends_on:
      db:
        condition: service_healthy
    ports:
      - "8069:8069"
    healthcheck:
      test: curl -fs http://localhost:8069/web/database/selector || exit 1
      interval: 10s
      timeout: 5s
      retries: 5
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./config:/etc/odoo

  db:
    image: postgres:16
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
      - PGDATA=/var/lib/postgresql/data/pgdata
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U odoo"]
      interval: 10s
      timeout: 5s
      retries: 5
    volumes:
      - odoo-db-data:/var/lib/postgresql/data/pgdata

volumes:
    odoo-web-data:
    odoo-db-data:

```

當執行時, 你會發現多了一個 `health: starting` 如下圖,

![alt tag](https://i.imgur.com/j4TBQ7M.png)

當(每)過了 10 秒 (`interval: 10s`) 之後, 如果順利啟動會變成 `(healthy)` 如下圖,

![alt tag](https://i.imgur.com/g8ysqZ0.png)

當(每)過了 10 秒之後, 如果連續失敗很多次 (`retries: 5`),

則會顯示 `(unhealthy)` 如下圖,

![alt tag](https://i.imgur.com/zJhJf6u.png)

docker 的 Health Check 會回傳你數字,

0 代表成功，container is healthy

1 代表失敗，假設失敗超過指定次數(`retries: 5`), container is unhealthy

至於 depends_on 底下的 `condition: service_healthy` 代表必須檢查通過,

才會啟動, 可參考 [Control startup](https://docs.docker.com/compose/startup-order/#control-startup), 有以下三種,

`service_started` 如果沒有特別指定, 就是這一種.

`service_healthy`

`service_completed_successfully`

## 後記：

Docker 算是我最近才開始接觸的，所以也算是新手，如果我有任何講錯的，歡迎和我說，我會再修改  :grinning:

Docker 可以玩的真的很多，延伸參考

* [實戰 Docker + Jenkins + Django + Postgres 📝](https://github.com/twtrubiks/docker-jenkins-django-tutorial) - 結合 Jenkins

* [Docker + Django + Nginx + uWSGI + Postgres 基本教學 - 從無到有](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial)

* [實戰 Docker + Django + Nginx + uWSGI + Postgres - Load Balance 📝](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-load-balance-tutorial)

也可以再玩玩 **Docker Swarm** ( 分散式系統 ) :satisfied:

* [Docker Swarm 基本教學 - 從無到有 Docker-Swarm-Beginners-Guide📝](https://github.com/twtrubiks/docker-swarm-tutorial)

最後，希望大家在學習 Docker 的過程中，遇到不懂的，可以去找資料並且了解他，
順便補足一些之前不足的知識。

## 執行環境

* Mac
* Python 3.8.12
* windows 10

## Reference

* [https://docs.docker.com/](https://docs.docker.com/)
* [portainer](https://github.com/portainer/portainer)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡 :laughing:

綠界科技ECPAY ( 不需註冊會員 )

![alt tag](https://payment.ecpay.com.tw/Upload/QRCode/201906/QRCode_672351b8-5ab3-42dd-9c7c-c24c3e6a10a0.png)

[贊助者付款](http://bit.ly/2F7Jrha)

歐付寶 ( 需註冊會員 )

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## 贊助名單

[贊助名單](https://github.com/twtrubiks/Thank-you-for-donate)

## License

MIT license
