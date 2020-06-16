class Solution:
    """my sol under hint, 1st attempt"""
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverseList(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        # reverse whole list
        reverseList(0, len(s) - 1)

        # reverse each word
        start = 0
        while start < len(s):
            end = start
            while end < len(s) and s[end] != ' ':
                end += 1
            reverseList(start, end - 1)
            start = end + 1

