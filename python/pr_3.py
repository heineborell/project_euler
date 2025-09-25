import time


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
    while n % 2 == 0:
        divisor_list.append(divide(n, 2))
        n = n // 2

    for m in range(3, int(n**0.5) + 1, 2):
        while n % m == 0:
            divisor_list.append(divide(n, m))
            n = n // m

    if n > 2:
        divisor_list.append((1, n))

    return divisor_list


if __name__ == "__main__":
    start_time = time.perf_counter()

    print(largest_prime(600851475143))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time is {elapsed_time:.6f} seconds")
