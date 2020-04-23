class Solution:
    """my sol, one-pass, time n, space 1"""
    def maxProduct(self, nums: List[int]) -> int:

        # record negative cumulative product
        neg = set()
        max_neg = - float("inf")

        # current cumulative product
        cur = 1
        ans = - float("inf")

        for num in nums:
            cur *= num

            # if cur > 0
            ans = max(ans, cur)

            # if cur < 0
            if cur < 0:
                if len(neg) > 0:
                    if cur > max_neg:
                        max_neg = cur
                    else:
                        ans = max(ans, cur / max_neg)

                neg.add(cur)
                max_neg = max(max_neg, cur)

            # if cur = 0, reset
            if cur == 0:
                neg = set()
                max_neg = - float("inf")
                cur = 1

        return int(ans)


