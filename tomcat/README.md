这个部分只是介绍我安装tomcat，以及学习的过程

# 目录
> * [1.tomcat安装](#main-chapter-1)


# 1. tomcat安装
## 1.1 旧的jdk卸载
```
yum list installed | grep java
yum remove -y java-1.6.0-openjdk*
yum remove -y tzdata-java.noarch
```

## 1.2 安装jdk
```
yum search java | grep jdk
yum install -y java-1.8.0-openjdk java-1.8.0-openjdk
```
