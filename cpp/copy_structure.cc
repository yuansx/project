#include <iostream>

using std::cout;
using std::endl;

class A
{
public:
    A() {
        cout << "create A" << endl;
    }
    A(const A& a) {
        cout << "copy create A" << endl;
    }
    A& operator=(const A& a) {
        cout << "assign A" << endl;
    }
    ~A() {
        cout << "destroy A" << endl;
    }
};

void func(A a)
{
    cout << "in func" << endl;
}

void func2(A& a)
{
    cout << "in func2" << endl;
}

int main(int argc, char **argv)
{
    A a;
    A b = a;
    A c(a);
    func(a);
    func2(a);
    return 0;
}

