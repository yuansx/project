这个部分只是介绍我安装shadowsocks，以及学习的过程

# 目录
> * [1.shadowsocks服务端]

## 1. shadowsocks服务端
### 1.1 安装python和pip
```
yum install -y python36
yum install -y python3-pip
```

### 1.2 更新pip
```
pip install --upgrade pip
```

### 1.3 安装shadowsocks
```
pip install -y shadowsocks
```

### 1.4 配置shadowsocks.json
```
{
    "server": "0.0.0.0",
    "server_port": "7878",
    "local_address": "127.0.0.1",
    "local_port": "1080",
    "password": "Xiao12345",
    "timeout": "300",
    "method": "aes-256-cfb",
    "fast_open": false
}
```

### 1.5 启动
```
nohup ssserver -c /etc/shadowsocks.json 2>&1 /dev/null &
```
