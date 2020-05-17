"""Weekly Contest 189 - Q3"""


class Solution:
    """my set col, time n^2, beat 100, 100"""
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        fc_set = [set(com) for com in favoriteCompanies]
        ans = []

        for i in range(len(fc_set)):
            distinct = True
            for j in range(len(fc_set)):
                if i is not j and fc_set[i].issubset(fc_set[j]):
                    distinct = False
                    break
            if distinct:
                ans.append(i)

        return ans
