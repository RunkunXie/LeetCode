class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bits = len(bin(N)[2:])

        return N ^ (2 ** bits - 1)
