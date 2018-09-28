#include <iostream>
#include <string>

using namespace std;

int main(int argc, char **argv)
{
    string s("YSXiaoIT@foxmail.com");

    cout << "find fox at " << s.find("fox") << endl;
    cout << "Find yuan at " << s.find("yuan") << endl;

    cout << "find io first at " << s.find_first_of("io") << endl;
    cout << "find first YSXIT not at " << s.find_first_not_of("YSXIT") << endl;

    cout << "find o at " << s.find('o') << endl;
    cout << "find o at " << s.find('o', 8) << endl;

    cout << stoi("335d") << endl;

    return 0;
}

