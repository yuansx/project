目录|功能
----|----
test_file | 测试程序
alien     | 飞船打火星人小游戏

# 1. 安装常用库
```
yum install -y python36
yum install -y python3-devel
pip3 install django
pip3 install requests
pip3 install pillow
pip3 install mysqlclient
pip3 install pymysql
```

# 2. django使用
## 2.1 常用命令
```
django-admin startproject helloworld
cd helloworld
python3 manage.py runserver [ip:port]
python3 manage.py startapp test
python3 manage.py migrate
python3 manage.py makemigration hello
python3 manage.py createsuperuser
```

