import time

start_time = time.perf_counter()

# Code goes here
no_list = [i for i in range(1, 101)]
sum_of_squares = sum(list(map(lambda a: a * a, no_list)))
sums = sum(no_list)
print(sums * sums - sum_of_squares)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time:.6f} seconds")
