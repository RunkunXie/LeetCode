class Solution:
    """my sol, 1 attempt, time, implement topo-sort by dfs"""
    def alienOrder(self, words: List[str]) -> str:

        # dfs
        def dfs(graph, v):
            color[v] = 1
            for adj in graph[v]:
                if color[adj] == 0:
                    dfs(graph, adj)
                elif color[adj] == 1:
                    self.invalid = True
            color[v] = 2
            ans.append(v)

        # build graph
        self.invalid = False
        graph = defaultdict(set)
        for w1, w2 in combinations(words, 2):
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    graph[w1[i]].add(w2[i])
                    break
            else:
                if len(w1) > len(w2): self.invalid = True

        # build vertices and their colors (0: unvisited, 1: processing, 2: finished)
        V = set(''.join(words))
        color = {v: 0 for v in V}
        ans = []

        # iterate vertices and dfs
        for v in V:
            if color[v] == 0:
                dfs(graph, v)

        # answer
        ans.reverse()
        return ''.join(ans) if not self.invalid else ""

    """ans, dfs"""
    def alienOrder(self, words: List[str]) -> str:
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)