# Automatically start Docker in Linux

[中文版](README.md)

[Youtube Tutorial - Linux Tutorial - Automatically start docker / compose on boot](https://youtu.be/c4YIQHCDLnQ)

Suppose we have a `docker-compose.yml` file, and I want it to start automatically every time Linux boots up.

First, create a `.service` file under `/etc/systemd/system`.

For example, `/etc/systemd/system/docker-compose-app.service`

```cmd
sudo vim docker-compose-app.service
```

The content of the `docker-compose-app.service` file is as follows:

```ini
[Unit]
Description=my service
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/home/twtrubiks/my-docker-run
ExecStartPre=/bin/sleep 3
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

`WorkingDirectory` is the working directory. The `my-docker-run` folder contains the `docker-compose.yml`.

`ExecStart` is the command to be executed.

For explanations of other parameters or more parameters, please do your own research.

After setting it up, you can use the following command to start it.

Start the service

```cmd
systemctl start docker-compose-app
```

Enable the service to start automatically on boot

```cmd
systemctl enable docker-compose-app
```

Show the status of the service

```cmd
systemctl status docker-compose-app
```

For an explanation of `systemctl`, please refer to [linux-note](https://github.com/twtrubiks/linux-note/tree/master/systemctl-tutorial).
