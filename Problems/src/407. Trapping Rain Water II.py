class Solution:
    """my 1st wrong attempt"""
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        l, r, u, d, ans = [], [], [], [], 0
        m, n = len(heightMap), len(heightMap[0])

        for i in range(m):
            if i == 0:
                u.append(heightMap[i].copy())
            else:
                u.append([max(heightMap[i][j], u[-1][j]) for j in range(n)])

        for i in range(m - 1, -1, -1):
            if i == m - 1:
                d.append(heightMap[i].copy())
            else:
                d.append([max(heightMap[i][j], d[-1][j]) for j in range(n)])
        d = list(reversed(d))

        for i in range(m):
            tmp = heightMap[i].copy()
            for j in range(1, n):
                tmp[j] = max(tmp[j], tmp[j - 1])
            l.append(tmp)

        for i in range(m):
            tmp = heightMap[i].copy()
            for j in range(n - 2, -1, -1):
                tmp[j] = max(tmp[j], tmp[j + 1])
            r.append(tmp)

        for i in range(m):
            for j in range(n):
                if 0 < i < m - 1 and 0 < j < n - 1:
                    h = min(l[i][j - 1], r[i][j + 1], u[i - 1][j], d[i + 1][j])
                    ans += max(0, h - heightMap[i][j])
        return ans




