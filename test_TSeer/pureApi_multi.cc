#include <iostream>
#include <Tseer_api.h>
#include <Tseer_comm.h>

int main(int argc, char **argv)
{
    int ret = 0;
    std::string errmsg;

    Tseerapi::InitRawApiParams param;
    param.domainName = "172.18.0.128";
    param.registryPort = 9903;
    ret = Tseerapi::ApiSetRegistryInfo(param, errmsg);
    if (ret) {
        std::cout << "init registry error" << std::endl;
        return 0;
    }

    Tseerapi::RoutersRequest req;
    req.obj = "Derek.Tseer.Develop.Web";
    req.lbGetType = Tseerapi::LB_GET_ALL;
    ret = Tseerapi::ApiGetRoutes(req, errmsg);
    if (!ret) {
        for (const auto& it : req.nodeInfoVec) {
            std::string nodeInfo;
            nodeInfo += it.ip + ":" + std::to_string(it.port) + " | ";
            if (it.isTcp)
                nodeInfo += "tcp | ";
            else
                nodeInfo += "udp | ";
            nodeInfo += it.slaveSet;
            std::cout << "[NodeInfo]: " << nodeInfo << std::endl;

            Tseerapi::RouterRequest reportReq;
            reportReq.obj = req.obj;
            reportReq.lbGetType = req.lbGetType;
            reportReq.setInfo = req.setInfo;
            reportReq.ip = it.ip;
            reportReq.port = it.port;
            reportReq.isTcp = it.isTcp;
            Tseerapi::ApiRouteResultUpdate(reportReq, 0, 1, errmsg);
            std::cout << "[report] errmsg: " << errmsg << std::endl;
        }

    }

    return 0;
}

