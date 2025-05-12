import time


# Code goes here
def check_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            result = False
            break
    else:
        result = True

    if result:
        return n


def nth_prime(n):
    prime_list = []
    j = 2
    while n > len(prime_list):
        prime_check = check_prime(j)
        if prime_check is not None:
            prime_list.append(prime_check)
        j += 1

    return prime_list


if __name__ == "__main__":
    start_time = time.perf_counter()

    print(nth_prime(10001))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time is {elapsed_time:.6f} seconds")
