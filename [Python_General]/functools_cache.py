import functools
import time


def fib(n):
    start=time.time()
    
    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
    stop=time.time()
    print("Function without cache takes{} sec".format(stop-start))    
    return result

@functools.lru_cache()
def fib1(n):
    start=time.time()
    if n <= 2:
        result = n
    else:
        result = fib1(n-1)[0] + fib1(n-2)[0]
    stop=time.time()
    #print("Function with cache takes {} sec".format(stop-start))
    return result, stop-start

print(fib(10))
print(fib1(10))
