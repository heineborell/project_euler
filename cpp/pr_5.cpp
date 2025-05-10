#include <iostream>
#include <chrono>

int main() {
    int i;
    int nbr = 20;

    auto start = std::chrono::high_resolution_clock::now();  // Start timing

    while (true) {
        i = 2;
        while (i <= 20) {
            if (nbr % i != 0)
                break;
            i++;
        }
        if (i == 21) {
            std::cout << nbr << std::endl;
            break;
        }
        nbr += 20;
    }

    auto end = std::chrono::high_resolution_clock::now();  // End timing

    std::chrono::duration<double> duration = end - start;
    std::cout << "Time taken: " << duration.count() << " seconds" << std::endl;

    return 0;
}
