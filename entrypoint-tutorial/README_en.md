# ENTRYPOINT

[中文版](README.md)

The `ENTRYPOINT` and `CMD` instructions in Docker are very similar, but a bit different.

Here's a simple explanation for everyone :smile:

## CMD

Example Dockerfile as follows:

```Dockerfile
FROM alpine
CMD [ "ls"]
#ENTRYPOINT [ "ls" ]
```

build `docker build -t demo .`

execute `docker run --rm demo`

There's no problem with the usage above.

But what if today I want to change the command (I want to list the files in `dev` directly)?

Change the command as follows:

`docker run --rm demo dev`

```cmd
docker: Error response from daemon: failed to create shim: OCI runtime create failed: container_linux.go:380: starting container process caused: exec: "dev": executable file not found in $PATH: unknown.
```

You'll find an error because it only executed `dev`, not `ls dev`.

You must make the following adjustment (you need to write the complete command again):

`docker run --rm demo ls dev`

Now it's normal, and it successfully displays the contents of `dev`.

But this is a bit troublesome in practice, because what if the command is very long? :question:

So now we have `ENTRYPOINT` to introduce :smile:

## ENTRYPOINT

Example Dockerfile as follows:

```Dockerfile
FROM alpine
# CMD [ "ls"]
ENTRYPOINT [ "ls" ]
```

build `docker build -t demo .`

execute `docker run --rm demo`

The above are all the same.

If I want to change the command (I want to list the files in `dev` directly),

change the command as follows:

`docker run --rm demo dev`

It successfully displays the contents of `dev`.

(The previous `CMD` example would have resulted in an error, but this problem can be avoided with `ENTRYPOINT`.)

This is because it's the concept of appending the command.

You can simply think of it as `ENTRYPOINT`(ls) + `CMD`(dev).

You can also achieve more complex variations through bash.

See [docker-entrypoint.sh](https://github.com/twtrubiks/docker-tutorial/blob/master/api/docker-entrypoint.sh)
