#!/usr/bin/env python
from concurrent.futures import ThreadPoolExecutor, as_completed


def func(a):
    if a % 2:
        raise
    return None


def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(func, i) for i in range(10)]
        for future in as_completed(futures):
            try:
                print future.result()
            except Exception as e:
                print e
                


if __name__ == '__main__':
    main()
