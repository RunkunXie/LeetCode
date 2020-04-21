class Solution:
    """my sol, time n, space n"""
    def findDuplicate(self, nums: List[int]) -> int:

        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return num

    """ans: Floyd's algorithm, time n, space 1"""
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare