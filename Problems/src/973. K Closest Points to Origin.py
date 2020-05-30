class Solution:
    """my sort sol, time nlogn"""
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:K]

    """my heap sol, time nlogk"""
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        ans = []

        for p in points:

            if len(ans) < K:
                heappush(ans, (- p[0] ** 2 - p[1] ** 2, p))

            else:
                prev_min_distance, prev_p = ans[0]
                if p[0] ** 2 + p[1] ** 2 < - prev_min_distance:
                    heappushpop(ans, (- p[0] ** 2 - p[1] ** 2, p))

        return [p for d, p in ans]

    """online heap sol, time nlogk"""
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)

class Solution(object):
    """ans, quick sort, average time n, worst time n^2"""
    def kClosest(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]