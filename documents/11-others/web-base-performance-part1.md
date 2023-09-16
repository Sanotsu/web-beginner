前端 vue 项目的压缩和 nginx 部署

只讲有关压缩这部分，就有效提高前端的性能。

**一、在 vite 打包时就配置好压缩**

**二、在 nginx 部署时不用 gzip 而是 Brotli(以下简称 br)**

1、下载 br 源码和 nginx 对应版本源码

下载 br 源码并更新

```shell
# 下载的位置看个人，后面注意替换到自己实际的路劲
cd /usr/src
# 下载brotli
git clone https://github.com/google/ngx_brotli.git
# 更新brotli
cd ngx_brotli
git submodule update --init
```

下载与服务器中同样 nginx 版本的源码(需要 1.9.11 以上，因为在此之后才支持动态模块)

```shell
# 获取当前nginx版本
nginx -V
# 获取nginx源码
# 去官网下: http://nginx.org/en/download.html

# 解压到某个位置
tar -xvf nginx-1.18.0.tar.gz
```

2、编译动态模块

```shell
# 进入解压后的nginx安装包目录，配置configure，然后用make modules
cd nginx-1.18.0
./configure --with-compat --add-dynamic-module=/usr/src/ngx_brotli
make modules
```

在`./configure ……`这一步可能会看到一些错误，例如:

```
……
adding module in /usr/local/src/ngx_brotli
 + ngx_brotli was configured
checking for PCRE library ... not found
checking for PCRE library in /usr/local/ ... not found
checking for PCRE library in /usr/include/pcre/ ... not found
checking for PCRE library in /usr/pkg/ ... not found
checking for PCRE library in /opt/local/ ... not found

./configure: error: the HTTP rewrite module requires the PCRE library.
You can either disable the module by using --without-http_rewrite_module
option, or install the PCRE library into the system, or build the PCRE library
statically from the source with nginx by using --with-pcre=<path> option.
```

像我这也用不到`http_rewrite_module`模块就直接加上者选项就好:

```shell
./configure --with-compat --add-dynamic-module=/usr/local/src/ngx_brotli --without-http_rewrite_module
```

否则的话，你就可能需要手动想办法加上这些缺少的 PCRE libray 路径。

等 make 运行完成后，查看编译好的模块

```shell
ls objs/*.so
# 正常会输出 objs/ngx_http_brotli_filter_module.so  objs/ngx_http_brotli_static_module.so

# 将编译好的模块文件复制到nginx动态模块加载目录
cp objs/{ngx_http_brotli_filter_module.so,ngx_http_brotli_static_module.so} /usr/share/nginx/modules
```

注意：`/usr/share/nginx/modules`是我这 1.18.0 版本的 nginx 的模块默认路径，请确认自己 nginx 版本的位置是否一样、或者有异动配置。此外，像我为了和其他模块区分，会刻意创建一个文件夹存放自行编译的模块，所以放置的位置类似`/usr/share/nginx/modules/dynamic_modules`。

3、注册 Brotli 模块

像我这 nginx 的默认配置中有指定模块使用配置的位置。

打开`/etc/nginx/nginx.conf`配置文件，一般在最上面能看到类似一行代码:

```conf
……
include /etc/nginx/modules-enabled/*.conf;
……
```

所以刚刚把动态模块放到位置之后，现在要注册，  
我是打看这个`/etc/nginx/modules-enabled/`文件夹，  
新建一个`self-dynamic-modules.conf`配置文件，  
然后在里面加入动态模块的地址(文件名称随意，内容为 load_module 指定模块即可):

```conf
# Brotli模块
load_module modules/dynamic_modules/ngx_http_brotli_filter_module.so;
load_module modules/dynamic_modules/ngx_http_brotli_static_module.so;
```

**注意**，这里面的路径`modules/dynamic_modules/`，  
“modules”就是 nginx 默认的路径，就是上面的`/usr/share/nginx/modules/`，  
“dynamic_modules/”是我为了区分自己动态编译的模块而单独建的一层文件夹。

4、启用 Brotli 压缩

最好是先关闭 nginx 服务，然后打开 nginx 的默认配置开启 br。

我这是`/etc/nginx/nginx.conf`文件，在`http {}`选项中加入如下内容（br 的配置可自行学习）:

```cong
http {
    ……

    # 启用 brotli 压缩
	brotli on;
    brotli_comp_level 6;
    brotli_buffers 16 8k;
    brotli_min_length 20;
    brotli_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript application/javascript image/svg+xml;

    ……

}

```

还有一点特别注意: **Brotli 压缩只能在 https 中生效**，所以自定的 server 配置需要启用 ssl，当然也需要配置 key。

例如我这个示例:

```conf
server {
        server_name http_host;
        listen 8089 ssl; # 以前是单独一行 ssl on; 快弃用了直接在listen后面加 ssl 就好了
        ssl_certificate     /etc/nginx/crtdir/server.cer;
        ssl_certificate_key /etc/nginx/crtdir/server.key;
        ……
}
```

重新启动 nginx，如果没有报错(有报错肯定要先解决)，再访问部署的页面，可以看到指定请求的 Response Headers 中`Content-Encoding: br`信息，类似：

```
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 24 Aug 2023 01:50:06 GMT
Content-Type: text/html
Last-Modified: Thu, 17 Feb 2022 06:38:35 GMT
Transfer-Encoding: chunked
Connection: keep-alive
ETag: W/"620ded6b-3f9"
X-XSS-Protection: 1; mode=block
Cache-Control: no-cache
Pragma: no-cache
Content-Encoding: br # 就这里
```

5、补充：nginx 中多个压缩方式共存

这个也是我在对比不同算法的压缩效率看到的，我 nginx 可以配置多种压缩，然后在 server 配置时指定某一种就好了。

在 ngnix 默认配置`/etc/nginx/nginx.conf`中配置 http 选项多种压缩方式:

```conf
http {
    ##
	# Gzip Settings
	##
	gzip_proxied any;
	gzip_comp_level 6;
	gzip_buffers 16 8k;
	gzip_http_version 1.1;
	gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    ##
	# Brotli Settings
	##
    brotli_comp_level 6;
    brotli_buffers 16 8k;
    brotli_min_length 20;
    brotli_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript application/javascript image/svg+xml;
}
```

注意，这里就没有启用的配置，而是在 server 选项配置，比如我的自定配置`my.conf`中:

```
server {
	server_name demo_server1;
    listen 8089 ssl;
    ssl_certificate     /etc/nginx/crtdir/server.cer;
    ssl_certificate_key /etc/nginx/crtdir/server.key;
    brotli on;
    ……
}

server {
	listen 8088;
	server_name demo_server2;
    gzip on;
    ……
}
```

8089 端口的用的就是 br，8088 的就是 gzip。

**三：nginx 启用 http2**

同样在压缩上面，还可以讲 nginx 配置 http2,这样还能进一步减少请求的资源大小。事实上，http2 相较于 http3 使用上还是需要更加广泛(理论小于实践是不是就这个说法)，对应 http1.1 的提升还是比较明显的。

nginx 启用 http2 也很简单，上面的 server 配置看到了吧，把 listen 再加一个选项即可:

```conf
# 更高效率的压缩：br + h2
server {
	server_name demo_server1;
    listen 8089 ssl http2; # 加http2
    ssl_certificate     /etc/nginx/crtdir/server.cer;
    ssl_certificate_key /etc/nginx/crtdir/server.key;
    brotli on; # 启用br
    ……
}
```

简单的效果:

![gzip和br在http1.1和http2的不同表现](./pictures-others/nginx-config/gzip和br在http1.1和http2的不同表现.png)
