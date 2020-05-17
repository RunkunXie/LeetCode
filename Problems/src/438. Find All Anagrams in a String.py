class Solution:
    """my sol - dict, 1 attempt, time n"""
    def findAnagrams(self, s: str, p: str) -> List[int]:

        c = Counter(p)
        d = defaultdict(int)
        ans = []

        i = j = 0
        while j < len(s):

            # new char
            char = s[j]

            # add new char:
            # if matching, add to d
            if char in c and d[char] < c[char]:
                d[char] += 1
            # if not matching, reset d
            elif char not in c:
                d = defaultdict(int)
                i = j + 1
            # if matching, but freq exceed, move i to reset freq
            elif d[char] == c[char]:
                d[char] += 1
                while i < j and d[char] > c[char]:
                    d[s[i]] -= 1
                    i += 1

            # check after add new char
            if c == d:
                ans.append(i)
            j += 1

        return ans

    """ans - dict + sliding window"""
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()

        output = []

        for i in range(ns):

            s_count[s[i]] += 1

            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1

            if p_count == s_count:
                output.append(i - np + 1)

        return output







