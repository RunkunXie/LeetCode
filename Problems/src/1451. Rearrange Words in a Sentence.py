"""Weekly Contest 189 - Q2"""


class Solution:
    """my sort sol - 1 attempt, time n(char) + n(word)*log(n(word))"""
    # def arrangeWords(self, text: str) -> str:
    #
    #     text = text.lower()
    #     words = []
    #
    #     cur_len = 0
    #     cur_word = ""
    #
    #     for i in range(len(text)):
    #
    #         if text[i] == " ":
    #             words.append([cur_word, cur_len])
    #
    #             cur_len = 0
    #             cur_word = ""
    #
    #         else:
    #             cur_word += text[i]
    #             cur_len += 1
    #
    #     words.append([cur_word, cur_len])
    #
    #     words = sorted(words, key=lambda x: x[1])
    #     words[0][0] = words[0][0][0].upper() + words[0][0][1:]
    #
    #     return " ".join([w[0] for w in words])

    """online sol"""
    def arrangeWords(self, text: str) -> str:

        res = sorted([w.lower() for w in text.split()], key=len)
        res = [res[0].capitalize()] + res[1:]
        return ' '.join(res)
