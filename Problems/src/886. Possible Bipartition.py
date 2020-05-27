class Solution:
    """ans, time V + E"""
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        dislike = defaultdict(set)
        for d in dislikes:
            dislike[d[0]].add(d[1])
            dislike[d[1]].add(d[0])

        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in dislike[node])

        return all(dfs(node)
                   for node in range(1, N + 1)
                   if node not in color)





