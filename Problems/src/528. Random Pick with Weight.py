class Solution:
    """my bisearch sol, 1st attempt, time logn per pick, similar to ans"""
    def __init__(self, w: List[int]):
        self.w = w
        self.sum_w = []
        self.total = 0

        total = 0
        for we in w:
            total += we
            self.sum_w.append(total)
        self.total = total

    def pickIndex(self) -> int:

        r = randint(1, self.total)
        start, end = 0, len(self.w) - 1
        while start < end:
            mid = start + (end - start) // 2
            if r == self.sum_w[mid]:
                return mid
            elif r > self.sum_w[mid]:
                start = mid + 1
            else:
                end = mid

        return end

class SolutionOnline:
    """online bisearch sol, cleaner"""
    def __init__(self, w):
        self.w = list(itertools.accumulate(w))

    def pickIndex(self):
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

import bisect
w = [1,2,3]
a = [1,1,1,2,3,4,5,6]

for i in range(1, 7):
    print(i, bisect.bisect_left(a, i), bisect.bisect(a, i))
