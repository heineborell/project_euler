#include <chrono> // for std::chrono functions
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

int fibonacci(int n) {
  if (n == 0)
    return 0;
  else if (n == 1)
    return 1;
  else
    return fibonacci(n - 1) + fibonacci(n - 2);
}

template <typename T> T evenSum(std::vector<T> &array) {
  T sum{};
  for (T number : array)
    if (number % 2 == 0)
      sum += number;
  return sum;
}

int main() {
  Timer t;
  int i{0};
  int result{0};
  std::vector<int> stack{};

  while (result < 4000000) {
    result = fibonacci(i);
    stack.push_back(result);
    ++i;
  }
  std::cout << evenSum(stack) << '\n';

  std::cout << "Time elapsed: " << t.elapsed() << " seconds\n";

  return 0;
}
