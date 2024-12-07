import sys
sys.setrecursionlimit(20000)

import time
start = time.time()

cache = {}

def L(n: int) -> int:
    if type(n).__name__ != "int" or n < 0:
        raise ValueError(f"Invalid argument \"{n}\": input must be a non-negative integer.")
    if n == 0:
        cache[n] = n
        return n
    if n in {1,2,3}:
        cache[n] = 1
        return 1
    try:
        return 2*cache[n-2] + cache[n-4]
    except:
        res = 2*L(n-2) + L(n-4)
        cache[n] = res
        return res

def S(n: int) -> int:
    return L(n+2)

print("\n", S(10000), "\n")

end = time.time()

print(f"Runtime: {end-start} s.")

