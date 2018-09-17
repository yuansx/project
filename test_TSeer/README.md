https://github.com/Tencent/TSeer.git
安装在172.18.0.128机器上
TseerServer中Tseer.TseerServer.QueryObj的Endpoint=tcp -h  172.18.0.128 -p 9903 -t 50000
TseerAgent安装在172.17.0.2机器上

以下测试代码在172.17.0.2的机器上运行

文件名 | 功能
-------|-------
agentApi_single.cc | 通过TseerAgent获取某个Obj单个路由信息
agentApi_multi.cc  | 通过TseerAgent获取某个Obj所有路由信息
pureApi_single.cc  | 通过纯Api方式获取某个Obj单个路由信息
pureApi_multi.cc   | 通过纯Api方式获取某个Obj所有路由信息
makefile           | 编译这几个功能的makefile

