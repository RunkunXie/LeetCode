class Solution:
    """my sol, time m + n"""
    # def findMedianSortedArrays(self, nums1, nums2) -> float:
    #
    #     m, n = len(nums1), len(nums2)
    #
    #     # base cases
    #     if m == 0 and n != 0:
    #         if n % 2 == 1:
    #             return nums2[n // 2]
    #         else:
    #             return (nums2[n // 2 - 1] + nums2[n // 2]) / 2
    #     elif n == 0 and m != 0:
    #         if m % 2 == 1:
    #             return nums1[m // 2]
    #         else:
    #             return (nums1[m // 2 - 1] + nums1[m // 2]) / 2
    #     elif m == 0 and n == 0:
    #         return []
    #
    #     i = 0
    #     j = 0
    #     result = []
    #     midian = (m + n) / 2
    #
    #     # loop
    #     while len(result) <= midian:
    #
    #         result.append(min(nums1[i], nums2[j]))
    #
    #         if nums1[i] < nums2[j] and i < m - 1:
    #             i += 1
    #         elif nums1[i] >= nums2[j] and j < n - 1:
    #             j += 1
    #         else:
    #             if nums1[i] < nums2[j]:
    #                 last_append_i = 1
    #                 last_append_j = 0
    #             else:
    #                 last_append_i = 0
    #                 last_append_j = 1
    #             break
    #
    #     while len(result) <= midian and last_append_i:
    #         result.append(nums2[j])
    #         j += 1
    #
    #     while len(result) <= midian and last_append_j:
    #         result.append(nums1[i])
    #         i += 1
    #
    #     if (m + n) % 2 == 1:
    #         return result[-1]
    #     else:
    #         return sum(result[-2:]) / 2

    """my sol under hint, time log(n+m)"""
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        m, n = len(nums1), len(nums2)

        # base cases
        if m == 0 and n != 0:
            if n % 2 == 1:
                return nums2[n // 2]
            else:
                return (nums2[n // 2 - 1] + nums2[n // 2]) / 2
        elif n == 0 and m != 0:
            if m % 2 == 1:
                return nums1[m // 2]
            else:
                return (nums1[m // 2 - 1] + nums1[m // 2]) / 2
        elif m == 0 and n == 0:
            return []

        if m < n:
            nums1, nums2, m, n = nums2, nums1, n, m

        total = (m + n)
        half = int((total + 1) / 2)

        l, r = 0, n
        mid2 = int((r + l + 1) / 2)
        mid1 = half - mid2

        while True:
            if mid2 < n and nums1[mid1 - 1] > nums2[mid2]:
                l = mid2
                mid2 = int((r + l + 1) / 2)
                mid1 = half - mid2
            elif mid2 > 0 and nums2[mid2 - 1] > nums1[mid1]:
                r = mid2
                mid2 = int((r + l) / 2)
                mid1 = half - mid2
            else:
                break

        if int(total % 2) == 1:
            if mid2 == 0:
                return nums1[mid1 - 1]
            elif mid1 == 0:
                return nums2[mid2 - 1]
            else:
                return max(nums1[mid1 - 1], nums2[mid2 - 1])
        else:
            if mid2 == 0:
                if mid1 == m:
                    return (nums1[mid1 - 1] + nums2[mid2]) / 2
                return (nums1[mid1 - 1] + min(nums1[mid1], nums2[mid2])) / 2
            elif mid1 == 0:
                if mid2 == n:
                    return (nums2[mid2 - 1] + nums1[mid1]) / 2
                return (nums2[mid2 - 1] + min(nums2[mid2], nums1[mid1])) / 2
            elif mid1 == m:
                return (max(nums1[mid1 - 1], nums2[mid2 - 1]) + nums2[mid2]) / 2
            elif mid2 == n:
                return (max(nums1[mid1 - 1], nums2[mid2 - 1]) + nums1[mid1]) / 2
            else:
                return (max(nums1[mid1 - 1], nums2[mid2 - 1]) +
                        min(nums1[mid1], nums2[mid2])) / 2


s = Solution()
print("result:")
print(1.5, s.findMedianSortedArrays([1,2], []))
print(4, s.findMedianSortedArrays([], [3,4,5]))

print(2.5, s.findMedianSortedArrays([1,2], [3,4]))
print(3, s.findMedianSortedArrays([1,2], [3,4,5]))

print(2, s.findMedianSortedArrays([3], [1]))
print(2, s.findMedianSortedArrays([3], [1, 2]))

print(3, s.findMedianSortedArrays([3], []))


class Solution(object):
    """online clear python2 sol"""
    def findMedianSortedArrays(self, nums1, nums2):

        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0



