# This is the brute force simple code version
import time

start_time = time.perf_counter()

# Code goes here

i = 2
no_list = list(range(1, 20))
while not all(i % ele == 0 for ele in no_list):
    i += 1

print(i)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time:.6f} seconds")
