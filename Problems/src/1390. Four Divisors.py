from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        ans = 0
        for num in nums:

            divisors = set()
            # the trick here is you only need to iterate from 1 to sqrt(num)
            for denominator in range(1, int(num ** 0.5) + 1):
                quotient, remainder = divmod(num, denominator)
                if remainder == 0:
                    divisors.add(denominator)
                    divisors.add(quotient)

                if len(divisors) > 4:
                    break

            if len(divisors) == 4:
                ans += sum(divisors)

        return ans

