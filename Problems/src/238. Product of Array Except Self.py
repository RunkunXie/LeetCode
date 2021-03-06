from typing import List


class Solution:
    """"""

    """time n, space 1, my intuitive solution"""
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #
    #     if not nums:
    #         return None
    #
    #     mul_all = 1
    #     count_0 = 0
    #     loc_0 = []
    #     for i, num in enumerate(nums):
    #         if num is not 0:
    #             mul_all *= num
    #         else:
    #             count_0 += 1
    #             loc_0.append(i)
    #
    #     if count_0 > 1:
    #         return [0] * len(nums)
    #     elif count_0 == 1:
    #         ans = [0] * len(nums)
    #         ans[loc_0[0]] = mul_all
    #         return ans
    #
    #     ans = []
    #     for i in range(len(nums)):
    #         ans.append(int(mul_all / nums[i]))
    #
    #     return ans

    """answer, time n, space 1"""
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The left and right arrays as described in the algorithm
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]

        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]

        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]

        return answer