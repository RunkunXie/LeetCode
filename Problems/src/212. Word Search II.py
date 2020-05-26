class Trie:

    def __init__(self):

        self.child = {}
        self.is_key = False

    def insert(self, word: str) -> None:

        curr = self

        for w in word:
            if w not in curr.child:
                curr.child[w] = Trie()
            curr = curr.child[w]

        curr.is_key = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # build trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        # init
        m, n = len(board), len(board[0])
        direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = set()

        # dfs search
        def dfs(i, j, trie, cur_word="", used=set()):

            # if out of board
            if not (0 <= i < m and 0 <= j < n) or (i, j) in used:
                return

            # current char
            cur_char = board[i][j]
            cur_word += cur_char

            # if not match, return
            if cur_char not in trie.child:
                return

            # if match, continue dfs and add used location
            trie = trie.child[cur_char]
            used.add((i, j))

            # if word ends
            if trie.is_key:
                ans.add(cur_word)

            # dfs 4 directions
            for d in direct:
                dfs(i + d[0], j + d[1], trie, cur_word, used)

            # remove used location
            used.remove((i, j))

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "", set())

        return list(ans)



