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

    Tseerapi::RouterRequest req;
    req.obj = "Derek.Tseer.Develop.Web";
    req.lbGetType = Tseerapi::LB_GET_ALL;
    req.type = Tseerapi::LB_TYPE_LOOP;
    req.moduleName = "YuansxGetTseerWeb";
    ret = Tseerapi::ApiGetRoute(req, errmsg);
    std::cout << "[out]ret: " << ret << " errmsg: " << errmsg << std::endl;
    std::cout << "[out]ip: " << req.ip << std::endl;
    std::cout << "[out]port: " << req.port << std::endl;
    std::cout << "[out]isTcp: " << req.isTcp << std::endl;

    if (!ret) {
        Tseerapi::ApiRouteResultUpdate(req, 0, 1, errmsg);
        std::cout << "[report] errmsg: " << errmsg << std::endl;
    }

    return 0;
}

