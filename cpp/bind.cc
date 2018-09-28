#include <iostream>
#include <functional>
#include <algorithm>
#include <numeric>

using namespace std;

bool check_size(const int a, const int size)
{
    return a > size;
}

bool change_size(const int& a, int& size)
{
    return a > size ? size = a, true : false;
}

int main(int argc, char **argv)
{
    vector<int> a = {1, 2,3, 4,5, 6, 7, 8, 3, 5,7, 2,45,7};

    auto tmp = find_if(a.cbegin(), a.cend(), bind(check_size, placeholders::_1, 10));
    if (tmp != a.cend())
        cout << tmp - a.cbegin() << " num is " << *tmp << endl;
    int size = 10;
    tmp = find_if(a.cbegin(), a.cend(), bind(change_size, placeholders::_1, ref(size)));
    if (tmp != a.cend())
        cout << tmp - a.cbegin() << " num is " << *tmp << ", and size " << 10 << " change to " << size << endl;

    return 0;
}

