#include <chrono>
#include <iostream>
#include <ranges>
#include <string>

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

long reverseString(std::string &stringNumber) {
  std::string reversedString{};
  for (char element : std::views::reverse(stringNumber)) {
    reversedString.push_back(element);
  }

  return stol(reversedString);
}

bool isPalindrome(long n) {
  std::string stringed{std::to_string(n)};
  if (n == reverseString(stringed))
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
