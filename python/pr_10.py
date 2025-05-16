import time
import math

"""Sum of primes up to million."""


# Code goes here
def check_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            result = False
            break
    else:
        result = True

    return result


def main():
    list_of_primes = []
    for j in range(2, 2000_001):
        check = check_prime(j)
        if check:
            list_of_primes.append(j)
    return sum(list_of_primes)


if __name__ == "__main__":
    start_time = time.perf_counter()
    print(main())
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time is {elapsed_time:.6f} seconds")
