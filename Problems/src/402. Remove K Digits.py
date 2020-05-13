class Solution:
    """my sol - first attempt, time n"""
    # def removeKdigits(self, num: str, k: int) -> str:
    #
    #     # monotonic queue
    #     mono_q = []
    #     n = len(num)
    #
    #     # special case
    #     if n == k:
    #         return "0"
    #
    #     # one-pass
    #     for char in num:
    #
    #         if k == 0:
    #             mono_q.append(char)
    #             continue
    #
    #         while mono_q and int(mono_q[-1]) > int(char) and k > 0:
    #             mono_q.pop()
    #             k -= 1
    #
    #         mono_q.append(char)
    #
    #     # remove from left
    #     while k > 0:
    #         mono_q.pop()
    #         k -= 1
    #
    #     return str(int("".join(mono_q)))

    """my modified sol - modify based on answer, time n"""
    def removeKdigits(self, num: str, k: int) -> str:

        # monotonic queue
        mono_q = []

        # one-pass
        for char in num:

            while k > 0 and mono_q and int(mono_q[-1]) > int(char):
                mono_q.pop()
                k -= 1

            mono_q.append(char)

        # remove from left
        mono_q = mono_q[:-k] if k else mono_q

        return "".join(mono_q).lstrip('0') or "0"
