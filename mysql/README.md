# 目录
> * [1.MySQL安装](#main-chapter-1)
> * [2.MySQL配置](#main-chapter-2)

# 1. MySQL安装
## 1.1 添加yum源
```
wget http://repo.mysql.com//mysql57-community-release-el7-7.noarch.rpm
yum localinstall -y mysql57-community-release-el7-7.noarch.rpm
```

## 1.2 安装启动MySQL
```
yum install -y mysql-community-server
service mysqld start
```


# 2. MySQL配置
## 2.1 查看默认密码
```
grep -n password /var/log/mysqld.log
```

## 2.2 修改密码，允许远程访问
```
登录
mysql -u root -p

SET PASSWORD = PASSWORD('Derek@12345');
use mysql;
update user set Host='%' where User='root';
flush privileges;
```

