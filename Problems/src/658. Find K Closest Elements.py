class Solution:
    """online bi search sol"""
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        A = arr
        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) // 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]

    """my sol start + 1 < end, need final check"""
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        A = arr
        left, right = 0, len(A) - k
        while left + 1 < right:
            mid = (left + right) // 2
            if x - A[mid] > A[mid + k] - x:
                left = mid
            else:
                right = mid

        if left + k == len(A) or x - A[left] <= A[left + k] - x:
            return A[left:left + k]
        else:
            return A[right:right + k]