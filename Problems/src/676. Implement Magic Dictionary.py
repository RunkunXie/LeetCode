class MagicDictionary:
    """my sol - using Trie, first attempt, speed 97%, space 100%"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.is_key = False

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:

            # insert word into trie
            curr = self
            for w in word:
                if w not in curr.child:
                    curr.child[w] = MagicDictionary()
                curr = curr.child[w]

            # mark word ending key
            curr.is_key = True

    def search(self, word: str, modified: bool = False) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        curr = self

        # base case
        if not word:
            return modified and curr.is_key

        # get first char
        w = word[0]

        # if already modified, just find if there is matching child and go there
        if modified:
            if w not in curr.child:
                return False
            return curr.child[w].search(word[1:], True)

        # if not modified, iterate every children
        else:
            ans = False

            for k in curr.child.keys():
                # go to matching child - still unmodified
                if w == k:
                    ans = ans or curr.child[k].search(word[1:], False)

                # go to unmatched child - modified
                else:
                    ans = ans or curr.child[k].search(word[1:], True)

            return ans

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

