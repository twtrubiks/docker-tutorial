# ENTRYPOINT

docker 指令中的 ENTRYPOINT 和 CMD 很像, 但有點不太一樣,

這邊簡單和大家說明一下:smile:

## CMD

範例 Dockerfile 如下

```Dockerfile
FROM alpine
CMD [ "ls"]
#ENTRYPOINT [ "ls" ]
```

build `docker build -t demo .`

執行 `docker run --rm demo`

以上使用沒甚麼問題,

可是如果今天我想要改一下指令(想直接列出 dev 裡面的資料),

指令改為如下

`docker run --rm demo dev`

```cmd
docker: Error response from daemon: failed to create shim: OCI runtime create failed: container_linux.go:380: starting container process caused: exec: "dev": executable file not found in $PATH: unknown.
```

你會發現出錯了, 因為他只執行了 `dev`, 而不是執行了 `ls dev`,

必須經過以下的調整(需要把完整的指令再寫一次)

`docker run --rm demo ls dev`

這樣就正常了, 成功顯示 dev 底下的東西.

但是這個在實際上有點麻煩, 因為如果指令非常長呢:question:

所以有了接下來要介紹的 ENTRYPOINT:smile:

## ENTRYPOINT

範例 Dockerfile 如下

```Dockerfile
FROM alpine
# CMD [ "ls"]
ENTRYPOINT [ "ls" ]
```

build `docker build -t demo .`

執行 `docker run --rm demo`

以上都是相同的.

如果我想要改一下指令(想直接列出 dev 裡面的資料),

指令改為如下

`docker run --rm demo dev`

成功顯示 dev 底下的東西.

(剛剛前面 CMD 的範例是會錯誤的, 但透過 ENTRYPOINT 可以避免這個問題.)

因為它是把指令再加上去的概念,

你可以簡單把它成想是 `ENTRYPOINT`(ls) + `CMD`(dev) 這樣.

還可以透過 bash 完成更複雜的變化,

可參考 [docker-entrypoint.sh](https://github.com/twtrubiks/docker-tutorial/blob/master/api/docker-entrypoint.sh)
