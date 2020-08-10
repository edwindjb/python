fcache = {}

def _fib(n):
    global maxrdepth
    global currrdepth

    try:
        return fcache[n]
    except KeyError:
        if n  <= 1:
            return n
        else:
            fcache[n-2] = _fib(n-2)
            fcache[n-1] = _fib(n-1)
            fcache[n] = fcache[n-2] + fcache[n-1]
            return fcache[n]

def fib(n):
    res = -1

    if n < 0:
        raise Exception('n must be >= 0')
    if type(n) is not int:
        raise Exception('n must be int type')


    rlimit = 250
    chunksize = n // rlimit
    nruns = chunksize + [0,1][n % rlimit > 0]

    try:
        for i in range(1, nruns):
            res = _fib(rlimit * i)

        res = _fib(n)

    except RecursionError:
        print('recursion failure at {}'.format(n))
        print('lower value of rlimit from {}'.format(rlimit))

    else:
        return res


def fib2(n):
    res = -1

    if n < 0:
        raise Exception('n must be >= 0')
    if type(n) is not int:
        raise Exception('n must be int type')

    try:
        res = fcache[n]
    except KeyError:
        for i in range(0, n, 5):
            _fib(i+5)

    res = _fib(n)

    return res
