

class Solution:
    """ Test Cases
    "catsanddog"
    ["cat","cats","and","sand","dog"]
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    "aaaaaaa"
    ["aaaa","aa","a"]
    """

    """my dp sol, time n^3"""
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        if not wordDict or not s:
            return []

        wordSet = set(wordDict)
        min_word = min([len(w) for w in wordDict])
        max_word = max([len(w) for w in wordDict])

        @lru_cache(None)
        def dfs(s):

            ns = len(s)
            res = []

            for i in range(min_word, max_word + 1):

                if i > ns:
                    break

                cur_word = s[:i]
                if cur_word in wordSet:

                    if i == ns:
                        res.append(cur_word)
                        return res

                    rest_sentence = dfs(s[i:])
                    if rest_sentence:
                        for rest in rest_sentence:
                            res.append(cur_word + ' ' + rest)
            return res

        return dfs(s)
