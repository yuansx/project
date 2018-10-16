#!/bin/bash

MachineIp=`ifconfig eth0 | grep inet | awk '{print $2}'`
SQL_PASSWD=root@appinside
MachineName=`hostname`

if [ "x$MachineIp" == "x" ]; then
    echo "MachineIp is null"
    exit 0
fi

cd /usr/local/mysql
rm -rf data/*
perl scripts/mysql_install_db --user=mysql
sed -i "s/192.168.2.131/${MachineIp}/g" /usr/local/mysql/my.cnf
service mysql start
chkconfig mysql on
mysqladmin -u root password $SQL_PASSWD
mysqladmin -u root -h ${MachineName} password $SQL_PASSWD
mysql -uroot -p$SQL_PASSWD -e "grant all on *.* to 'tars'@'%' identified by 'tars2015' with grant option;"
mysql -uroot -p$SQL_PASSWD -e "grant all on *.* to 'tars'@'localhost' identified by 'tars2015' with grant option;"
mysql -uroot -p$SQL_PASSWD -e "grant all on *.* to 'tars'@'${MachineName}' identified by 'tars2015' with grant option;"
mysql -uroot -p$SQL_PASSWD -e "flush privileges;"
    
cd /root/src/tars/framework/sql
sed -i "s/192.168.2.131/${MachineIp}/g" `grep 192.168.2.131 -rl ./*`
sed -i "s/root@appinside/${SQL_PASSWD}/g" exec-sql.sh
sh exec-sql.sh

cd /usr/local/app/tars
sed -i "s/192.168.2.131/${MachineIp}/g" `grep 192.168.2.131 -rl ./*`

cd /root/src/tars/web/
sed -i "s/192.168.2.131/${MachineIp}/g" config/webConf.js
sed -i "s/192.168.2.131/${MachineIp}/g" config/tars.conf
npm run prd
