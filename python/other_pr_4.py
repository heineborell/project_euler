import time

start_time = time.perf_counter()


def is_palindrome(n):
    return str(n) == str(n)[::-1]


largest_palindrome = 0
for i in range(100, 1000):
    for j in range(i, 1000):  # Start j from i to avoid duplicate calculations
        product = i * j
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product

print(largest_palindrome)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time:.6f} seconds")
