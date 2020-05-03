class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can = max(candies)
        ans = [can + extraCandies >= max_can for can in candies]

        return ans