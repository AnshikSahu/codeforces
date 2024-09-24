#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>

void maxSum(std::vector<int> arr, int k) {
    int n = arr.size();
    std::vector<long long> prefix_sums(n + 1, 0);

    for (int i = 0; i < n; i++) {
        prefix_sums[i + 1] = prefix_sums[i] + arr[i];
    }

    std::deque<std::pair<long long, int> > deq;
    long long answer = LLONG_MIN; // Initialize with the smallest possible value

    for (int i = 0; i <= n + k; i++) {
        while (!deq.empty() && deq.front().second < i - k) {
            deq.pop_front();
        }

        if (i <= n) {
            while (!deq.empty() && deq.back().first <= prefix_sums[i]) {
                deq.pop_back();
            }
            deq.push_back(std::make_pair(prefix_sums[i], i));
        }

        if (i >= k) {
            // deq.front().first is the maximum element of prefix_sums[i-d..min(n, i)]
            answer = std::max(answer, deq.front().first - prefix_sums[i - k]);
        }
    }

    std::cout << answer << std::endl;
}

int main() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    maxSum(arr, k);
    
    return 0;
}
