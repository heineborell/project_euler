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

struct Cache {
  int key{};
  int value{};
};

int fibonacci(std::vector<Cache> &cache, int n) {
  if (n <
      static_cast<int>(cache.size())) // checking if this value of n is computed
    return cache.data()[n].value;
  else
    cache.push_back({n, fibonacci(cache, n - 1) +
                            fibonacci(cache, n - 2)}); // if not compute
  return cache[static_cast<std::size_t>(n)].value;
}

int evenSum(std::vector<Cache> &array) {
  int sum{};
  for (Cache element : array)
    if (element.value % 2 == 0)
      sum += element.value;
  return sum;
}

int main() {
  Timer t;
  int i{0};
  std::vector<Cache> cache{{0, 1}, {1, 1}};

  while (cache.back().value < 400000000) {
    fibonacci(cache, i);
    ++i;
  }
  cache.pop_back(); // gotta take out the last one (should have written btter
                    // but whatever)
  std::cout << evenSum(cache) << '\n';

  std::cout << "Time elapsed: " << t.elapsed() << " seconds\n";

  return 0;
}
