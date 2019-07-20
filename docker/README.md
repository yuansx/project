这个部分只是介绍我安装docker，以及学习的过程

# 目录
> * [1.docker安装](#main-chapter-1)

# 1. docker安装 <a id="main-chapter-1"></a>
## 1.1 Docker 安装官网地址
    https://docs.docker.com/install/linux/docker-ce/centos/

## 1.2 安装基本软件，添加docker yum源
```
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

## 1.3 安装最新版的docker ce和containerd
```
yum install -y docker-ce docker-ce-cli containerd.io
```

## 1.4 启动docker
```
systemctl start docker
systemctl enable docker
```
