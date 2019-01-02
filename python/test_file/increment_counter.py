def CreateCounter():
    n = 0
    def counter(j):
        def count():
            return ++j
        return count
    def count():
        return counter(n)
    return count

counterA = CreateCounter()
print(counterA(), counterA())
