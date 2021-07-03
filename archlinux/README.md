
# 1. 下载iso安装包 <a id="main-chapter-1"></a>
```
https://archlinux.org/download/
```
使用HTTP，China的163.com下载点

# 2. U盘刻录
我这里使用的是U大侠，iso，选择RAW方式写入

# 3. 重启电脑
- 1. 启动 - 安全启动 - 选择其他系统（允许非Windows系统以EFI模式启动）
- 2. 选择U盘启动
- 3. 选择arch linux启动
- 4. 启动后确认是否EFI模式
```
ls /sys/firmware/efi/efivars
```
若报错则是非EFI模式启动

# 4. 网络设置
我这里是以太网有线连接，默认都没问题，确认网络通即可
```
ping baidu.com
```

# 5. 启用ntp自动更新系统时间
```
timedatectl set-ntp true
timedatectl status
```

# 6. 分区设置
## 6.1 分区
我用的是新硬盘/dev/sdc
```
查看当前硬盘分区
lsblk
使用交互式进行分区
cfdisk /dev/sdc
```
我这里分区如下
| Device | Size | Type | Describe |
| ------ | ---- | ---- | -------- |
| /dev/sdc1 | 600M | EFI | linux efi boot |
| /dev/sdc2 | 300G | Extended | Linux Extended |
| /dev/sdc5 | 100G | one of Extended | Linux /root |
| /dev/sdc6 | 100G | one of Extended | Linux /home |
| /dev/sdc7 | 100G | one of Extended | Linux / |
| /dev/sdc3 | 16G  | Linux swap / Solaris | Linux Swap |

## 6.2 格式化
格式化ext4
```
mkfs.ext4 /dev/sdc2
mkfs.ext4 /dev/sdc5
mkfs.ext4 /dev/sdc6
mkfs.ext4 /dev/sdc7
```
格式化swap并激活
```
mkswap /dev/sdc3
swapon /dev/sdc3
```
格式化EFI
```
mkfs -t vfat /dev/sdc1
```

## 6.3 挂载分区
```
mount /dev/sdc7 /mnt
mkdir -p /mnt/root /mnt/home /mnt/boot/efi
mount /dev/sdc6 /mnt/home
mount /dev/sdc5 /mnt/root
mount /dev/sdc1 /mnt/boot/efi
```

# 7. 安装系统基本软件
```
可把就近源，且网络较好的点放在前面
vim /etc/pacman.d/mirrorlist
安装
pacstrap /mnt base linux linux-firmware vim
```

# 8. 配置系统
- 1. 设置启动自动挂载
```
genfstab -U /mnt >> /mnt/etc/fstab
```
- 2. chroot到新系统设置
```
arch-chroot /mnt
```
- 3. 设置时区为上海
```
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```
- 4. 硬件时间设置为UTC
```
hwclock --systohc
```
- 5. 语言设置
```
vim /etc/locale.gen
放开注释
en_US.UTF-8 UTF-8
zh_CN.UTF-8 UTF-8
zh_CN.GB2312
zh_TW.UTF-8 UTF-8
生成locale
locale-gen
echo LANG=en_US.UTF-8 > /etc/locale.conf
```

# 9. host设置
```
echo xiao-archlinux > /etc/hostname
vim /etc/hosts
127.0.0.1 localhost
::1 localhost
127.0.0.1 xiao-archlinux.localdomain xiaoarchlinux
```

# 10. 密码
```
passwd
```

# 11. 安装引导
- 1. 安装grub
```
pacman -S grub efibootmgr ntfs-3g os-prober
```

- 2. 设置grub
```
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=grub
```

- 3. 生成配置
```
grub-mkconfig -o /boot/grub/grub.cfg
```

# 12. 退出重启
```
exit
umount -R /mnt
reboot
```

# 13. 网络配置
- 1. 先配置静态IP连公网
```
ip link set dev eth0 up
ip a add 192.168.64.100/24 dev eth0
ip r add default via 192.168.64.1 dev eth0
echo "nameserver 192.168.64.1" >> /etc/resolv.conf
```
- 2. 下载软件包
```
pacman -S netctl dhcpcd
```
- 3. 修改网卡名称
我的网卡名称为enp3s0，还是比较熟悉传统的eth0
```
ln -s /dev/null /etc/udev/rules.d/80-net-setup-link.rules
reboot
```
- 4. 拷贝netctl例子使用
```
cp /etc/netctl/examples/ethernet-dhcp /etc/netctl/eth0
```
- 5. 启用
```
netctl start eth0
开启自动启用
netctl enable eth0
重新加载
netctl reenable eth0
```
- 6. 另一个NetworkManager
```
pacman -S networkmanager
systemctl enable NetworkManager
systemctl start NetworkManager
pacman -S network-manager-applet
```

# 14. 安装独立显卡驱动
```
lspci -k | grep -A 2 -E "(VGA|3D)"
我这里是NVIDIA [GeForce GTX 960]
pacman -S nvidia
reboot
nvidia-xconfig
```

# 15. 桌面安装
```
pacman -S xorg-server xorg-xinit
pacman -S xfce4 xfce4-goodies
pacman -S plasma kde-applications
pacman -S sddm
systemctl enable sddm
```

# 16. 检查服务启动
```
查看systemd启动失败的服务
systemctl --failed
查看/var/log日志文件中是否存在错误
journalctl -p 3 -xb
安装微码，启动时，CPU异常的修正，防止意外停机
pacman -S intel-ucode # amd的cpu安装amd-ucode
```
shadowsocks

