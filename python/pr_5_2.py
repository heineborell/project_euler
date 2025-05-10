# This is a faster python algorithm that uses +20 jumps for the number we look for
import time

start_time = time.perf_counter()

# Code goes here


def main():
    nbr = 20
    while True:
        i = 2
        while i <= 20:
            if nbr % i != 0:
                break
            i += 1
        if i == 21:
            print(nbr)
            return
        nbr += 20


main()
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time is {elapsed_time:.6f} seconds")
