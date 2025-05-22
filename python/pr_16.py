"""This is possible with simple print(sum(list(map(int, str(2**1000))))).
But I tried a recursive one just for one wikipedia"""

import time

start_time = time.perf_counter()


# Code goes here
def exp_by_squaring(x, n):
    if n < 0:
        return exp_by_squaring(1 / x, -n)
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return exp_by_squaring(x * x, n / 2)
    elif n % 2 != 0:
        return x * exp_by_squaring(x * x, (n - 1) / 2)


print(sum(map(lambda x: int(x), list(str(exp_by_squaring(2, 1000))))))
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time:.6f} seconds")
