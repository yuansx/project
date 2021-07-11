#!/usr/bin/env python3

def test_log2(func):
    def _log(*args, **kargs):
        print('-----log2-------')
        ret = func(*args, **kargs)
        return ret
    return _log


def test_log(func):
    def _log(*args, **kargs):
        print('begin {0}'.format(func))
        ret = func(*args, **kargs)
        print('end {0}'.format(func))
        return ret
    return _log


@test_log
@test_log2
def add(a, b):
    print('{0} + {1} = {2}'.format(a, b, a + b))


if __name__ == '__main__':
    add(1, 1)

