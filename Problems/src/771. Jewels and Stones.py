class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j = set(J)

        return sum([s in J for s in S])