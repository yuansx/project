#include <iostream>
#include <memory>
#include <map>
#include <stdlib.h>
#include <unistd.h>

class C;
class A
{
public:
    ~A() {
        std::cout << "destroy A" << std::endl;
    }
    std::shared_ptr<C> c;
};

class B
{
public:
    ~B() {
        std::cout << "destroy B" << std::endl;
    }
    // 这里循环引用，会导致程序退出时，不会调用析构函数，从而资源无法回收
//    std::shared_ptr<A> a;
};

class C
{
public:
    ~C() {
        std::cout << "destroy C" << std::endl;
    }
    std::shared_ptr<B> b;
};

int main(int argc, char **argv)
{
    std::shared_ptr<A> a = std::make_shared<A>();
    a->c = std::make_shared<C>();
    a->c->b = std::make_shared<B>();
 //   a->c->b->a = a;

    return 0;
}

