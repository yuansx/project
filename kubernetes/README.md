# 目录
> * [1.环境介绍](#main-chapter-1)
> * [2.](#main-chapter-2)

# 1. 环境介绍
> * CentOS 8
> * Tencent CVM 4核8G
> * 192.168.0.9 k8s-master
> * 192.168.0.8 k8s-node1
> * 192.168.0.7 k8s-node2

对应机器执行
```
hostnamectl set-hostname k8s-master
```
在/etc/hosts添加
```
192.168.0.9 k8s-master
192.168.0.8 k8s-node1 
192.168.0.7 k8s-node2 
```

# 2. 关闭交换分区
```
swapoff -a
```
非云上机器还需要注释/etc/fstab对应交换分区

# 3. 禁用selinux
```
setenforce 0
```
非云上机器还要设置/etc/selinux/config中SELINUX=disabled关闭

# 4. 关闭防火墙
```
systemctl stop firewalld
systemctl disable firewalld
```
# 5. 禁用ipv6，开启v4转发
```
cat << EOF > /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
```
修改/etc/sysctl.conf
```
net.ipv4.ip_forward = 1
net.ipv6.conf.all.disable_ipv6=1
net.ipv6.conf.default.disable_ipv6=1
net.ipv6.conf.lo.disable_ipv6=1
```
重新加载
```
sysctl -p
sysctl --system
```

# 6. 安装docker
```
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum install -y docker-ce
```

# 7. docker设置并启动
```
cat << EOF > /etc/docker/daemon.json
{
    "exec-opts": ["native.cgroupdriver=systemd"]
}
EOF
```
```
systemctl daemon-reload
systemctl restart docker
systemctl enable docker
```

# 8. 安装kubeadm kubectl kubelet
```
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF
```
```
yum install kubeadm-1.23.1-0 kubectl-1.23.1-0 kubelet-1.23.1-0 --disableexcludes=kubernetes -y
```
安装最新版本，好像kubernetes与docker不兼容

# 9. 从阿里云拉取对应镜像
查看需要安装的镜像
```
kubeadm config images list
k8s.gcr.io/kube-apiserver:v1.23.6
k8s.gcr.io/kube-controller-manager:v1.23.6
k8s.gcr.io/kube-scheduler:v1.23.6
k8s.gcr.io/kube-proxy:v1.23.6
k8s.gcr.io/pause:3.6
k8s.gcr.io/etcd:3.5.1-0
k8s.gcr.io/coredns/coredns:v1.8.6
```
对应使用docker拉取并打tag，譬如
```
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:v1.23.6
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:v1.23.6 k8s.gcr.io/kube-apiserver:v1.23.6
docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:v1.23.6
```
注意coredns阿里云地址为registry.cn-hangzhou.aliyuncs.com/google_containers/coredns:v1.8.6

# 10. 安装kubernetes对应组件
```
kubeadm init --apiserver-advertise-address=192.168.0.9 --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=Swap
```
如果失败，可先删除重来
```
kubeadm reset
```

# 11. 记录token，忘了可查
```
kubeadm token list
```
默认24小时过期，重新生成
```
kubeadm token create
```

# 12. 配置kubectl命令环境
如果用的是zsh，则放到对应的.zsh_profile
```
echo "export KUBECONFIG=/etc/kubernetes/admin.conf" >> ~/.bash_profile
echo "source <(kubectl completion bash)" >> ~/.bashrc
source ~/.bash_profile
source ~/.bashrc
```
如果使用非root用户，则需要拷贝对应文件
```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
echo "source <(kubectl completion bash)" >> ~/.bashrc
source ~/.bashrc
```

# 13. 安装pod网络
```
wget https://github.com/flannel-io/flannel/blob/master/Documentation/kube-flannel.yml
kubectl apply -f kube-flannel.yml
```
先下载，再安装，如果下载不了，则考虑到别处找

# 14. node机器上
执行步骤1-8后
```
kubeadm join --token d38a01.13653e584ccc1980 192.168.0.9:6443
```
