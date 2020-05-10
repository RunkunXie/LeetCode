class Solution:
    """my sol, 1st attempt, time E + V"""
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if N == 1:
            return 1

        trusted = defaultdict(set)
        all_ppl = set(range(1, N + 1))
        not_judge = set()
        judge = []

        for x, y in trust:
            trusted[y].add(x)
            not_judge.add(x)

        for ppl, t in trusted.items():
            if ppl not in not_judge and len(all_ppl - t) == 1 and ppl in all_ppl - t:
                judge.append(ppl)

        return judge[0] if len(judge) == 1 else -1

    """answer 1 - graph approach"""
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1

        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(1, N + 1):
            if indegree[i] == N - 1 and outdegree[i] == 0:
                return i
        return -1

    """ans 2, best approach"""
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if len(trust) < N - 1:
            return -1

        trust_scores = [0] * (N + 1)

        for a, b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1

        for i, score in enumerate(trust_scores[1:], 1):
            if score == N - 1:
                return i
        return -1
