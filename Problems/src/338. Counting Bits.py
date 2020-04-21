from typing import List


class Solution:
    """"""

    """online dp sol, time n"""
    def countBits(self, num: int) -> List[int]:

        if num == 0:
            return [0]

        ans = [0]

        for i in range(1, num + 1):
            if i % 2 == 0:
                ans.append(ans[i // 2])
            else:
                ans.append(ans[i // 2] + 1)

        return ans