class Solution:
    """my quick-find sol, 2nd attempt, TLE, time mn*mn"""
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        ans, count = [0], 0
        island_to_set = {}
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # make all islands in set id2 to id1, time #set <= mn
        def union(id1, id2):
            for k, v in island_to_set.items():
                if v == id2:
                    island_to_set[k] = id1

        # time #position <= mn
        for set_id, (i, j) in enumerate(positions):

            # repeated island
            if (i, j) in island_to_set:
                ans.append(ans[-1])
                continue

            # new island
            island_to_set[(i, j)] = set_id
            count += 1

            # union nearby islands, time 4 * time union <= 4mn
            for di, dj in direction:
                newi, newj = i + di, j + dj
                if 0 <= newi < m and 0 <= newj < n and (newi, newj) in island_to_set and island_to_set[
                    (newi, newj)] != set_id:
                    union(set_id, island_to_set[(newi, newj)])
                    count -= 1

            # acount
            ans.append(count)

        return ans[1:]

    """online Quick-Union with Path Compression sol, time mn log(mn)"""
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        def find(x):
            while x in pa:
                if pa[x] in pa:  # path compress
                    pa[x] = pa[pa[x]]
                x = pa[x]
            return x

        def union(x, y):
            pax, pay = find(x), find(y)
            if pax == pay:  # union fail,has been unioned.
                return False
            pa[pax] = pay
            return True

        seen, pa, res, count = set(), {}, [], 0
        for x, y in positions:  # connect with neighbor val==1,if union success,means one island disappear.
            if (x, y) not in seen:
                seen.add((x, y))
                count += 1
                for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (i, j) in seen and union((i, j), (x, y)):
                        count -= 1
            res.append(count)
        return res

    """
        best runtime algorithm in theory: 
        Weighted Quick-Union with Path Compression (WQUPC), time mn log*(mn)
    """

"""
    my WQUPC sol
    use path compression is simpler and enough
"""
class UnionFind2D:

    def __init__(self):
        self.id = {}
        self.sz = {}  # add weight
        self.count = 0

    def add(self, i, j):
        self.id[i, j] = i, j
        self.sz[i, j] = 1  # add weight
        self.count += 1

    def root(self, i, j):
        while (i, j) != self.id[i, j]:
            self.id[i, j] = self.id[self.id[i, j]]  # add path compression
            i, j = self.id[i, j]
        return i, j

    def union(self, i, j, i2, j2):
        r, r2 = self.root(i, j), self.root(i2, j2)
        if r != r2:
            if self.sz[r] < self.sz[r2]:  # add weight
                r, r2 = r2, r
            self.id[r2] = r
            self.sz[r] += self.sz[r2]  # add weight
            self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        ans = []
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        u = UnionFind2D()

        for i, j in positions:
            if (i, j) not in u.id:
                u.add(i, j)
                for di, dj in direction:
                    newi, newj = i + di, j + dj
                    if 0 <= newi < m and 0 <= newj < n and (newi, newj) in u.id:
                        u.union(i, j, newi, newj)
            ans.append(u.count)

        return ans











