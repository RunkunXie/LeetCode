class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        result = 0

        AB = {}
        for a in A:
            for b in B:
                ab = a + b
                if a + b in AB:
                    AB[ab] += 1
                else:
                    AB[ab] = 1

        for c in C:
            for d in D:
                cd = c + d
                if -cd in AB:
                    result += AB[-cd]

        return result

        # import collections
        # AB = collections.Counter(a + b for a in A for b in B)
        # return sum(AB[- c - d] for c in C for d in D)