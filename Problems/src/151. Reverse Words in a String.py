class Solution:
    """my sol, 1st attempt"""
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))