#include <iostream>
#include <deque>
#include <list>

using namespace std;

int main(int argc, char **argv)
{
    list<int> a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    deque<int> d1;
    deque<int> d2;

    for (auto iter = a.cbegin(); iter != a.cend(); ++iter) {
        if (*iter % 2)
            d1.push_back(*iter);
        else
            d2.push_back(*iter);
    }

    for (auto iter = d1.cbegin(); iter != d1.cend(); ++iter) {
        cout << "d1: " << *iter << endl;
    }
    for (auto iter = d2.cbegin(); iter != d2.cend(); ++iter) {
        cout << "d2: " << *iter << endl;
    }


    return 0;
}

