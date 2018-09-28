#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int tmp = 10;
    auto f = [&]() {
        if (tmp > 0)
            while (--tmp);
        else if (tmp < 0)
            while (++tmp);
        else
            return true;
        return false;
    };
    cout << "first tmp = " << tmp << ", f() = " << f() << endl;
    cout << "second tmp = " << tmp << ", f() = " << f() << endl;

    tmp = -4;
    cout << "first tmp = " << tmp << ", f() = " << f() << endl;
    cout << "second tmp = " << tmp << ", f() = " << f() << endl;

    tmp = 0;
    cout << "first tmp = " << tmp << ", f() = " << f() << endl;
    cout << "second tmp = " << tmp << ", f() = " << f() << endl;

    return 0;
}

