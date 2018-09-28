#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using std::cout;
using std::endl;
using std::vector;
//using namespace std;

int main(int argc, char **argv)
{

    vector<int> a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6};
    vector<int>::const_iterator b = find(a.cbegin(), a.cend(), 5);
    int cnt = count(a.cbegin(), a.cend(), 5);
    int sum = accumulate(a.cbegin(), a.cend(), 0);
    cout << "find 5 " << *b << endl;
    cout << "5 count == " << cnt << endl;
    cout << "sum a = " << sum << endl;

    vector<int> aa = {1, 2};
    auto res = equal(a.cbegin(), a.cbegin() + 2, aa.cbegin());
    cout << "equal a and aa, res " << res << endl;

    vector<double> aaa = {1.1, 2.2, 3.3, 4.4, 5.5};
    double dsum = accumulate(aaa.cbegin(), aaa.cend(), 0);
    cout << "dsum = " << dsum << endl;

    fill(a.begin(), a.end(), 1);
    cout << "fill 1 sum = " << accumulate(a.cbegin(), a.cend(), 0) << endl;

    fill_n(a.begin(), a.size(), 2);
    cout << "fill 2 sum = " << accumulate(a.cbegin(), a.cend(), 0) << endl;

    vector<int> a4;
    fill_n(back_inserter(a4), 10, 1);
    cout << "back_inserter 10 1 sum = " << accumulate(a4.cbegin(), a4.cend(), 0) << endl;

    vector<int> a5(10, 0);
    cout << "a5 init sum = " << accumulate(a5.cbegin(), a5.cend(), 0) << endl;
    copy(a4.cbegin(), a4.cend(), a5.begin());
    cout << "copy from a4, a5 sum = " << accumulate(a5.cbegin(), a5.cend(), 0) << endl;

    replace(a5.begin(), a5.end(), 1, 2);
    cout << "replace 1 to 2, a5 sum = " << accumulate(a5.cbegin(), a5.cend(), 0) << endl;

    vector<int> origin = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6};
    cout << "origin: ";
    for (auto i : origin)
        cout << i << " ";
    cout << endl;
    sort(origin.begin(), origin.end());
    cout << "sort : ";
    for (auto &i : origin)
        cout << i << " ";
    cout << endl;
    auto unique_res = unique(origin.begin(), origin.end());
    cout << "unique: ";
    for (auto &i : origin)
        cout << i << " ";
    cout << endl;
    cout << "erase: ";
    origin.erase(unique_res, origin.end());
    for (auto &i : origin)
        cout << i << " ";
    cout << endl;

    return 0;
}

