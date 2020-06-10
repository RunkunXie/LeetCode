import itertools
import collections


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    """my sol, 2nd attempt, bidirectional dfs, best in time complexity"""
    def ladderLength(self, start, end, dict):
        # write your code here

        # build graph, time N * M * M
        graph = defaultdict(set)
        for v in dict.union({start, end}):
            for i in range(len(v)):
                generic_form = v[:i] + "*" + v[i + 1:]
                graph[generic_form].add(v)

        # init BFS
        visited_depth = {start: 1}  # track BFS depth
        dq = deque([start])
        visited_depth_end = {end: 1}
        dq_end = deque([end])

        # BFS function, time N * M * (M + 26M)
        def visit_one_step(visited_depth, dq, visited_depth_other):
            if dq:
                v = dq.popleft()
                if v in visited_depth_other:
                    return visited_depth[v] + visited_depth_other[v] - 1
                for i in range(len(v)):
                    generic_form = v[:i] + "*" + v[i + 1:]
                    for v_next in graph[generic_form]:
                        if v_next not in visited_depth:
                            dq.append(v_next)
                            visited_depth[v_next] = visited_depth[v] + 1
            return 0

        # bidirectional BFS
        while dq and dq_end:
            ans = visit_one_step(visited_depth, dq, visited_depth_end)
            if ans: return ans
            ans = visit_one_step(visited_depth_end, dq_end, visited_depth)
            if ans: return ans

        return ans

    """my dfs sol, 2nd attempt, time NMM, build BFS in function -> build bidirectional BFS"""
    def ladderLength(self, start, end, dict):
        # write your code here

        # build graph, time N * M * M
        graph = defaultdict(set)
        for v in dict.union({start, end}):
            for i in range(len(v)):
                generic_form = v[:i] + "*" + v[i + 1:]
                graph[generic_form].add(v)

        # BFS, time N * M * (M + 26M)
        visited_depth = {start: 1}  # track BFS depth
        dq = deque([start])

        def visit_one_step(visited_depth, dq):
            if dq:
                v = dq.popleft()
                if v == end:
                    return visited_depth[v]
                for i in range(len(v)):
                    generic_form = v[:i] + "*" + v[i + 1:]
                    for v_next in graph[generic_form]:
                        if v_next not in visited_depth:
                            dq.append(v_next)
                            visited_depth[v_next] = visited_depth[v] + 1
            return 0

        while dq:
            ans = visit_one_step(visited_depth, dq)
            if ans: return ans
        return ans

    """my dfs sol, 2nd attempt, time NMM"""
    def ladderLength(self, start, end, dict):
        # write your code here

        # build graph, time N * M * M
        graph = defaultdict(set)
        for v in dict.union({start, end}):
            for i in range(len(v)):
                generic_form = v[:i] + "*" + v[i + 1:]
                graph[generic_form].add(v)

        # BFS, time N * M * (M + 26M)
        visited_depth = {start: 1}  # track BFS depth
        dq = deque([start])
        while dq:
            v = dq.popleft()
            if v == end:
                return visited_depth[v]
            for i in range(len(v)):
                generic_form = v[:i] + "*" + v[i + 1:]
                for v_next in graph[generic_form]:
                    if v_next not in visited_depth:
                        dq.append(v_next)
                        visited_depth[v_next] = visited_depth[v] + 1
        return 0

    """my naive bfs sol, 1st attempt, TLE, time NNM"""
    def ladderLength(self, start, end, dict):
        # write your code here

        # check if it possible to transfer, time len(word) = M
        def trans(w1, w2):
            num = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    num += 1
                if num > 1:
                    return False
            return True

        if trans(start, end):
            return 2

        # build graph, time N^2*M
        graph = collections.defaultdict(set)
        for v1, v2 in itertools.combinations(dict, 2):
            if trans(v1, v2):
                graph[v1].add(v2)
                graph[v2].add(v1)

        for v in dict:
            if trans(start, v):
                graph[v].add(start)
                graph[start].add(v)
            if trans(end, v):
                graph[v].add(end)
                graph[end].add(v)

        # BFS, time N * 26M
        visited = {v: False for v in graph.keys()}
        depth = {v: 0 for v in graph.keys()}
        dq = collections.deque([start])
        depth[start] = 1
        visited[start] = True
        while dq:
            v = dq.popleft()
            if v == end:
                break
            for v_next in graph[v]:
                if not visited[v_next]:
                    dq.append(v_next)
                    depth[v_next] = depth[v] + 1
                    visited[v_next] = True

        return depth[end] if depth[end] != 0 else 0






