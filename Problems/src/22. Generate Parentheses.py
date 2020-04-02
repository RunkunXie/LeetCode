from typing import List


class Solution:
    """"""

    """answer"""

    def generateParenthesis(self, n: int) -> List[str]:
        return self.gen("", n, n)

    def gen(self, s: str, l: int, r: int) -> List[str]:
        if l == 0 and r == 0:
            return [s]

        left = self.gen(s + '(', l - 1, r) if l > 0 else []
        right = self.gen(s + ')', l, r - 1) if l < r else []

        return left + right


print(Solution().generateParenthesis(3))
