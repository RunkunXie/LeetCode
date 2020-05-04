class Solution:
    """my sol"""
    def findComplement(self, num: int) -> int:

        ans = deque([])

        while num > 0:
            num, bit = divmod(num, 2)
            ans.appendleft(1 - bit)

        bit = 0
        ans_dec = 0
        while ans:
            ans_dec += ans.pop() * 2 ** bit
            bit += 1

        return ans_dec

class Solution:
    """online one-line"""
    def findComplement(self, num: int) -> int:

        bits = len(bin(num)[2:])

        return num ^ (2 ** bits - 1)

class Solution:
    """online one-line"""
    def findComplement(self, num: int) -> int:

        bits = int(math.log2(num)) + 1

        return num ^ (2 ** bits - 1)

