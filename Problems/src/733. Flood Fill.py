class Solution:
    """my sol - bfs"""
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        cor = image[sr][sc]
        m, n = len(image), len(image[0])

        def bfs(r, c):

            # out of bound
            if not (0 <= r < m and 0 <= c < n):
                return

            # bfs
            if image[r][c] == cor:
                image[r][c] = newColor
                bfs(r - 1, c)
                bfs(r + 1, c)
                bfs(r, c - 1)
                bfs(r, c + 1)

        if cor != newColor:
            bfs(sr, sc)

        return image