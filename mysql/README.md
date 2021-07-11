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
yum install -y mariabd-devel
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
# 3. 密码死活不正确
## 3.1 无密码方式一登陆
修改my.cnf
```
[mysqld]
skip-grant-tables
```
重启mysqld即可

## 3.2 无密码登陆方式二登陆
使用下面方式启动mysqld服务
```
mysqld --console --skip-grant-tables --shared-memory
```

## 3.3 修改密码
```
mysql
update mysql.user set authentication_string='' where user = 'root';
去掉skip-grant-tables重启mysql，然后空字符串密码方式登陆
mysql -uroot -p
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Derek@12345';
mysql很变态把password字段变成 authentication_string，然后密码策略也严谨了show variables like 'validate_password%';查看密码策略
```

# 4. 创建远程用户
```
CREATE USER 'root'@'%' IDENTIFIED BY 'Derek@12345';
GRANT ALL PRIVILIEGES ON *.* TO 'root'@'%';
CREATE USER 'read'@'%' IDENFIFIED BY 'Read@12345';
GRANT SELECT ON test.test TO 'read'@'%';
```
