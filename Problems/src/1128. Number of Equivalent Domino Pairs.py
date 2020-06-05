class Solution:
    """check c++ for my sol"""

    """online sol time n"""
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(v * (v - 1) // 2 for v in Counter(tuple(sorted(x)) for x in dominoes).values())