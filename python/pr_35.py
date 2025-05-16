"""Question is to find the circular primes we start with modifying the prime code to the
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes version which is way faster than what I originally have"""

import time

start_time = time.perf_counter()


# Code goes here
def primeList(n):
    no_list = [True for _ in range(2, n)]
    for i in range(2, int(n**0.5) + 1):
        for j, k in enumerate(no_list):
            if k:
                if i != j + 2 and (j + 2) % i == 0:
                    no_list[j] = False
    prime_list = [i + 2 for i, j in enumerate(no_list) if j]
    return prime_list


def stringfyList(prime_list):
    return list(map(lambda x: str(x), prime_list))


def main():
    prime_list = primeList(1000_001)
    str_list = stringfyList(prime_list)
    no_of_cyclic = 0
    for s in str_list:
        rotations = [
            int(s[i:] + s[:i]) for i in range(len(s))
        ]  # neat way of circular rotations
        if set(rotations).issubset(set(prime_list)):
            no_of_cyclic += 1

    print(no_of_cyclic)


main()

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time:.6f} seconds")
