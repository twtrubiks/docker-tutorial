# 介紹 yaml anchors

這個功能不是 docker 的, 是 YAML 的功能, 叫做 YAML anchors,

簡單說明, 透過 yaml anchors, 可以將重複的部份放在一起, 就不用寫很多次了,

使用範例如下 [docker-compose.yml](docker-compose.yml)

```yml
x-config: &x-config
  image: nginx:1.24.0
  restart: always
  logging:
    driver: "json-file"
    options:
      max-file: "1"
      max-size: "50m"
  volumes:
      - static:/my_tmp
      - ./local_static:/local_static

services:

  nginx1:
    <<: *x-config
    container_name: nginx1
    ports:
      - "81:80"

  nginx2:
    <<: *x-config
    container_name: nginx2
    # 假如有寫任何一行 volumes, 會完全附蓋掉 x-config 的 volumes
    volumes:
      - static_nginx_2:/tmp2
    ports:
      - "82:80"

  nginx3:
    <<: *x-config
    container_name: nginx3
    volumes:
      - static_nginx_3:/tmp3
      - static:/my_tmp  # 要再自己手動加上去
      - ./local_static:/local_static # 要再自己手動加上去
    ports:
      - "83:80"


volumes:
  static:
  static_nginx_2:
  static_nginx_3:
```

nginx1, nginx2, nginx3 有共用的 `image` `restart` `logging` 以及 `volumes`

這樣就可以不用重複寫很多次了.

但是 `volumes` 這邊要注意一下, 只要你有覆蓋任何一個參數,

像是 nginx2 底下的 volume, x-config 中的共用的部份在這個容器下都會生效,

也就是只生效 `- static_nginx_2:/tmp2`.

所以, 只要你有覆寫, 請改寫成 nginx3 這樣, 手動自己再把共用的部份加上去.
