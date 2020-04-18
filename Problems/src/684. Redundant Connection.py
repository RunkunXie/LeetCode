from typing import List


class UnionFind:
    def __init__(self, n):
        self.graph = [i for i in range(n + 1)]

    def find(self, x):
        while x != self.graph[x]:
            # path compression
            self.graph[x] = self.graph[self.graph[x]]
            x = self.graph[x]
        return x

    def union(self, x, y):
        # join y to x
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            self.graph[yp] = xp


class Solution:
    """online Union-Find sol, time n space n"""
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        uf = UnionFind(len(edges))
        for edge in edges:
            x, y = uf.find(edge[0]), uf.find(edge[1])
            if x != y:
                # not a cycle
                uf.union(edge[0], edge[1])
                # print(uf.graph)
            else:
                return edge