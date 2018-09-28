#include <iostream>
#include <deque>

using namespace std;

int main(int argc, char **argv)
{
    deque<int> a = {1, 2, 3, 4, 5};
    auto &b = a.back();
    cout << b << endl;
    b = 2;

    for (deque<int>::size_type i = 0; i < a.size(); ++i)
        cout << "deque[" << i << "] = " << a.at(i) << endl;

    return 0;
}

