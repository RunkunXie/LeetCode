class Solution:
    """my sol - 1 attempt, time n^2 * logn"""
    def simplifiedFractions(self, n: int) -> List[str]:

        ans = []
        pri = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

        for i in range(2, n + 1):

            # factors - takes log n
            cur_factor = []
            for p in pri:
                if p >= i:
                    break
                if i % p == 0:
                    cur_factor.append(p)

            # acceptable numerators
            for j in range(1, i):

                div = False
                for f in cur_factor:
                    if f > j:
                        break
                    if j % f == 0:
                        div = True
                        break

                if not div:
                    cur = "".join([str(j), '/', str(i)])
                    ans.append(cur)

        return ans

    """online sol - gcd, 1 line, time n^2 * logn"""
    def simplifiedFractions(self, n: int) -> List[str]:
        return ['%d/%d' % (a, b) for a in range(1, n) for b in range(a + 1, n + 1) if math.gcd(a, b) == 1]

    """online sol - dict, time n^2 which is fastest"""
    def simplifiedFractions(self, n: int) -> List[str]:

        res = []
        tmp = set()
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                cur = numerator / denominator
                if cur not in tmp:
                    res.append("{0}/{1}".format(numerator, denominator))
                    tmp.add(cur)
        return res