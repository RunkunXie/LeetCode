from collections import deque


class Solution:
    """my bfs sol, first attempt, need optimized"""

    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        next_rot = []
        fresh_num = 0
        time = 0

        # count fresh number and location of rot ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_num += 1
                elif grid[i][j] == 2:
                    next_rot.append([i, j])

        # if no fresh and no rot
        if fresh_num == 0:
            return 0

        # if have rot, loop to see if all fresh can turn rot
        while next_rot:

            if fresh_num == 0:
                return time

            prev_rot, next_rot = next_rot, []
            for i, j in prev_rot:
                if i + 1 < m and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    fresh_num -= 1
                    next_rot.append([i + 1, j])
                if j + 1 < n and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    fresh_num -= 1
                    next_rot.append([i, j + 1])
                if i > 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    fresh_num -= 1
                    next_rot.append([i - 1, j])
                if j > 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    fresh_num -= 1
                    next_rot.append([i, j - 1])

            time += 1
            print(time, grid)

        # else, return -1
        return -1


class Solution:
    """ans, bfs"""

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1
