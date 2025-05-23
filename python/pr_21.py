import time


# Code goes here
def find_divisors(n):
    i = 1
    divisor_list = []
    while i < n:
        if n % i == 0:
            divisor_list.append(i)

        i += 1

    return sum(divisor_list)


def number_divisor_list(limit):
    no_list = []
    for i in range(1, limit + 1):
        no_list.append((i, find_divisors(i)))

    return no_list


def amicable_numbers(limit):
    sum_list = []
    no_list = number_divisor_list(limit)
    for i in no_list:
        for j in no_list:
            if i == (j[1], j[0]) and i != j and sum(i) not in sum_list:
                sum_list.append(sum(i))

    print(sum(sum_list))


def main():
    amicable_numbers(10000)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time is {elapsed_time:.6f} seconds")
