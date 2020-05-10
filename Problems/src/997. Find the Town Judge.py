class Solution:
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


