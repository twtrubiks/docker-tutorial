# docker-tutorial

[中文版](README.md)

Docker Beginners Guide - From Scratch

Learn how to use [Docker](https://www.docker.com/) to build [Django](https://github.com/django/django) + [PostgreSQL](https://www.postgresql.org/) 📝

* [Youtube Tutorial PART 1 - Docker Beginners Guide - From Scratch](https://youtu.be/Wg5m0-Jyox8)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial#%E7%94%A8-docker-%E5%AF%A6%E6%88%B0-django-%E4%BB%A5%E5%8F%8A-postgre) - [Youtube Tutorial PART 2 - Hands-on with Docker, Django, and PostgreSQL](https://youtu.be/aZ6woJ7qekE)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial#%E5%85%B6%E4%BB%96%E7%AE%A1%E7%90%86-docker-gui-%E7%9A%84%E5%B7%A5%E5%85%B7) - [Youtube Tutorial PART 3 - Docker Basic Tutorial - Managing Docker with Portainer](https://youtu.be/VZjHmBcEcew)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial#docker-registry) - [Youtube Tutorial PART 4 - Tutorial on Pushing Docker Images to Docker Hub](https://youtu.be/dVBKwmqO5e4)

Other Information

* [Youtube Tutorial - How to install Docker on Ubuntu (Linux)](https://youtu.be/eS_HMBC_RaA)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial#docker-compose-networks) - [Youtube Tutorial - Explanation of docker-compose networks](https://youtu.be/wmV9WfkpyGk)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial#docker-container-%E5%85%A7%E5%A6%82%E4%BD%95%E9%80%A3%E6%8E%A5%E5%88%B0%E6%9C%AC%E6%A9%9F-localhost-%E6%9C%8D%E5%8B%99) - [Youtube Tutorial - How to connect to a localhost service from within a Docker container](https://youtu.be/KbaHWdVej9U)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial#docker-compose-updown-%E5%92%8C-restart-%E7%9A%84%E5%B7%AE%E7%95%B0) - [Youtube Tutorial - The difference between docker-compose up/down and restart](https://youtu.be/nX-sbLPz-MU)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-auto-run-linux) - [Youtube Tutorial - Linux Tutorial - Automatically start docker/compose on boot](https://youtu.be/c4YIQHCDLnQ)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-env-tutorial) - [Youtube Tutorial - Docker Basic Tutorial - Making good use of Environment variables in docker-compose](https://youtu.be/JwbI1aNKbtY)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial#%E5%A6%82%E4%BD%95%E6%B8%85%E9%99%A4-docker-container-log) - [Youtube Tutorial - How to clear Docker container logs](https://youtu.be/SiG0tmwhqqg)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial#json-file-logging-driver) - [Youtube Tutorial - JSON File logging driver in Docker (container log)](https://youtu.be/wb9bONgnFn4)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial#health-check) - [Youtube Tutorial - Docker Tutorial Health Check](https://youtu.be/QffnQZgvmwE)
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-compose-override) - Introduction to docker-compose-override
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-compose-profiles) - Introduction to docker-compose-profiles
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-yaml-anchors) - Introduction to YAML Anchors
* [Table of Contents](https://github.com/twtrubiks/docker-tutorial/tree/master/cadvisor_tutorial) - Introduction to cAdvisor - for monitoring Docker containers

## Introduction

[Docker](https://www.docker.com/)

![](https://i.imgur.com/gDcSwcs.png)

***Containers as a Service (CaaS)***

This technology has become popular in recent years, and many companies use Docker. It's really convenient and worth learning about. :smile:

If you have problems with inconsistent environments, use Docker! :smile:

If you're driven crazy every time you set up an environment, use Docker! :blush:

If you want a high-efficiency, lightweight environment that starts in seconds, use Docker! :blush:

If you don't want to drive yourself crazy, use Docker! :smile:

If you want to be super cool, you must use Docker! :laughing:

### What is Docker?

[Docker](https://www.docker.com/) is an open-source project that appeared in early 2013, initially as a side project within Dotcloud.

It is implemented in the Go language, which was launched by Google. (Dotcloud later changed its name to Docker).

We won't go into the technical principles here, but let's briefly mention its benefits.

First, let's look at the official website's explanation:

Comparing Containers and Virtual Machines

![](https://i.imgur.com/IqiGyoJ.png)

From this diagram, you can see that Containers do not have an OS, so they are naturally smaller in size and start up incredibly fast.

For details, see [https://www.docker.com/what-container](https://www.docker.com/what-container)

What are Virtual Machines?

Similar to [https://www.virtualbox.org/](https://www.virtualbox.org/), we might use it to install other operating systems. For example,

I'm on a MAC, but I want to use Windows, so I'll install a VM on my MAC and install the Windows system.

A table to understand how great Docker is :+1:

| Feature | Containers | Virtual Machines (Traditional Virtualization) |
| --- | --- | --- |
| Startup | Seconds | Minutes at best |
| Size | MB | GB |
| Performance | Fast | Slow |
| Number Supported | Many Containers | A dozen is a lot |
| Replicating Environment | Fast | Very Slow |

Don't get it? :question: :question: :question:

Let's look at a diagram, I guarantee you'll understand.

![](https://i.imgur.com/H8wmOUh.jpg)

Image source:
[https://blog.jayway.com/2015/03/21/a-not-very-short-introduction-to-docker/](https://blog.jayway.com/2015/03/21/a-not-very-short-introduction-to-docker/)

### Why use Docker?

It's cool~ No explanation needed :satisfied:

#### More efficient use of resources

Compared to something like [https://www.virtualbox.org/](https://www.virtualbox.org/), Docker has higher utilization. We can set up more

Containers, and they start up incredibly fast! :flushed:

#### Unified environment

I believe everyone has had the frustrating experience of setting up a computer environment. :angry:

If a new colleague joins the company, you have to set up the environment for them all over again. :expressionless:

Or, "It runs fine on my machine~ Why doesn't it work on yours? Is it because of version xxx?" :joy:

I believe everyone has more or less encountered these situations. We can solve these problems with Docker,

keeping everyone's environment consistent, and it's fast to set up. :smile:

#### Benefits for DevOps

For [DevOps](https://en.wikipedia.org/wiki/DevOps), the ideal scenario is to configure once and be able to quickly set up the environment and run it correctly anywhere in the future.

### Docker Concepts

It's recommended to first understand a few terms in Docker:

***Image***

An image can be thought of as the Guest OS we used to play with in VMs (the operating system installed on a virtual machine).

Images are read-only (R/O).

***Container***

A container is created from an image. One image can create multiple different containers.

Containers can be started, begun, stopped, deleted, and are isolated from each other.

When a container starts, it creates a read-write (R/W) layer on the outermost (top) layer.

This diagram explains the relationship between read-only (R/O) images and read-write (R/W) containers.

![](https://i.imgur.com/wVvrWwJ.png)

For more on this relationship, see [https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/#images-and-layers](https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/#images-and-layers)

***Registry***

You can think of it as something like [GitHub](https://github.com/), which stores a large number of images. You can browse them on [Docker Hub](https://hub.docker.com/).

I won't explain in more detail here, I'll leave it for you to do your homework. :stuck_out_tongue:

## Installation

Windows

First, go to the official Docker website

[https://www.docker.com/docker-windows](https://www.docker.com/docker-windows)

Download the stable version

![](https://i.imgur.com/ryKtNXm.jpg)

Next is a straightforward installation. After installation, it will ask you to log out of your computer. Click it and it will log you out.

![](https://i.imgur.com/EE7XmYM.jpg)

Then, if your computer does not have [Hyper-V](https://msdn.microsoft.com/en-us/library/hh831531(v=ws.11).aspx) enabled, it will ask you to restart your computer.
(Again, just click it)

(For more information on Hyper-V, see [https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/))

![](https://i.imgur.com/YG79VE1.jpg)

After restarting, you will see the cute Docker icon pop up in the bottom right corner.

![](https://i.imgur.com/zMgf36E.png)

We can use cmd to confirm if the installation was successful.

```cmd
docker --version
docker-compose --version
```

![](https://i.imgur.com/k1o3GIz.png)

Remember to set up one more thing: Shared Drives

![](https://i.imgur.com/a6dqWU8.jpg)

After installation, it is recommended to install [Kitematic](https://kitematic.com/) as well. It has a GUI interface, which makes it easier to use Docker.

(Later, I will introduce an even better GUI interface, [portainer](https://github.com/portainer/portainer) :grin:)

I know typing commands is cool, but it's still recommended to install it.

Right-click on your Docker icon, and you will see [Kitematic](https://kitematic.com/).

![](https://i.imgur.com/gdVFFMT.png)

![](https://i.imgur.com/SRaHNCP.jpg)

Download, unzip, and double-click to use.

![](https://i.imgur.com/9zsU23B.png)

MAC

I also have a MAC, but since I installed it a long time ago, I didn't record the steps. It's basically the same.

[https://www.docker.com/docker-mac](https://www.docker.com/docker-mac)

Linux

[Youtube Tutorial - How to install Docker on Ubuntu (Linux)](https://youtu.be/eS_HMBC_RaA)

Here we use Ubuntu as an example.

Although you can install docker very quickly in ubuntu using `snap`,

we will not use the `snap` method here. :smile:

Please follow the official documentation for installation steps.

Get Docker Engine - Community for Ubuntu

[Get Docker Engine - Community for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

Post-installation steps (optional :exclamation:), but it is recommended to take a look.

[Post-installation steps for Linux](https://docs.docker.com/install/linux/linux-postinstall/)

docker-compose installation

[docker-compose install](https://docs.docker.com/compose/install/)

System resource allocation issue,

If you are using docker for windows or mac,

you will have an interface to set how much cpu and ram you want to allocate to your docker,

usually in Preferences -> Advanced, there is a GUI interface,

![](https://i.imgur.com/CWMQHxs.png)

But if you are using linux, there will be no such interface, because in Linux,

resources will be allocated automatically according to the system's resources.

## Command Introduction

Next, let's introduce some Docker commands.

There are really a lot of Docker commands, so here I will only introduce the ones I use more often or find more practical.

View current images

```cmd
docker images
```

Create an image

```cmd
docker create [OPTIONS] IMAGE [COMMAND] [ARG...]
```

For detailed parameters, see [https://docs.docker.com/engine/reference/commandline/create/](https://docs.docker.com/engine/reference/commandline/create/)

Example (create an image named busybox)

```cmd
docker create -it --name busybox busybox
```

Delete an Image

```cmd
docker rmi [OPTIONS] IMAGE [IMAGE...]
```

View currently running containers

```cmd
docker ps
```

View all containers (including stopped ones)

```cmd
docker ps -a
```

Create and start a Container

```cmd
docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
```

For example

```cmd
docker run -d -p 80:80 --name my_image nginx
```

`-d` means run in Detached (background) mode. If `-d` is not added, it will run in the foreground by default.

`-p` means forward all traffic from port 80 of the host to port 80 of the container.

`--name` sets the name of the container.

Another example

```cmd
 docker run -it --rm busybox
```

`--rm` means that when you exit the container, the container will be automatically removed. (incompatible with -d)

For more details, see [https://docs.docker.com/engine/reference/run/](https://docs.docker.com/engine/reference/run/)

Start a Container

```cmd
docker start [OPTIONS] CONTAINER [CONTAINER...]
```

If you want to run it in the foreground and watch the output, you can use the following command

```cmd
docker start -a [OPTIONS] CONTAINER [CONTAINER...]
```

`--attach` or `-a` means Attach STDOUT/STDERR and forward signals.

For more details, see [https://docs.docker.com/engine/reference/commandline/start/](https://docs.docker.com/engine/reference/commandline/start/)

(You only need to write a few characters of the container ID, the concept is the same as Git.

If you don't understand Git, you can refer to [Git-Tutorials GIT Basic Usage Tutorial](https://github.com/twtrubiks/Git-Tutorials))

Stop a Container

```cmd
docker stop [OPTIONS] CONTAINER [CONTAINER...]
```

Restart a Container

```cmd
docker restart [OPTIONS] CONTAINER [CONTAINER...]
```

Delete a Container

```cmd
docker rm [OPTIONS] CONTAINER [CONTAINER...]
```

`--volumes , -v` Adding this parameter will remove the volumes associated with this container.

See [https://docs.docker.com/engine/reference/commandline/rm/](https://docs.docker.com/engine/reference/commandline/rm/)

Enter a Container

```cmd
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
docker exec -it <Container ID> bash
```

Enter as root user

```cmd
docker exec -u 0 -it <Container ID> bash
docker exec -u root -it <Container ID> bash
```

Typing commands is cooler, or you can enter through [Kitematic](https://kitematic.com/).

[](https://i.imgur.com/Yui1UZb.png)

After we enter the Container, sometimes we want to see the Linux version inside.

You can use the following command to check

```cmd
cat /etc/os-release
```

View Container details

```cmd
docker inspect [OPTIONS] NAME|ID [NAME|ID...]
```

View logs

```cmd
docker logs [OPTIONS] CONTAINER
```

`--follow` , `-f` , Follow log output

For more details, see [https://docs.docker.com/engine/reference/commandline/logs/](https://docs.docker.com/engine/reference/commandline/logs/)


Track from the last 100 lines,

```cmd
docker logs -f --tail 100 CONTAINER
```

or

```cmd
docker logs -f -n 100 CONTAINER
```

You can use `--since` to get logs from a specified time to the present,

For example,

```cmd
docker logs --since 2023-04-13T09:20:00 <container_id>
```

Logs from 10 minutes ago to now

```cmd
docker logs --since 10m CONTAINER
```

Logs from 1 hour ago to now

```cmd
docker logs --since 1h CONTAINER
```

If you want to specify a time and view logs for a specific period,

you can first use `-t` to find out the docker time format,

```cmd
docker logs -t CONTAINER
```

Then you can use `--since` or `--until` to specify the time period,

You must use the docker time format, otherwise it will not work.

Here is a combination to find all logs from 8:10 to 8:30

```cmd
docker logs --since 2023-12-10T8:10:00.346748975Z  --until 2023-12-10T8:30:00.346748975Z  CONTAINER
```

You can also write the logs to a file,

```cmd
docker logs CONTAINER >> access.log
```

If the above command does not work, please change it to the following

```cmd
docker logs CONTAINER >& access.log
```

You can also filter the logs before writing them to a file,

```cmd
docker logs CONTAINER | grep "29/Mar/2022" >> access_tmp.log
```

If the above command does not work, please change it to the following

```cmd
docker logs CONTAINER 2>&1 | grep "29/Mar/2022" >& access_tmp.log
```

Display container resources (CPU, I/O...)

```cmd
docker stats [OPTIONS] [CONTAINER...]
```

You can also add `--no-stream`

```cmd
docker stats --no-stream
```

`--no-stream` Disable streaming stats and only pull the first result.

Note :exclamation: :exclamation: The memory usage obtained here will be smaller than the actual usage,

because this value is the total memory usage minus the cache usage memory.

Related issues can be found at [https://github.com/moby/moby/issues/32253](https://github.com/moby/moby/issues/32253)

```txt
On Linux, the Docker CLI reports memory usage by subtracting cache usage from the total memory usage.
```

For detailed instructions, see [https://docs.docker.com/engine/reference/commandline/stats/](https://docs.docker.com/engine/reference/commandline/stats/)

Also see [https://docs.docker.com/config/containers/runmetrics/](https://docs.docker.com/config/containers/runmetrics/)

View running processes in a container

```CMD
docker top CONTAINER
```

Stop all **processes** in the specified CONTAINER

```cmd
docker pause CONTAINER [CONTAINER...]
```

After executing `docker pause`, you can try to use `docker ps` to check, you will find

it is still running. Let's compare it with `docker stop`. The differences are as follows.

`docker stop`: process level.

`docker pause`: container level.

Resume all **processes** in the specified paused CONTAINER

```cmd
docker unpause CONTAINER [CONTAINER...]
```

docker tag

```cmd
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```

Example

```cmd
docker tag 0e5574283393 twtrubiks/nginx:version1.0
```

For more, see [https://docs.docker.com/engine/reference/commandline/tag/](https://docs.docker.com/engine/reference/commandline/tag/)

Save (backup) an image to a tar file

```cmd
[OPTIONS] IMAGE [IMAGE...]
```

Example

```cmd
docker save busybox > busybox.tar
```

or

```cmd
docker save --output busybox.tar busybox
```

or (you can also back up multiple at once)

```cmd
docker save -o images.tar postgres:9.6 busybox
```

For more, see [https://docs.docker.com/engine/reference/commandline/save/](https://docs.docker.com/engine/reference/commandline/save/)

Load an image

```cmd
docker load [OPTIONS]
```

Example

```cmd
docker load < busybox.tar
```

or

```cmd
docker load -i busybox.tar
```

For more, see [https://docs.docker.com/engine/reference/commandline/load/](https://docs.docker.com/engine/reference/commandline/load/)

Show the history of an image, query each layer of the image

```cmd
docker history [OPTIONS] IMAGE
```

In docker, the concept of layers is very important.

![](https://i.imgur.com/NmImVby.png)

For more, see [https://docs.docker.com/engine/reference/commandline/history/](https://docs.docker.com/engine/reference/commandline/history/)

I just taught you how to save (backup) images and load images.

There is another way, which is to export and import containers.

For docker export container, please refer to [https://docs.docker.com/engine/reference/commandline/export/](https://docs.docker.com/engine/reference/commandline/export/).

For docker import container, please refer to [https://docs.docker.com/engine/reference/commandline/import/](https://docs.docker.com/engine/reference/commandline/import/).

Other commands

Delete all dangling images

```cmd
docker image prune
```

Remove all unused images (not just dangling images)

```cmd
docker image prune -a
```

For more information, see [image_prune](https://docs.docker.com/engine/reference/commandline/image_prune/)

Stop all running Containers

```cmd
docker container stop $(docker ps -q)
```

For more information, see [container_stop](https://docs.docker.com/engine/reference/commandline/container_stop/)

Remove all stopped containers

```cmd
docker container prune
```

For more information, see [container_prune](https://docs.docker.com/engine/reference/commandline/container_prune/)

### ENTRYPOINT

For tutorial instructions, please click [entrypoint-tutorial](https://github.com/twtrubiks/docker-tutorial/tree/master/entrypoint-tutorial)

### Volume

Next, we will introduce Volume. Volume is the mechanism most recommended by Docker for storing persisting data.

Using Volume has the following advantages:

* Volumes are easier to back up or migrate than bind mounts.
* You can manage volumes using Docker CLI commands or the Docker API.
* Volumes work on both Linux and Windows containers.
* Volumes can be more safely shared among multiple containers.
* Volume drivers allow you to store volumes on remote hosts or cloud providers, to encrypt the contents of volumes, or to add other functionality.
* A new volume's contents can be pre-populated by a container.

In the writable layer of a container, using a volume is a better choice because it does not increase the size of the container.

The contents of the volume exist outside the container.

You can also refer to the diagram below

![](https://i.imgur.com/fiIt0kS.png)

For more details, see [https://docs.docker.com/engine/admin/volumes/volumes/](https://docs.docker.com/engine/admin/volumes/volumes/)

View current volumes

```cmd
docker volume ls [OPTIONS]
```

Create a volume

```cmd
docker volume create [OPTIONS] [VOLUME]
```

Delete a volume

```cmd
docker volume rm [OPTIONS] VOLUME [VOLUME...]
```

View volume details

```cmd
docker volume inspect [OPTIONS] VOLUME [VOLUME...]
```

Remove all unused volumes

```cmd
docker volume prune [OPTIONS]
```

You can also create readonly volumes (readonly inside the container)

The `docker-compose.yml` method is as follows,

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

If you want read-write, set it to `rw`.

Volumes are indeed not writable inside the container (only readable)



Use the following command to view Mounts and observe its Mode

```cmd
docker inspect <container ID>
```



You can also create NFS volumes,

The `docker-compose.yml` method is as follows,

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

You can use the following commands to view the settings

```cmd
docker volume ls
docker inspect <volume name>
```



For NFS related articles, please refer to [linux-nfs-server - How to enable NFS Server on ubuntu](https://github.com/twtrubiks/linux-note/tree/master/linux-nfs-server)

### network

I suggest everyone spend some time studying the network in docker, it will be very helpful :smiley:

View the current docker network list

```cmd
docker network ls [OPTIONS]
```

For details, see [https://docs.docker.com/engine/userguide/networking/](https://docs.docker.com/engine/userguide/networking/)

There are three main types of networks in docker: Bridge, Host, and None. The default is Bridge mode.

Example of specifying a network (specify using the `host` network)

```cmd
docker run -it --name busybox --rm --network=host busybox
```

Create a network

```cmd
docker network create [OPTIONS] NETWORK
```

Remove a network

```cmd
docker network rm NETWORK [NETWORK...]
```

Remove all unused networks

```cmd
docker network prune [OPTIONS]
```

View network details

```cmd
docker network inspect [OPTIONS] NETWORK [NETWORK...]
```

Connect a container to a network

```cmd
docker network connect [OPTIONS] NETWORK CONTAINER
```

For more details, see [https://docs.docker.com/engine/reference/commandline/network_connect/](https://docs.docker.com/engine/reference/commandline/network_connect/)

Disconnect a container from a network

```cmd
docker network disconnect [OPTIONS] NETWORK CONTAINER
```

For more details, see [https://docs.docker.com/engine/reference/commandline/network_disconnect/](https://docs.docker.com/engine/reference/commandline/network_disconnect/)

#### User-defined networks

This method is recommended by the official documentation :thumbsup:

Through the built-in DNS server, you can directly use the container name to resolve the IP, without having to use the IP to let containers communicate with each other.

We only need to know the container name to connect to the container.

For more details, see [https://docs.docker.com/engine/userguide/networking/#user-defined-networks](https://docs.docker.com/engine/userguide/networking/#user-defined-networks)

## docker-compose

Next, let's introduce docker-compose. You can refer to the official website [https://docs.docker.com/compose/](https://docs.docker.com/compose/)

![](https://i.imgur.com/YxrrO7t.png)

Compose is a tool for defining and running multi-container Docker applications. Don't understand what I'm saying? :question: :question: :question:

Think about it, a web application usually has a database, and may even have [Redis](https://redis.io/) or [Celery](http://www.celeryproject.org/).

So we need Compose to manage these things, through a `docker-compose.yml` (YML format) file.

For the writing of `docker-compose.yml`, please refer to [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)

You can also directly refer to the official examples [https://docs.docker.com/compose/compose-file/#compose-file-structure-and-examples](https://docs.docker.com/compose/compose-file/#compose-file-structure-and-examples)

Many of Compose's command-line commands are similar to Docker's.

See [https://docs.docker.com/glossary/?term=compose](https://docs.docker.com/glossary/?term=compose)

View current Containers

```cmd
docker-compose ps
```

With `-q`, only the id is displayed

```cmd
docker-compose ps -q
```

Start a Service's Container

```cmd
docker-compose start  [SERVICE...]
```

Stop a Service's Container (does not delete the Container)

```cmd
docker-compose stop [options] [SERVICE...]
```

Restart a Service's Container

```cmd
docker-compose restart [options] [SERVICE...]
```

Builds, (re)creates, starts, and attaches to containers for a service

```cmd
docker-compose up [options] [--scale SERVICE=NUM...] [SERVICE...]
```

Add `-d` to start in the background, which is generally recommended for production environments.

```cmd
docker-compose up -d
```

Then if you have multiple `docker-compose.yml` `docker-compose-dev.yml`,

you can use `-f` to decide which one to execute, for example,

```cmd
docker-compose -f ./docker-compose-dev.yml up -d
```

`-f` `--file FILE` Specify an alternate compose file

(default: `docker-compose.yml`)

The `up` function is very powerful, it is recommended to refer to [https://docs.docker.com/compose/reference/up/](https://docs.docker.com/compose/reference/up/)

If you want to rebuild the image every time, you can add

`--build` (Build images before starting containers.)

```cmd
docker-compose up -d --build
```

docker-compose down

```cmd
docker-compose down [options]
```

The `down` function is also recommended to refer to [https://docs.docker.com/compose/reference/down/](https://docs.docker.com/compose/reference/down/)

For example

```cmd
docker-compose down -v
```

Adding `-v` will also help you remove the volume (remove the volume you set in `docker-compose.yml`)

Execute a command in a specified Service

```cmd
docker-compose run [options] [-v VOLUME...] [-p PORT...] [-e KEY=VAL...] SERVICE [COMMAND] [ARGS...]
[ARGS...]
```

For example

```cmd
docker-compose run web bash
```

Execute the `bash` command in the web Service

See [https://docs.docker.com/compose/reference/run/](https://docs.docker.com/compose/reference/run/)

View Service logs

```cmd
docker-compose logs [options] [SERVICE...]
```

Check if the `docker-compose.yml` format is correct

```cmd
docker-compose config
```

The following command is the same as `docker exec`

```cmd
docker-compose exec
```

Example (enter the bash of the web service)

```cmd
docker-compose exec web bash
```

Display a list of images used in the container

```cmd
docker-compose images
```

Remove service containers

```cmd
docker-compose rm
```

Pushes images to docker hub

```cmd
docker-compose push
```

I don't really understand this command at the moment, you can refer to [https://github.com/docker/compose/issues/4283](https://github.com/docker/compose/issues/4283)

The official website's explanation is not very clear either [https://docs.docker.com/compose/reference/push/](https://docs.docker.com/compose/reference/push/)

### Difference between docker-compose up/down and restart

* [Youtube Tutorial - The difference between docker-compose up/down and restart](https://youtu.be/nX-sbLPz-MU)

Let's first talk about `docker-compose up/down`.

If you modify `docker-compose.yml` or update an image today,

when you want to rebuild docker, there are several ways.

Method one.

First stop the container, execute `docker-compose down` and then execute `docker-compose up`.

Method two.

No need to stop the container, just execute `docker-compose up -d`.

(It will automatically rebuild for you, which is very convenient, no need to shut down the container first)

Conclusion, as long as your `docker-compose.yml` has any changes, you must execute `docker-compose up` for it to take effect.

Now let's talk about `docker-compose restart`.

Please see the official documentation [docker-compose restart](https://docs.docker.com/compose/reference/restart/). If you modify `docker-compose.yml` and then use this command, it will **not** take effect.

However, if you change the code (maybe python code), then this command is effective.

### docker-compose networks

* [Youtube Tutorial - Explanation of docker-compose networks](https://youtu.be/wmV9WfkpyGk)

Here's a little more on the concept of docker-compose networks, because I just happened to use it recently :smile:

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

First, change the version to 3.5, because this version started to have the concept of network names.

Networks (self-defined) have been added to both db and web. The definition is at the end.

`proxy` is the name (similar to the concept of volumes). The `external` option means

whether to refer to an externally defined network (so if it's not found, an error will be reported).

But if you don't add the `external` option, it means it's self-defined, and it will automatically create

the network you defined, named `my_network`.

If you don't define any networks at all, the default is `folder_name_default`.

### Difference between docker-compose ports and expose

In docker-compose, there are two ways to expose container ports:

`ports` and `expose`.

#### ports

```yml
...
ports:
  - "5000:5000"  # Bind container's port 5000 to host's port 5000
  # (HOST:CONTAINER)

  - "5001:5000"  # Bind container's port 5000 to host's port 5001

  - "5000"       # Bind container's port 5000 to a random port on the host (the host will be assigned a random port)
...
```

Random port example,

Here we use the `dpage/pgadmin4` image as a demonstration.

```cmd
docker run -p 80 \
    -e "PGADMIN_DEFAULT_EMAIL=xxxrubiks@gmail.com" \
    -e "PGADMIN_DEFAULT_PASSWORD=SuperSecret" \
    -d dpage/pgadmin4
```

If we execute the above command twice, you will find that the host is assigned two random ports (as shown below),



The host was randomly assigned ports 32768 and 32769.

No matter how we set the ports here, these ports will be exposed to the host and other containers. This is very important :exclamation: :exclamation:

That is to say, if host port 5001 is used, other containers cannot use port 5001.

You may have to change it to port 5002 or something.

#### expose

```yml
...
expose:
  - "4000"
  - "6000"
...
```

`expose` exposes the port to other containers.

The biggest difference between `expose` and `ports` is that `expose` does not expose the port to the host.

So the host can never be accessed, but it can be accessed within containers.

So if your container wants to be accessed from the host today, you must use the `ports` method.

***Difference between ports and expose***

Simply put, `ports` can be accessed by the host and containers; while

`expose` cannot be accessed by the host, only in containers.

## How to connect to a localhost service from within a Docker container

* [Youtube Tutorial - How to connect to a localhost service from within a Docker container](https://youtu.be/KbaHWdVej9U)



Suppose there is a service A on the host, which is run by `docker run`.

And there is another service B on the host, which is run by vscode (not docker).

Now I have a requirement, I want to connect my service A to my service B,

that is, connect from a service inside docker to the host's localhost.

A simpler way is to use this parameter inside docker,

`host.docker.internal:host-gateway`.

Add it to your yml file,

```yml
version: '3.5'
services:

  web:
    ......
    extra_hosts:
      - "host.docker.internal:host-gateway"
......
```

This way, when you are inside the container, you can successfully access the host :smile:

```cmd
curl http://host.docker.internal:8069
```

You can also refer to [docker compose install pgadmin4](https://github.com/twtrubiks/docker-pgadmin4-tutorial#docker-compose-%E5%AE%89%E8%A3%9D-pgadmin4),

Suppose today we don't consider using the network method. If a container `db` is on 5432, and another container is `pgadmin4`,

how can I connect to my host's 5432 through `pgadmin4`? 😵‍💫

The answer is to use `host.docker.internal:host-gateway`.

## Docker Registry

![](https://i.imgur.com/uAXUtxT.png)

You can think of it as a place similar to github, except that it stores docker stuff. Of course,

you can also set it up yourself, but there will be some extra costs, such as network, maintenance, etc. You have to weigh this part yourself :grinning:

Next, I will teach you how to push an image to the Docker Registry :smiley:

* [Youtube Tutorial PART 4 - Tutorial on Pushing Docker Images to Docker Hub](https://youtu.be/dVBKwmqO5e4)

First, log in to [Docker Registry](https://hub.docker.com/) (the registration process is very simple, so I'll skip it)

```cmd
docker login
```

![](https://i.imgur.com/lm9GWTj.png)

For example, first run a busybox container

```cmd
docker run -it busybox
```

Then add a piece of data inside

```cmd
 echo 'text' > data.txt
```

![](https://i.imgur.com/KCeZGQh.png)

Then open another terminal and use `docker ps` to view the current container id

![](https://i.imgur.com/mBIhGBW.png)

Then use commit in the same way as git

docker commit

```cmd
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
```

See [https://docs.docker.com/engine/reference/commandline/commit/](https://docs.docker.com/engine/reference/commandline/commit/)

```cmd
docker commit -m "test" 4fb4ef51e917 twtrubiks/my_busybox
```

`-m` commit message, same as git.

`twtrubiks/my_busybox` is the REPOSITORY we defined.

If you need a tag, you can also add it

```cmd
docker commit -m "test" 4fb4ef51e917 twtrubiks/my_busybox:v1
```

(If no tag is defined, it will show `latest`)

At this time, you can use `docker images` to view

![](https://i.imgur.com/R548ail.png)

Finally push

```cmd
docker push twtrubiks/my_busybox
```

![](https://i.imgur.com/2ExgYpB.png)

Docker is a layered concept, it will only push the layers you added yourself,

so don't worry about the whole image being very large and taking a long time to upload :relaxed:

Finally, you can go to [https://hub.docker.com/](https://hub.docker.com/) to confirm whether it was successful :smile:

![](https://i.imgur.com/W5P3YQL.png)

## Hands-on with Docker, Django, and PostgreSQL

* [Youtube Tutorial PART 2 - Hands-on with Docker, Django, and PostgreSQL](https://youtu.be/aZ6woJ7qekE)

After introducing so much, it's necessary to have some hands-on practice :satisfied:

We use [Django-REST-framework Basic Tutorial - From Scratch DRF-Beginners-Guide](https://github.com/twtrubiks/django-rest-framework-tutorial) as an example

There are a few places that need to be modified.

Change the db connection in `settings.py` to [PostgreSQL](https://www.postgresql.org/)

```python
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

It is also recommended to change `ALLOWED_HOSTS = []` to `ALLOWED_HOSTS = ['*']`
(This is just for convenience, it is not used this way in practice)

Next are two very important files, `Dockerfile` and `docker-compose.yml`

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

For details, see [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)

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

For details, see [https://docs.docker.com/compose/compose-file/#compose-file-structure-and-examples](https://docs.docker.com/compose/compose-file/#compose-file-structure-and-examples)

Friendly reminder 1 :heart:

Some people may ask why I use `0.0.0.0` instead of `127.0.0.1` :question: :question:

```cmd
python manage.py runserver 0.0.0.0:8000
```

`127.0.0.1` does not represent the real **localhost**. We often think of it as localhost because our computer's `host` file is set up for us by default :smirk:

For a detailed `host` setting tutorial, please refer to [hosts-configuration file and query intranet ip](https://github.com/twtrubiks/docker-django-nginx-uswgi-postgres-tutorial#hosts-設定檔-以及-查詢內網-ip).

`0.0.0.0` is the real representation of **the current (local) machine on the network** :pencil2:

If you want to understand more deeply, you can google the difference between `127.0.0.1` and `0.0.0.0` :smile:

Friendly reminder 2 :heart:

I want to specifically mention the `depends_on` parameter here.

For details, see [https://docs.docker.com/compose/compose-file/#depends_on](https://docs.docker.com/compose/compose-file/#depends_on).

There is a very important description in the link above

****depends_on does not wait for db and redis to be "ready" before starting web - only until they have been started. If you need to wait for a service to be ready, see Controlling startup order for more on this problem and strategies for solving it.****

Taking my [docker-compose.yml](https://github.com/twtrubiks/docker-tutorial/blob/master/docker-compose.yml) as an example, although the startup order is db -> web, **it will not wait for db to be ready before starting web**.

That is to say, it is still possible that **web starts before db is ready**, in which case you need to restart the web service, otherwise it will not be able to connect to the db :sob:

If you really want to control the startup order, please refer to [Controlling startup order](https://docs.docker.com/compose/startup-order/).

Friendly reminder 3 :heart:

`docker-compose.yml` can actually be done with `docker run`. For example, in this example, if you use

`docker run` to write it, it will look like this.

First, to allow the containers to communicate with each other, we first create a network (User-defined networks).

```cmd
docker network create my_network
```

db container

```cmd
docker run --name db -v pgdata:/var/lib/postgresql/data/ -p 5432:5432 --network=my_network -e POSTGRES_PASSWORD=password123 postgres
```

Next, go to the api folder to build the image

```cmd
docker build --tag web_image .
```

`--tag , -t` , tag this image as `web_image`

It can also be

```cmd
docker build -t user/repo:tag .
```

web container

```cmd
docker run --name web -v api_data:/docker_api -p 8000:8000 --network=my_network --restart always web_image python manage.py runserver 0.0.0.0:8000
```

The above is actually the same as `docker-compose.yml` :open_mouth:

After setting it up, we can start it

```cmd
docker-compose up
```

Next you will see a similar screen

![](https://i.imgur.com/GJWIgEP.png)

![](https://i.imgur.com/dVRRyrM.png)

If you see a similar screen

![](https://i.imgur.com/cCEmVBq.png)

It means that while the database is still being created, your web (Django) is trying to connect to it.

This causes the connection to fail. At this point, we can terminate it (press Ctrl+C).

Then restart with `docker-compose up`.

We have successfully started (and the db connection is normal)

![](https://i.imgur.com/iuCxLMY.png)

:exclamation: [commit](https://github.com/twtrubiks/docker-tutorial/commit/398cb2fc375af8926cfe1eeabda33da018437897) has been updated to automatically migrate :exclamation:

But if you look closely at the picture above, you will see that it says you haven't migrated yet.

Next, we open another cmd to enter the web service.

Enter the service through the command just introduced

```cmd
docker ps
docker exec -it <Container ID> bash
```

Or you can enter from [Kitematic](https://kitematic.com/).

After entering, we can start migrating

```cmd
python manage.py makemigrations musics
python manage.py migrate
```

![](https://i.imgur.com/zMmZKuL.png)

Create a superuser at the same time

```cmd
python manage.py createsuperuser
```

:exclamation: [commit](https://github.com/twtrubiks/docker-tutorial/commit/398cb2fc375af8926cfe1eeabda33da018437897) has been updated to automatically create a superuser :exclamation:

Please refer to the environment in [docker-compose.yml](https://github.com/twtrubiks/docker-tutorial/blob/master/docker-compose.yml) (as follows),

`DJANGO_SUPERUSER_USERNAME` `DJANGO_SUPERUSER_PASSWORD` `DJANGO_SUPERUSER_EMAIL`

Next, we can try to use the GUI to connect to the db.

Because we are using [PostgreSQL](https://www.postgresql.org/), we can connect through [pgadmin](https://www.pgadmin.org/).

![](https://i.imgur.com/2Hdt7wU.png)

The things we just migrated do exist

![](https://i.imgur.com/PEUfGRy.png)

We don't need to restart

We can happily go to browse [http://127.0.0.1:8000/api/music/](http://127.0.0.1:8000/api/music/)

Everyone will definitely see a familiar screen

![](https://i.imgur.com/pzqZbdz.png)

Then log in with the account and password you just set

![](https://i.imgur.com/l6RZXsQ.png)

![](https://i.imgur.com/xeJtRJc.png)

The entire environment above is in Docker :open_mouth:

If we press Ctrl+C to exit and restart with `docker-compose up` again,

this time it will not tell you that you have not migrated.

![](https://i.imgur.com/zIBkL3t.png)

## Other GUI tools for managing Docker

* [Youtube Tutorial PART 3 - Docker Basic Tutorial - Managing Docker with Portainer](https://youtu.be/VZjHmBcEcew)

In addition to [Kitematic](https://kitematic.com/), there are other good ones to recommend to everyone.

This time I want to introduce [portainer](https://github.com/portainer/portainer), which is powerful and easy to use :fire:

In fact, if you look at the github of [Kitematic](https://github.com/docker/kitematic) and [portainer](https://github.com/portainer/portainer),

you will find that [portainer](https://github.com/portainer/portainer) seems to be more maintained :smile:

And after I used [portainer](https://github.com/portainer/portainer), I really recommend it :smiley:

For installation methods, see [https://portainer.io/install.html](https://portainer.io/install.html)

```cmd
docker volume create portainer_data
docker run --name=portainer -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```

`-d` and `-p` were introduced in the previous `docker run` section. `--name` is just for naming.

`Note 1`: The `-v /var/run/docker.sock:/var/run/docker.sock` option is available on Linux environments only.

`Note 2`: The `-v portainer_data:/data portainer/portainer` option will persist Portainer data in `portainer_data` on the host where Portainer is running. You can specify another location on your filesystem.

(After it is created, just operate it as a container)

Then check [http://localhost:9000/](http://localhost:9000/) and you will see the picture below

Then set the account and password

![](https://i.imgur.com/exdMf2p.png)

Choose Local or Remote

![](https://i.imgur.com/3mkNMxF.png)

The interface is really nice, and the information is very rich :heart_eyes:

![](https://i.imgur.com/ynoqTZT.png)

Trust me, after you use it, you will silently sideline [Kitematic](https://kitematic.com/) :smirk:

## Check port usage status

This is recommended for everyone. Sometimes you will encounter a port being occupied. It is more convenient to check with commands.

Linux

Install net-tools

```cmd
sudo apt install net-tools
```

Check who is occupying port 80

```cmd
sudo netstat -lnp | grep -w ':80'
```

`-l`, `--listening` display listening server sockets.

`-n`, `--numeric` don't resolve names.

`-p`, `--programs` display PID/Program name for sockets.

You can also use `lsof`

```cmd
sudo lsof -i :80
```

`-i` select IPv[46] files.

Windows

Check the usage status of all ports

```cmd
netstat -ano
```

Check the usage status of a specified port, for example, to check the usage status of port 5432

```cmd
netstat -aon|findstr "5432"
```

Check the process corresponding to the PID

```cmd
tasklist|findstr "2016"
```

Stop the process with PID 6093

```cmd
taskkill /f /PID 6093
```

Stop the vscode.exe process

```cmd
taskkill /f /t /im vscode.exe
```

MAC

Stop all processes on port 8000

```cmd
sudo lsof -t -i tcp:8000 | xargs kill -9
```

Check the usage status of a specified port, for example, to check the usage status of port 5432

```cmd
lsof -i tcp:5432
```

## Automatically start docker in Linux

[Automatically start docker in Linux](https://github.com/twtrubiks/docker-tutorial/tree/master/docker-auto-run-linux)

## How to clear Docker container log

[Youtube Tutorial - How to clear Docker container log](https://youtu.be/SiG0tmwhqqg)

Docker container logs are all in `/var/lib/docker/containers`

(provided you use the official installation method, [Youtube Tutorial - How to install docker on Ubuntu(Linux)](https://youtu.be/eS_HMBC_RaA))

If you installed docker using `snap`, the path will be `/var/snap/docker/common/var-lib-docker/containers`.



The log is a json file



If you don't manage it, the log will get bigger and bigger :scream:

This log will be cleared in the following situations: if you modify `docker-compose.yml` or

you execute `docker-compose down`, these logs will be cleared (because the containers are recreated).

(`docker-compose stop` is not affected, because it is just paused)

It is recommended to refer to [The difference between docker-compose up/down and restart](https://github.com/twtrubiks/docker-tutorial#docker-compose-updown-%E5%92%8C-restart-%E7%9A%84%E5%B7%AE%E7%95%B0)

Then you might ask me, what if I don't modify `docker-compose.yml` or execute

`docker-compose down` for a long time :sob: (because the log may grow very fast)

Here is a method for everyone, use the truncate command in linux (see [Linux command tutorial - truncate](https://github.com/twtrubiks/linux-note#truncate))

Delete all container logs

```cmd
truncate -s 0 /var/lib/docker/containers/*/*-json.log
```

But sometimes you only want to target (clear) the logs of a certain container. At this time, you can use the following command

```cmd
truncate -s 0 $(docker inspect --format='{{.LogPath}}' <container_name_or_id>)
```

(please replace `<container_name_or_id>` with your own container's id or name)

The `docker inspect --format='{{.LogPath}}' <container_name_or_id>` part just displays the path.



But there is a better way, directly through the JSON File logging driver in docker.

## JSON File logging driver

[Youtube Tutorial - JSON File logging driver in Docker (container log)](https://youtu.be/wb9bONgnFn4)

In docker, the json-file driver is the default logging driver. For details, see [json-file](https://docs.docker.com/config/containers/logging/json-file/)

So we can use this setting to limit the size of the log,

```yaml
logging:
  driver: "json-file"
  options:
    max-file: "1"    # default is 1
    max-size: "200m" # default is -1, which means no limit
```

After setting it up, restart docker-compose. You can use the following command to check if it has taken effect

```cmd
docker inspect --format '{{.HostConfig.LogConfig}}' CONTAINER
```



After setting this up, you don't have to worry about the container log taking up a lot of space anymore :smile:

## Health Check

* [Youtube Tutorial - docker tutorial Health Check](https://youtu.be/QffnQZgvmwE)

Let's look at an example directly [docker-compose.yml](https://github.com/twtrubiks/odoo-docker-tutorial/blob/15.0/docker-compose.yml)

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

When executed, you will find an additional `health: starting` as shown below,



After (every) 10 seconds (`interval: 10s`), if it starts successfully, it will become `(healthy)` as shown below,



After (every) 10 seconds, if it fails many times in a row (`retries: 5`),

it will display `(unhealthy)` as shown below,



Docker's Health Check will return you a number,

0 means success, container is healthy

1 means failure, if it fails more than the specified number of times (`retries: 5`), the container is unhealthy

As for `condition: service_healthy` under `depends_on`, it means that the check must pass before

it will start. See [Control startup](https://docs.docker.com/compose/startup-order/#control-startup). There are three types,

`service_started` If not specified, this is the one.

`service_healthy`

`service_completed_successfully`

## Afterword:

I only recently started learning Docker, so I'm still a beginner. If I've said anything wrong, please let me know and I'll correct it :grinning:

There's a lot you can do with Docker. For further reference:

* [Hands-on Docker + Jenkins + Django + Postgres 📝](https://github.com/twtrubiks/docker-jenkins-django-tutorial) - Integrating Jenkins

* [Docker + Django + Nginx + uWSGI + Postgres Basic Tutorial - From Scratch](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial)

* [Hands-on Docker + Django + Nginx + uWSGI + Postgres - Load Balance 📝](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-load-balance-tutorial)

You can also play with **Docker Swarm** (distributed system) :satisfied:

* [Docker Swarm Basic Tutorial - From Scratch Docker-Swarm-Beginners-Guide📝](https://github.com/twtrubiks/docker-swarm-tutorial)

Finally, I hope that in the process of learning Docker, when you encounter something you don't understand, you can look for information and understand it,
and at the same time supplement some of the knowledge you were lacking before.

## Execution Environment

* Mac
* Python 3.8.12
* windows 10

## Reference

* [https://docs.docker.com/](https://docs.docker.com/)
* [portainer](https://github.com/portainer/portainer)

## Donation

The articles are all original after my own research and internalization. If it has helped you and you want to encourage me, please buy me a cup of coffee :laughing:

ECPAY (no membership registration required)

![alt tag](https://payment.ecpay.com.tw/Upload/QRCode/201906/QRCode_672351b8-5ab3-42dd-9c7c-c24c3e6a10a0.png)

[Sponsor Payment](http://bit.ly/2F7Jrha)

O'Pay (membership registration required)



[Sponsor Payment](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## Sponsor List

[Sponsor List](https://github.com/twtrubiks/Thank-you-for-donate)

## License

MIT license
