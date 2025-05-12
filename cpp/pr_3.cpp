#include <chrono> // For timing
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;
using namespace std::chrono;

// Function to check if a number is prime (optimized for large numbers)
bool check_prime(long long n) {
  if (n <= 1) {
    return false;
  }
  for (long long i = 2; i <= sqrt(n); ++i) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

// Function to divide and check if the divisor is prime
pair<long long, long long> divide(long long n, long long m) {
  if (n % m == 0 && check_prime(m)) {
    return make_pair(n / m, m);
  }
  return make_pair(-1, -1); // Return (-1, -1) if no division is possible
}

// Function to find prime factors
void prime_factors(long long n) {
  vector<pair<long long, long long>> divisor_list;

  // Check for factor of 2 first (to speed up processing)
  while (n % 2 == 0) {
    divisor_list.push_back(make_pair(n / 2, 2));
    n /= 2;
  }

  // Check for odd factors starting from 3
  for (long long m = 3; m <= sqrt(n); m += 2) {
    while (n % m == 0) {
      divisor_list.push_back(make_pair(n / m, m));
      n /= m;
    }
  }

  // If n is still greater than 2, then it's prime
  if (n > 2) {
    divisor_list.push_back(make_pair(1, n));
  }

  // Print the prime factors
  for (const auto &divisor : divisor_list) {
    cout << "(" << divisor.second << ", " << divisor.first << ")" << endl;
  }
}

int main() {
  long long number = 600851475143;

  auto start = chrono::high_resolution_clock::now();

  prime_factors(number);

  auto end = chrono::high_resolution_clock::now();

  auto duration = chrono::duration_cast<chrono::microseconds>(end - start);
  cout << "Execution time: " << duration.count() << " microseconds" << endl;

  return 0;
}
