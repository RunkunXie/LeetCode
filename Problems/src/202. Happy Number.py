class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1:
            return True

        exist = set()
        while n != 1:
            exist.add(n)

            new_n = 0
            while n > 0:
                new_n += (n % 10) ** 2
                n //= 10

            if new_n in exist:
                return False

            n = new_n

        return True

