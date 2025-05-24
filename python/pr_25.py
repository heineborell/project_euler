# 1000 digit fibonacci number
import time


start_time = time.perf_counter()


cache = {0: 0, 1: 1}


def fibo(n):
    if n in cache.keys():
        return cache[n]
    else:
        cache[n] = fibo(n - 1) + fibo(n - 2)
    return cache[n]


i = 0
fibo_list = []
while len(str(fibo(i))) < 1000:
    fibo_list.append(fibo(i))
    i += 1

print(i)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time}")
