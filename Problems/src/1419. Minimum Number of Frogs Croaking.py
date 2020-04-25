class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        cur_wait = {'c': [], 'r': [], 'o': [], 'a': [], 'k': []}
        next_char = {'c': 'r', 'r': 'o', 'o': 'a', 'a': 'k', 'k': 'c'}
        frogs = 0

        for f in croakOfFrogs:

            if f == 'c' and not cur_wait['c']:
                frogs += 1
                cur_wait['r'].append(1)
            elif not cur_wait[f]:
                return -1
            else:
                cur_wait[next_char[f]].append(cur_wait[f].pop())

        return frogs if not cur_wait['r'] and not cur_wait['o'] and not cur_wait['a'] and not cur_wait['k'] else -1



