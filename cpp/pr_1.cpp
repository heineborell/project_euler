#include <chrono> // for std::chrono functions
#include <cstddef>
#include <iostream>
#include <ranges>
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

template <typename T> T sum(std::vector<T> &array) {
  T sum{};
  for (T number : array)
    sum += number;
  return sum;
}

int main() {
  Timer t;
  std::vector<int> stack{};
  int range{100000};
  stack.reserve(static_cast<std::size_t>(range));
  for (range; range > 0; --range)
    if (range % 3 == 0 || range % 5 == 0) {
      stack.push_back(range);
    }
  std::cout << sum(stack) << '\n';

  // Code to time goes here

  std::cout << "Time elapsed: " << t.elapsed() << " seconds\n";

  return 0;
}
