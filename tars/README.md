tars是腾讯开源的高性能RPC框架

# 章节
> * [1.环境搭建](#main-chapter-1)
> * [2.使用介绍](#main-chapter-2)

# 1. 环境搭建 <a id="main-chapter-1"></a>
开源代码下载地址
```
https://github.com/TarsCloud/Tars
```
安装里面的Install.zh.md一步步安装即可

我这里已经安装完成，并做了个镜像，因此这里只需要执行
```
docker run --name tars --privileged -p 3333:3000 -tid yuansx/tars:v2.0 /usr/sbin/init
```
因为web页面使用3000端口，这里映射出来，方便打开页面

# 2. 使用介绍 <a id="main-chapter-2"></a>
执行
```
docker exec -ti tars bash
```
进入tars环境，然后执行
```
bash /usr/sbin/tars_init.sh
```
配置设置好数据库，再执行
```
bash /usr/local/app/tars/tars_install.sh
```
拉起tars基础框架的进程

至此完成tars基础的服务安装，后面跟着install.zh.md文档的4.4节部署其他服务即可
