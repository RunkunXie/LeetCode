from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        return self.mergeSort(nums)

    def mergeSort(self, nums):

        if len(nums) == 1:
            return nums

        p = int(len(nums) / 2)
        nums1 = self.mergeSort(nums[:p])
        nums2 = self.mergeSort(nums[p:])

        return self.merge(nums1, nums2)

    @staticmethod
    def merge(nums1, nums2):

        if len(nums1) == 0 and len(nums2) == 0:
            return []

        elif len(nums1) == 0 or len(nums2) == 0:
            return nums1 + nums2

        i = j = 0
        merge_nums = []
        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                merge_nums.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                merge_nums.append(nums2[j])
                j += 1
            else:
                merge_nums.append(nums1[i])
                merge_nums.append(nums2[j])
                i += 1
                j += 1

        if i < len(nums1) or j < len(nums2):
            merge_nums += nums1[i:] + nums2[j:]

        return merge_nums

    @staticmethod
    def merge_slower(nums1, nums2):

        if len(nums1) == 0 and len(nums2) == 0:
            return []

        elif len(nums1) == 0 or len(nums2) == 0:
            return nums1 + nums2

        merge_nums = []
        while nums1 or nums2:
            if nums1[0] <= nums2[0]:
                merge_nums.append(nums1.pop(0))
            else:
                merge_nums.append(nums2.pop(0))

            if len(nums1) == 0 or len(nums2) == 0:
                merge_nums += nums1 + nums2
                break

        return merge_nums


print(Solution().mergeSort([5, 1, 1, 2, 0, 0]))
