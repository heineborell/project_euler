import time
import math

"""Special Pythagorean Triplet. Using generating algorithm  with k and n,m coprimes from the https://en.wikipedia.org/wiki/Pythagorean_triple """


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
        return m


def prime_divisors(n):
    divisor_list = []
    if n > 1:
        while n % 2 == 0:
            divisor_list.append(divide(n, 2))
            n = n // 2

        for m in range(3, int(n**0.5) + 1, 2):
            while n % m == 0:
                divisor_list.append(divide(n, m))
                n = n // m

        if n > 2:
            divisor_list.append(n)

    return set(divisor_list)


def main():
    a = b = c = 0
    k = 1
    while a + b + c <= 1001:
        m = 1
        while a + b + c <= 1001:
            n = 0
            while a + b + c <= 1001 and m > n:
                common_div = prime_divisors(m).intersection(prime_divisors(n))
                a = k * (m**2 - n**2)
                b = k * (2 * m * n)
                c = k * (m**2 + n**2)
                if len(common_div) == 0 and a + b + c == 1000:
                    print(
                        (k, m, n, a, b, math.sqrt(a**2 + b**2), c, a + b + c, a * b * c)
                    )
                    return a * b * c
                n += 1

            m += 1

        a = b = c = 0
        k += 1


if __name__ == "__main__":
    start_time = time.perf_counter()
    print(main())
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time is {elapsed_time:.6f} seconds")
