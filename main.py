import sys
sys.setrecursionlimit(20000)

import time
start = time.time()

cache = {}

def S(n: int) -> int:
    if type(n).__name__ != "int" or n < 1:
        raise ValueError(f"Invalid argument \"{n}\": input must be a natural number.")
    if n == 1 or n == 2:
        cache[n] = n
        return n
    try:
        if n%2 == 0:
            res = cache[n-1] + cache[n-2]
        if n%2 == 1:
            res = 2*cache[n-1] - cache[n-2]
        return res
    except:
        if n%2 == 0:
            res = S(n-1) + S(n-2)
        if n%2 == 1:
            res = 2*S(n-1) - S(n-2)
        cache[n] = res
        return res

print("\n", S(10000), "\n")

end = time.time()

print(f"Runtime: {end-start} s.")

