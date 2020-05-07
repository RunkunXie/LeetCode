class Solution:
    """my sol, time n^2"""
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return None

        i, j, m, n = 0, 0, len(matrix), len(matrix[0])
        direction = {'right': 'down', 'down': 'left',
                     'left': 'up', 'up': 'right'}

        cur_dir = 'right'
        ans = []
        total_element = m * n
        count = 0

        while count < total_element:

            # direction
            if cur_dir == 'right' and j < n - 1 and matrix[i][j + 1] is not None:
                pass
            elif cur_dir == 'down' and i < m - 1 and matrix[i + 1][j] is not None:
                pass
            elif cur_dir == 'left' and j > 0 and matrix[i][j - 1] is not None:
                pass
            elif cur_dir == 'up' and i > 0 and matrix[i - 1][j] is not None:
                pass
            else:
                cur_dir = direction[cur_dir]

            # move
            ans.append(matrix[i][j])
            matrix[i][j] = None
            count += 1

            if cur_dir == 'right':
                j += 1
            elif cur_dir == 'down':
                i += 1
            elif cur_dir == 'left':
                j -= 1
            elif cur_dir == 'up':
                i -= 1

        return ans
