class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        dq = []
        ans = [0] * len(T)

        for i in range(len(T)):

            # pop
            while dq and T[i] > T[dq[-1]]:
                end_i = dq.pop()
                ans[end_i] = i - end_i

            # push
            dq.append(i)

        return ans