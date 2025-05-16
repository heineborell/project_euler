import time
import ast

start_time = time.perf_counter()

# Code goes here
# Since we have product of 3 digit numbers aha maximum can be 999 which is less than 1000 and 1000^{2} is 1000_000
# Therefore any palindrom we find should be 6 digit number. First list all 6 digit palindroms which is determined
# by the first 3 digits so first list all palindroms with 6 digit


def GeneratePalindromes(n):
    three_digit_list = [str(i) for i in range(10 ** (n - 1), 10**n)]
    palindromes = [i + i[::-1] for i in three_digit_list]
    palindromes = [ast.literal_eval(i) for i in palindromes]
    return palindromes


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
        divisor_list.append(n)

    return divisor_list


def digit_dropper(no_list, n):
    no_list = [i for i in no_list if not any(len(str(j)) >= n + 1 for j in i[1])]
    return no_list


def FilterPalindromes(n):
    palindrome_divisors = [(i, largest_prime(i)) for i in GeneratePalindromes(n)]

    # drop the numbers with prime divisors that are n digits
    palindrome_divisors = digit_dropper(palindrome_divisors, n)

    # if the divisor list length is 3 multiply smallest and next
    for j, i in enumerate(palindrome_divisors):
        if len(i[1]) == 3:
            palindrome_divisors[j] = (i[0], [i[1][0] * i[1][1], i[1][2]])

    palindrome_divisors = digit_dropper(palindrome_divisors, n)

    for j, i in enumerate(palindrome_divisors):
        div_list = i[1]
        while len(str(div_list[0] * div_list[-1])) <= n:
            new_list = div_list[1:-1]  # slice of the original list
            new_list.append(div_list[0] * div_list[-1])  # add your desired element here
            palindrome_divisors[j] = (i[0], new_list)
            div_list = new_list

        while len(str(div_list[0] * div_list[-2])) <= n:
            new_list = div_list[1:-2]  # slice of the original list
            new_list.append(div_list[0] * div_list[-2])  # add your desired element here
            new_list.append(div_list[-1])
            palindrome_divisors[j] = (i[0], new_list)
            div_list = new_list

    for j, i in enumerate(palindrome_divisors):
        if len(i[1]) == 2:
            print(palindrome_divisors[j])


FilterPalindromes(3)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time:.6f} seconds")
