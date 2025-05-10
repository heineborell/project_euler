import time


start_time = time.perf_counter()


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


i = 0
fibo_list = []
while fibo(i) < 4000_000:
    fibo_list.append(fibo(i))
    i += 1

even_fibo = filter(lambda a: a % 2 == 0, fibo_list)
print(sum(list(even_fibo)))
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time}")
