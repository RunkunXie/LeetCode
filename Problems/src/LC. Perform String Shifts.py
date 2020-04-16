from typing import List


class Solution:
    """my sol"""

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        n = len(s)

        for direct, amount in shift:
            total_shift += amount if not direct else -amount

        return s[total_shift % n:] + s[:total_shift % n]


""" Example
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
"""
