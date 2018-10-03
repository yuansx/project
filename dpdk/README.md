这个部分只是介绍我安装dpdk，以及学习的过程

#目录
> * [1.环境准备](#main-chapter-1)
> * [2.编译安装](#main-chapter-2)

# 1. 环境准备 <a id="main-chapter-1"></a>
## 1.1 操作系统安装
    使用virtualBox安装CentOS-7-x86_64-Minimal-1804.iso
    内存2G，CPU 2核，磁盘80G，3张网卡(nat+2host)

## 1.2 基本软件安装及网络配置
### 1.2.1 简单把网络搞通，能够上网
修改/etc/sysconfig/network-scripts/ifcfg-enp0s3
把
```
ONBOOT=no
```
修改为
```
ONBOOT=yes
```
修改/etc/sysconfig/network-scripts/ifcfg-enp0s8后，内容如下：
```
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static
IPADDR=192.168.56.128
NETMASK=255.255.255.0
NETWORK=192.168.56.0
BROADCAST=192.168.56.255
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=enp0s8
UUID=cfa4b7fb-476e-4727-9f5b-583ad0a06483
DEVICE=enp0s8
ONBOOT=yes
```
然后重启网络，自动获取ip
```
/etc/init.d/network restart
```
这样就可以通过ssh 192.168.56.128登录机器了，告别virtualBox的不友好窗口了

### 1.2.2 软件安装
基本软件安装
```
yum install -y net-tools vim gcc gcc-c++ cmake make git tcpdump netstat
```
dpdk依赖软件安装
```
yum install -y kernel-headers kernel-devel pciutils libpcap-devel numad numactl-devel numactl-libs tuned-profiles-cpu-partitioning
```
kernel链接修改(这里是我的kernel版本，具体是哪个名称要看各自机器)
```
rm -f build ; ln -s /usr/src/kernels/3.10.0-862.14.4.el7.x86_64/ build
```

### 1.2.3 下载dpdk源码(这里下载18.08版本)
```
mkdir /root/src ; cd /root/src; git clone -b v18.08 https://github.com/dpdk/dpdk
```

# 2. 编译安装<a id="main-chapter-2"></a>
执行dpdk/usertools/dpdk-setup.sh脚本
```
./usertools/dpdk-setup.sh
```
选择15 --> [15] x86_64-native-linuxapp-gcc
选择18 --> [18] Insert IGB UIO module

