class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        m, n = len(nums1), len(nums2)

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

        i = 0
        j = 0
        result = []

        while len(result) <= (m + n) / 2:

            result.append(min(nums1[i], nums2[j]))

            if nums1[i] < nums2[j] and i < m - 1:
                i += 1
            elif nums1[i] >= nums2[j] and j < n - 1:
                j += 1
            else:
                if nums1[i] < nums2[j]:
                    last_append_i = 1
                    last_append_j = 0
                else:
                    last_append_i = 0
                    last_append_j = 1
                break

        while len(result) <= (m + n) / 2 and last_append_i:
            result.append(nums2[j])
            j += 1

        while len(result) <= (m + n) / 2 and last_append_j:
            result.append(nums1[i])
            i += 1

        if (m + n) % 2 == 1:
            return result[-1]
        else:
            return sum(result[-2:]) / 2


s = Solution()
print("result:")
print(1.5, s.findMedianSortedArrays([1,2], []))
print(4, s.findMedianSortedArrays([], [3,4,5]))

print(2.5, s.findMedianSortedArrays([1,2], [3,4]))
print(3, s.findMedianSortedArrays([1,2], [3,4,5]))

print(2, s.findMedianSortedArrays([3], [1]))
print(2, s.findMedianSortedArrays([3], [1, 2]))

print(3, s.findMedianSortedArrays([3], []))
