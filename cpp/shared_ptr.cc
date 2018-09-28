#include <iostream>
#include <vector>
#include <memory>
#include <string>

using namespace std;

class IntBlob {
public:
    IntBlob() : data(make_shared<vector<int>>()) {}
    IntBlob(initializer_list<int> il) : data(make_shared<vector<int>>(il)) {}
    int& front() {
        check(0, "front on empty IntBlob");
        return data->front();
    }
    int& back() {
        check(data->size() - 1, "back on empty IntBlob");
        return data->back();
    }
    void push_back(int e) {
        data->push_back(e);
    }
    void pop_back() {
        if (!data->empty())
            data->pop_back();
    }
    void push_back(const int& e) const {
        data->push_back(e);
    }
    void dump() const {
        for (const auto i : *data)
            cout << i << " ";
        cout << endl;
    }

private:
    shared_ptr<vector<int>> data;
    void check(size_t idx, const string& msg) {
        if (idx >= data->size())
            throw out_of_range(msg);
    }
};

int main(int argc, char **argv)
{
    IntBlob a{54, 6, 2, 0};
    a.push_back(1);
    a.push_back(33);
    a.dump();
    return 0;
}

