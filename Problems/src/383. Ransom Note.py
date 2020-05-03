class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        r, m = Counter(ransomNote), Counter(magazine)

        for k, v in r.items():
            if m.get(k, 0) < v:
                return False

        return True