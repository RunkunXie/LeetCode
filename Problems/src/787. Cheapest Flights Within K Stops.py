class Solution:
    """online Dijkstra+heap sol, time (v+e)logv"""
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, K + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

    """my dfs sol, 1sta attempt, slow"""
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        graph = defaultdict(list)
        for f in flights:
            graph[f[0]].append(f[1:])
        visited = [False] * n
        self.ans = float("inf")

        def dfs(node=src, dst=dst, K=K, price=0):

            if node == dst:
                self.ans = min(self.ans, price)
                return

            if K == -1 or price > self.ans:
                return

            for adj, w in graph[node]:
                if not visited[adj]:
                    visited[adj] = True
                    dfs(adj, dst, K - 1, price + w)
                    visited[adj] = False

        dfs()
        return self.ans if self.ans != float("inf") else -1