#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int main(int argc, char **argv)
{
    queue<int> q;

    q.push(1);
    q.push(9);
    q.push(2);

    int a = q.front();
    q.pop();
    cout << a << endl;
    a = q.front();
    q.pop();
    cout << a << endl;

    return 0;
}

