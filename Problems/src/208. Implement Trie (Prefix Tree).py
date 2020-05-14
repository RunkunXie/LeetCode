class Trie:
    """my sol - first attempt, time m"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = {}
        self.is_key = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self
        while word:
            char = word[0]
            word = word[1:]
            if char in curr.next:
                curr = curr.next[char]
            else:
                curr.next[char] = Trie()
                curr = curr.next[char]
                curr.val = char

        curr.is_key = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self
        while word:
            char = word[0]
            word = word[1:]
            if char in curr.next:
                curr = curr.next[char]
            else:
                return False

        return curr.is_key

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self
        while prefix:
            char = prefix[0]
            prefix = prefix[1:]
            if char in curr.next:
                curr = curr.next[char]
            else:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Trie:
    """my modified sol"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.is_key = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self

        for w in word:
            if w not in curr.child:
                curr.child[w] = Trie()
            curr = curr.child[w]

        curr.is_key = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self

        for w in word:
            if w not in curr.child:
                return False
            curr = curr.child[w]

        return curr.is_key

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self

        for w in prefix:
            if w not in curr.child:
                return False
            curr = curr.child[w]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)