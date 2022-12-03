登录本地仓库：  
docker login 192.168.1.1:5001

推送到本地仓库：  
docker push 192.168.1.1:5001/i2dsp/emqx:4.3.10

修改镜像标签：  
`docker tag IMAGEID(镜像id) REPOSITORY:TAG（仓库：标签）`  
docker tag fa97991dd3e2 192.168.1.1:5001/i2dsp/emqx :4.3.10

下载镜像：  
docker pull 192.168.1.1:5001/i2dsp/elasticsearch:7.16.0

重启/关闭/启动 docker：  
sudo service docker restart/stop/start

守护进程重启：  
sudo systemctl daemon-reload

daemon.json 的作用

1. 如何配置 registry 私库相关的参数

涉及以下 2 个参数：  
 "insecure-registries": [], #这个私库的服务地址  
 "registry-mirrors": [], #私库加速器

2. 配置示例：

```
{
    "registry-mirrors": [
       "https://d8b3zdiw.mirror.aliyuncs.com"
    ],

    "insecure-registries": [
       "https://ower.site.com"
    ]
}
```

3. 创建并修改完 daemon.json 文件后，需要让这个文件生效  
   a.修改完成后 reload 配置文件  
   sudo systemctl daemon-reload  
   b.重启 docker 服务  
   sudo systemctl restartdocker.service  
   c.查看状态  
   sudo systemctl status docker -l  
   d.查看服务  
   sudo docker info


查看本地镜像：  
docker images

删除指定镜像：  
docker rmi [OPTIONS] IMAGE [IMAGE...]  
https://docs.docker.com/engine/reference/commandline/rmi/

删除指定容器：  
docker rm [OPTIONS] CONTAINER [CONTAINER...]  
https://docs.docker.com/engine/reference/commandline/rm/

卸载docker-cli（同样安装方式下）：
sudo apt-get remove docker-ce docker-ce-cli