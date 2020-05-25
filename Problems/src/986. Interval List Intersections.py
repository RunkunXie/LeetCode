class Solution:
    """my sol, time m+n"""
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        n, m = len(A), len(B)
        ans = []

        idxB = 0

        for startA, endA in A:

            for i in range(idxB, m):

                startB, endB = B[i]

                # interval B too small
                if endB < startA:
                    idxB += 1
                    continue

                # interval B too large
                if startB > endA:
                    break

                ans.append([max(startA, startB), min(endA, endB)])

        return ans



