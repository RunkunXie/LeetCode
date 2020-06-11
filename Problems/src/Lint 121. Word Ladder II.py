from collections import defaultdict, deque


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    """my bfs sol, save path in deque"""
    def findLadders(self, start, end, dict):
        # write your code here

        # build graph, time N * M * M
        graph = defaultdict(set)
        for v in dict.union({start, end}):
            for i in range(len(v)):
                generic_form = v[:i] + "*" + v[i + 1:]
                graph[generic_form].add(v)

        # init BFS
        visited_depth = {start: 1}  # track BFS depth
        dq = deque([[start, [start]]])  # track current vertice and path
        self.min_depth = float("inf")
        self.ans = []

        # BFS, time N * M * (M + 26M)
        while dq:
            v, path = dq.popleft()
            if visited_depth[v] > self.min_depth:
                return self.ans
            if v == end:
                self.ans.append(path)
                self.min_depth = visited_depth[v]
                continue
            for i in range(len(v)):
                generic_form = v[:i] + "*" + v[i + 1:]
                for v_next in graph[generic_form]:
                    if (v_next not in visited_depth or
                            visited_depth[v_next] == visited_depth[v] + 1):  # allow revisit when depth is add one
                        dq.append([v_next, path + [v_next]])
                        visited_depth[v_next] = visited_depth[v] + 1
        return self.ans

