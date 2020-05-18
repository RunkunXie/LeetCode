class Solution:
    """my sol, dict + match count, time n, space 1"""
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)
        i = j = 0
        count = 0

        c = Counter(s1)
        d = defaultdict(int)

        for i in range(n2):

            char = s2[i]

            if char not in c:
                d = defaultdict(int)
                j = i + 1
                count = 0

            elif char in c:
                d[char] += 1
                count += 1

                while d[char] > c[char] and j < i:
                    d[s2[j]] -= 1
                    j += 1
                    count -= 1

            if count == n1:
                return True

        return False

