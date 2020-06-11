class Solution:

    """my sol, modified from online ans, 1st attempt"""
    def addOperators(self, num: str, target: int) -> List[str]:

        def dfs(idx=0, path="", curr=0, prev=None):

            if idx == len(num) and curr == target:
                ans.append(path)
                return

            for i in range(idx + 1, len(num) + 1):
                if i == idx + 1 or (i > idx + 1 and num[idx] != '0'):
                    tmp = int(num[idx:i])
                    if prev is None:
                        dfs(i, path + num[idx:i], tmp, tmp)
                    else:
                        dfs(i, path + '+' + num[idx:i], curr + tmp, tmp)
                        dfs(i, path + '-' + num[idx:i], curr - tmp, - tmp)
                        dfs(i, path + '*' + num[idx:i], curr - prev + prev * tmp, prev * tmp)

        ans = []
        dfs()
        return ans