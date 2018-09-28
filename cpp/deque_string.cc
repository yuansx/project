#include <iostream>
#include <string>
#include <deque>
#include <list>

using namespace std;

int main(int argc, char **argv)
{
//    deque<string> d;
    list<string> d;
    string str;

    while (cin >> str)
        d.push_back(str);
    for (auto iter = d.cbegin(); iter != d.cend(); ++iter)
        cout << *iter << endl;

    return 0;
}

