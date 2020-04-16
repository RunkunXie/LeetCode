class Solution:
    def checkValidString(self, s: str) -> bool:

        s1 = []
        for char in s:
            if char is ')':
                if s1:
                    s1.pop()
                else:
                    return False

            else:
                s1.append(char)

        s2 = []
        for char in reversed(s):
            if char is '(':
                if s2:
                    s2.pop()
                else:
                    return False

            else:
                s2.append(char)

        return True
