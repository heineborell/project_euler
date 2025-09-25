import time


start_time = time.perf_counter()
no_list = []
for i in reversed(range(100000)):
    if i % 3 == 0 or i % 5 == 0:
        no_list.append(i)

print(sum(no_list))

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time}")
