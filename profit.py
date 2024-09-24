from collections import deque
from itertools import accumulate

def maxSum(arr,k):
    n = len(arr)
    prefix_sums = list(accumulate(map(int, arr), initial=0))
    # elements like `(pre_sums[i], i)`,  decreasing in the
    # `pref_sums[i]` part but increasing in the `i` part.
    deq = deque()
    answer = -1 << 63
    for i in range(n + k + 1):
        if deq and deq[0][1] < i - k:
            deq.popleft()
        if i <= n:
            while deq and deq[-1][0] <= prefix_sums[i]:
                deq.pop()
            deq.append((prefix_sums[i], i))
        if i >= k:
            # deq[0][0] is the maximum elements of pre_sums[i-d..min(n, i)]
            answer = max(answer, deq[0][0] - prefix_sums[i - k])
    print(answer)