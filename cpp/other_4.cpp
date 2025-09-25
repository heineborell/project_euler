#include <cassert> // for assert
#include <chrono>  // for std::chrono functions
#include <cstdint> // for std::int64_t
#include <iostream>

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

constexpr std::int64_t powint(std::int64_t base, int exp) {
  assert(exp >= 0 && "powint: exp parameter has negative value");

  // Handle 0 case
  if (base == 0)
    return (exp == 0) ? 1 : 0;

  std::int64_t result{1};
  while (exp > 0) {
    if (exp & 1) // if exp is odd
      result *= base;
    exp /= 2;
    base *= base;
  }

  return result;
}

int countDigit(long n) {
  if (n == 0)
    return 1;
  int count{};
  while (n > 0) {
    n /= 10;
    ++count;
  }
  return count;
}

long reverseNumber(long number) {
  int digitno{countDigit(number) - 1};
  int pow{0};
  long reversed{};
  for (; digitno >= 0; --digitno) {
    reversed += ((number / powint(10, pow)) % 10) * powint(10, digitno);
    ++pow;
  }
  return reversed;
}

bool isPalindrome(long n) {
  if (n == reverseNumber(n))
    return true;
  else
    return false;
}

long largestPalindrome() {
  long largest{};
  long product{};
  for (int i{100}; i <= 1000; ++i) {
    for (int j{i}; j <= 1000; ++j) {
      product = i * j;
      if (isPalindrome(product) && product > largest)
        largest = product;
    }
  }
  return largest;
}

int main() {
  Timer t;

  std::cout << std::boolalpha;
  std::cout << largestPalindrome() << '\n';
  std::cout << "Time elapsed: " << t.elapsed() << " seconds\n";

  return 0;
}
