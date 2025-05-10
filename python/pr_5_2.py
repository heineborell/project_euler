import time

start_time = time.perf_counter()

# Code goes here

i = 2
no_list = list(range(1, 20))
while not all(i % ele == 0 for ele in no_list):
    i += 1

print(i)
# no_list = list(range(1, 11))
# filtered_list = no_list.copy()
# for j in reversed(no_list):
#     for i in no_list:
#         if j != i and i != 1 and j % i == 0:
#             print(f"{j} is divisible by {i}")
#             if j in filtered_list:
#                 filtered_list.remove(j)
#             break
#
# print(filtered_list)
# result = 1
# for i in filtered_list:
#     result = result * i
#
# print(result)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time:.6f} seconds")
