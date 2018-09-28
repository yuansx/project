#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main(int argc, char **argv)
{
    map<string, vector<string>> family;
    vector<string> s;
    s.push_back("Shang");
    family.insert(make_pair("Yuan", s));

    return 0;
}

