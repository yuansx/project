#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <forward_list>
#include <array>
#include <deque>


using namespace std;

class Person
{
public:
    Person(int age) : _age(age), _name("") {}
    Person(string name) : _name(name), _age(18) {}

    void introduce() {
        cout << "name: " << _name << endl << "age: " << _age << endl;
    }

private:
    int _age;
    string _name;
};


bool find_num(const vector<int>::const_iterator& begin, const vector<int>::const_iterator& end, int num)
{
    vector<int>::const_iterator iter = begin;
    while (iter != end) {
        if (*iter == num)
            return true;
        ++iter;
    }

    return false;
}

int main(int argc, char **argv)
{
    vector<int> a;
    string b;
    forward_list<int> d;
    array<int, 4> e;
    deque<int> f;

    for (int i = 1; i < 10; ++i)
        a.push_back(i);
    list<int> c(a.begin(), a.end());

    cout << "find num: " << 10 << ", result: " << find_num(a.begin(), a.end(), 10) << endl;
    cout << "find num: " << 5 << ", result: " << find_num(a.cbegin(), a.cend(), 5) << endl;

    auto iter = c.begin();
    while (iter != c.end()) {
        cout << "list: " << *(iter++) << endl;
    }

    vector<int> g;
    g.swap(a);
    for (auto iter = g.crbegin(); iter != g.crend(); ++iter) {
        cout << "new vector : " << *iter << endl;
    }

    list<int> h;
    h.assign(5, -1);
    for (auto iter = h.cbegin(); iter != h.cend(); ++iter)
        cout << "assigin list: " << *iter << endl;

    vector<Person> p;
    for (auto i = 0; i < 3; ++i)
        p.emplace_back(i);
    p.emplace_back("Yuan");
    p.emplace_back("Shang");
    p.emplace_back("Xiao");

    for (auto i = p.begin(); i != p.end(); ++i)
        i->introduce();

    return 0;
}

