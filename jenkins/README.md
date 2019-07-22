这个部分只是介绍我安装tomcat，以及学习的过程

# 目录
> * [1.jenkins安装](#main-chapter-1)

# 1. jenkins安装
## 1.1 创建目录，添加读写权限
```
mkdir -p /var/jenkins_node     #创建目录
chmod 777 /var/jenkins_node    #赋予所有用户拥有这个目录的可读、可写、可执行权限
chown 1000:1000 /var/jenkins_node #将目录的拥有者改为uid为1000的用户(jenkins用户的uid是1000)
```

## 1.2 拉取jenkins镜像：docker pull jenkins。或者拉取并运行
```
docker run -d --name xiao_jenkins -p 8080:8080 -p 50000:50000 --privileged -v /var/jenkins_node:/var/jenkins_home jenkins
```

## 1.3 打开浏览器http://{your_ip}:8080，运行

## 1.4 获取admin密码
```
方法1：（宿主机执行）
cat /var/jenkins_node/secrets/initialAdminPassword
方法2：（宿主机执行）
docker logs xiao_jenkins
方法3：（容器内部执行）
cat /var/jenkins_home/secrets/initialAdminPassword
```

## 1.5 选择Install suggested plugins

