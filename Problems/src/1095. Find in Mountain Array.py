# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    """my sol under hint, using start + 1 < end"""
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        # find peak
        start = 0
        end = mountain_arr.length() - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid - 1):
                start = mid
            else:
                end = mid
        peak = start if mountain_arr.get(start) > mountain_arr.get(end) else end

        # bisearch left
        start = 0
        end = peak
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) > target:
                end = mid
            else:
                start = mid
        if mountain_arr.get(start) == target:
            return start
        elif mountain_arr.get(end) == target:
            return end

        # bisearch right
        start = peak
        end = mountain_arr.length() - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) > target:
                start = mid
            else:
                end = mid
        if mountain_arr.get(start) == target:
            return start
        elif mountain_arr.get(end) == target:
            return end

        return -1

    """my sol under, using start <= end"""
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        # find peak
        start = 0
        end = mountain_arr.length() - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid - 1):
                start = mid
            else:
                end = mid
        peak = start if mountain_arr.get(start) > mountain_arr.get(end) else end

        # bisearch left
        start = 0
        end = peak
        while start <= end:
            mid = start + (end - start) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) > target:
                end = mid - 1
            else:
                start = mid + 1

        # bisearch right
        start = peak
        end = mountain_arr.length() - 1
        while start <= end:
            mid = start + (end - start) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) > target:
                start = mid + 1
            else:
                end = mid - 1

        return -1