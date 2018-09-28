#include <iostream>

static int iter = 0;
class number
{
public:
    number() {
        mysn = ++iter;
    }
    number(const number& s) {
        mysn = ++iter;
    }
    int mysn;
};

void func(number& s)
{
    std::cout << s.mysn << std::endl;
}

int main(int argc, char **argv)
{
    number a, b = a, c = b;

    func(a);
    func(b);
    func(c);

    return 0;
}

