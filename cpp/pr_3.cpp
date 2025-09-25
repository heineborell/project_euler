#include <chrono> // for std::chrono functions
#include <cmath>
#include <iostream>
#include <vector>

class Timer {
private:
  // Type aliases to make accessing nested type easier
  using Clock = std::chrono::steady_clock;
  using Second = std::chrono::duration<double, std::ratio<1>>;

  std::chrono::time_point<Clock> m_beg{Clock::now()};

public:
  void reset() { m_beg = Clock::now(); }

  double elapsed() const {
    return std::chrono::duration_cast<Second>(Clock::now() - m_beg).count();
  }
};

struct Pair {
  long first{};
  long second{};
};

bool checkPrime(long n) {
  for (long m{2}; static_cast<long double>(m) < (std::sqrt(n) + 1); ++m) {
    if (n % m == 0)
      return false;
  }
  return true;
}

Pair divide(long n, long m) {
  if (n % m == 0 && checkPrime(m))
    return {n / m, m};
  else
    return {};
}

std::vector<Pair> largestPrime(long n) {
  std::vector<Pair> divisorlist{};
  // Handle the multiplies of 2
  while (n % 2 == 0) {
    divisorlist.push_back(divide(n, 2));
    n = n / 2;
  }

  for (int m{3}; static_cast<long double>(m) < (std::sqrt(n) + 1); m += 2) {
    while (n % m == 0) {
      divisorlist.push_back(divide(n, m));
      n = n / m;
    }
  }

  if (n > 2)
    divisorlist.push_back({1, n});
  return divisorlist;
}

template <typename T> void printArray(const std::vector<T> &array) {
  for (T element : array) {
    if (element.first != 0)
      std::cout << '{' << element.first << ',' << element.second << '}' << '\n';
  }
}

int main() {
  Timer t;
  std::cout << std::boolalpha;
  printArray(largestPrime(600851475143));
  // std::cout << largestPrime(600851475143).back().second << '\n';
  std::cout << "Time elapsed: " << t.elapsed() << " seconds\n";

  return 0;
}
