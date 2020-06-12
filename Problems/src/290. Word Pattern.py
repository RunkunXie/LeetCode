class Solution:
    """my 2 dict sol, 1st attempt"""
    def wordPattern(self, pattern: str, str: str) -> bool:

        d1 = {}
        d2 = {}
        string = str.split()
        if len(pattern) != len(string): return False

        for i, (p, s) in enumerate(zip(pattern, string)):
            if p not in d1 and s not in d2:
                d1[p] = s
                d2[s] = p
            elif p in d1:
                if d1[p] != s:
                    return False
            elif s in d2:
                if d2[s] != p:
                    return False

        return True

    """online set + zip sol"""
    def wordPattern(self, pattern: str, str: str) -> bool:

        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

    """online map sol"""
    def wordPattern(self, pattern: str, str: str) -> bool:

        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))