# 介紹 YAML Anchors

* [Youtube Tutorial - YAML Anchors (& * <<) 與 Docker Compose 實戰教學：告別重複設定！(等待新增)](x)

這個功能不是 docker 的, 是 YAML 的功能, 叫做 YAML Anchors,

先說結論, 透過 YAML Anchors, 可以將重複的部份放在一起, 就不用寫很多次.

看一下定義, 分別是

YAML Anchors (&) 錨點

Aliases (*) 別名

Merge Key (<<) 合併鍵

使用範例如下 [docker-compose.yml](docker-compose.yml)

先說明一下為什麼都要用 `x-` 開頭,

`x-` 前綴是一種慣例 (Convention), 而且 Docker Compose 會忽略 `x-` 頂層鍵,

不會把它當作 services, volumes, networks 這類的東西,

簡單說, 這樣使用, 就可以不影響 Docker Compose 的正常解析.

```yml
# &x-config 定義了一個錨點

# 這邊只是要說明 頂層的 Key 是可以任意定義的, 不需要和你的 Anchors 同名
# x-config: &x-config
# or
x-config-key: &x-config
  # key: value
  image: nginx
  restart: always
  logging:
    driver: "json-file"
    options:
      max-file: "1"
      max-size: "50m"
  # key: 序列 (Sequence) 或陣列 (Array)
  volumes:
      - static:/my_tmp
      - ./local_static:/local_static

services:

  nginx1:
    # *x-config 創建了一個指向該錨點內容的別名
    # << 合併的是映射 (mapping, 即 key-value pairs)，但合併過程中如果遇到相同的 key，預設行為是「覆蓋」
    <<: *x-config
    container_name: nginx1
    ports:
      - "81:80"

  nginx2:
    <<: *x-config
    container_name: nginx2
    # 因為 volumes 的 value 是一個序列 (Sequence) 或陣列 (Array)
    # 且預設行為是「覆蓋」, 所以會整個覆蓋掉 x-config 中相同的 key (volumes)
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

但是 `volumes` 這邊要注意一下, 只要你在本地服務中定義了與錨點中相同的 key（例如 volumes 這個 key）,

像是 nginx2 底下的 `volumes`, `x-config` 中的共用的部份在這個容器下就**不會生效**，因為整個 `volumes` 列表被本地定義覆蓋了,

也就是只生效 `- static_nginx_2:/tmp2`.

所以, 只要你有相同的 key (像這個情境是 volumes), 請改寫成 nginx3 這樣, 手動自己再把共用的部份加上去.
