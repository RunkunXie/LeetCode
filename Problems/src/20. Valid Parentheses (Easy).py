class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True

        stack = []

        for v in s:

            if v in ['(', '[', '{']:

                stack.append(v)

            else:

                if stack:
                    p = stack.pop()
                else:
                    return False

                if p != {')': '(', ']': '[', '}': '{'}[v]:
                    return False

        if not stack:
            return True

