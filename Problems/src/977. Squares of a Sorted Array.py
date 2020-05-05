class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        if not A:
            return None

        ans = []
        i, j = 0, len(A) - 1

        while i < j:

            if abs(A[i]) < abs(A[j]):
                ans.append(A[j] ** 2)
                j -= 1
            else:
                ans.append(A[i] ** 2)
                i += 1

        ans.append(A[i] ** 2)

        return reversed(ans)