class Solution:
    """my sol under hint, time n^2"""
    def maxPoints(self, points: List[List[int]]) -> int:

        """
        Notes:
            1. duplicate points - use points counter,
                and use dicts to memorize points in line and #points in line separately
            2. accuracy of slopes - use ax + by + c = 0 representation,
                instead of y = ax + b
            3. use functools.reduce and math.gcd:
                2ax + 2by + 2c = 0, and -ax + -by - c situation
        """

        if not points:
            return 0

        points = [tuple(p) for p in points]
        c_point = Counter(points)
        d_line = defaultdict(set)
        d_num = defaultdict(int)

        for p1, p2 in itertools.combinations(points, 2):

            if p1 == p2:
                continue

            x1, y1, x2, y2 = *p1, *p2

            # represent a line by (a, b, c)
            a, b, c = y2 - y1, x1 - x2, x2 * y1 - x1 * y2

            # consider negative case
            if a < 0:
                a, b, c = -a, -b, -c

            # greatest common divisor
            g = reduce(math.gcd, (a, b, c))
            a, b, c = a / g, b / g, c / g

            # add points to this line
            if p1 not in d_line[(a, b, c)]:
                d_line[(a, b, c)].add(p1)
                d_num[(a, b, c)] += c_point[p1]

            if p2 not in d_line[(a, b, c)]:
                d_line[(a, b, c)].add(p2)
                d_num[(a, b, c)] += c_point[p2]

        # if d_num, meaning we checked at least one line
        #   otherwise, all points are duplicate, return #points
        return max(d_num.values()) if len(d_num) >= 1 else len(points)


class Solution(object):
    """online sol"""
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        pointsInLine = {}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1, x2, y2 = *points[i], *points[j]

                a, b, c = y2 - y1, x1 - x2, x2 * y1 - x1 * y2
                if a < 0:
                    a, b, c = -a, -b, -c
                g = reduce(gcd, (a, b, c))
                a, b, c = a / g, b / g, c / g

                line = (a, b, c)
                pointsInLine.setdefault(line, set())
                pointsInLine[line].add(i)
                pointsInLine[line].add(j)

        return max(map(len, pointsInLine.values())) if pointsInLine else len(points)

