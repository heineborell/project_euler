import time

start_time = time.perf_counter()


# Code goes here
def check_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            result = False
            break
    else:
        result = True

    return result


def divide(n, m):
    if n % m == 0 and check_prime(m):
        return n // m, m


def largest_prime(n):
    divisor_list = []
    for m in range(2, n):
        left_over = divide(n, m)
        if isinstance(left_over, tuple) and len(left_over) == 2:
            while left_over is not None:
                divisor_list.append((left_over[1], left_over[0]))
                n = left_over[0]
                left_over = divide(n, m)

    print(divisor_list)


largest_prime(60085147)


end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time:.6f} seconds")
