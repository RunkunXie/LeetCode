"""Weekly Contest 189 - Q4"""


class Solution:
    """my sol under hint, time n^3"""
    def numPoints(self, points: List[List[int]], r: int) -> int:

        n = len(points)
        ans = 0

        for i in range(n - 1):
            for j in range(i + 1, n):

                c1, c2, hasCircle = self.findCircle(points[i], points[j], r)
                if hasCircle:
                    ans = max(ans, self.enclosedPoints(c1, points, r))
                    ans = max(ans, self.enclosedPoints(c2, points, r))

        return max(ans, 1)

    @staticmethod
    def enclosedPoints(c, points, r):

        ans = 0
        for p in points:
            if math.sqrt((p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2) <= r + 1e-5:
                ans += 1
        return ans

    @staticmethod
    def findCircle(p1, p2, r):

        x1, y1, x2, y2 = *p1, *p2

        q = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if q > 2 * r:
            return 0, 0, False

        y3 = (y1 + y2) / 2
        x3 = (x1 + x2) / 2

        xa = x3 + math.sqrt(r ** 2 - (q / 2) ** 2) * (y1 - y2) / q
        ya = y3 + math.sqrt(r ** 2 - (q / 2) ** 2) * (x2 - x1) / q

        xb = x3 - math.sqrt(r ** 2 - (q / 2) ** 2) * (y1 - y2) / q
        yb = y3 - math.sqrt(r ** 2 - (q / 2) ** 2) * (x2 - x1) / q

        return [xa, ya], [xb, yb], True

    """online sol, N^3"""
    def numPoints(self, points: List[List[int]], r: int) -> int:

        res = 1
        for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) / 4.0
            if d > r * r: continue
            x0 = (x1 + x2) / 2.0 + (y2 - y1) * (r * r - d) ** 0.5 / (d * 4) ** 0.5
            y0 = (y1 + y2) / 2.0 - (x2 - x1) * (r * r - d) ** 0.5 / (d * 4) ** 0.5
            res = max(res, sum((x - x0) ** 2 + (y - y0) ** 2 <= r * r + 0.00001 for x, y in points))

            x0 = (x1 + x2) / 2.0 - (y2 - y1) * (r * r - d) ** 0.5
            y0 = (y1 + y2) / 2.0 + (x2 - x1) * (r * r - d) ** 0.5
            res = max(res, sum((x - x0) ** 2 + (y - y0) ** 2 <= r * r + 0.00001 for x, y in points))
        return res

    """best one: online angular sweep sol - time n^2 * logn"""
    def numPoints(self, points: List[List[int]], r: int) -> int:
        ans = 1
        for x, y in points:
            angles = []
            for x1, y1 in points:
                if (x1 != x or y1 != y) and (d:=sqrt((x1-x)**2 + (y1-y)**2)) <= 2*r:
                    angle = atan2(y1-y, x1-x)
                    delta = acos(d/(2*r))
                    angles.append((angle-delta, +1)) #entry
                    angles.append((angle+delta, -1)) #exit
            angles.sort(key=lambda x: (x[0], -x[1]))
            val = 1
            for _, entry in angles:
                ans = max(ans, val := val+entry)
        return ans