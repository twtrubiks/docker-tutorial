## 在 Linux 中自動啟動 docker

[Youtube Tutorial - Linux 教學 - 開機自動啟動 docker / compose](https://youtu.be/c4YIQHCDLnQ)

假設今天我們有一個 docker-compose.yml 檔案，我希望每次 Linux 開機的時候都自動啟動。

先在 `/etc/systemd/system` 底下建立一個 `.service` 檔案，

舉個例子 `/etc/systemd/system/docker-compose-app.service`

```cmd
sudo vim docker-compose-app.service
```

`docker-compose-app.service` 檔案內容如下，

```cmd
[Unit]
Description=my service
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/home/twtrubiks/my-docker-run
ExecStart=/usr/local/bin/docker-compose up -d
ExecStop=/usr/local/bin/docker-compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

`WorkingDirectory` 為工作目錄，my-docker-run 資料夾裡面就是 `docker-compose.yml`，

`ExecStart` 為執行的指令。

其他參數或更多參數的說明再麻煩大家自行研究。

設定完之後，可以使用以下指定啟動，

啟動服務 start service

```cmd
systemctl start docker-compose-app
```

啟動開機自動啟動 enable service ( auto-start )

```cmd
systemctl enable docker-compose-app
```

查看當前服務狀態 show status of service

```cmd
systemctl status docker-compose-app
```

systemctl 說明可參考 [linux-note](https://github.com/twtrubiks/linux-note/tree/master/systemctl-tutorial)。