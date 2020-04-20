class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        if not nums:
            return 1

        cur_sum = 0
        min_sum = 100
        for num in nums:
            cur_sum += num
            min_sum = min(min_sum, cur_sum)
            print(cur_sum, min_sum)

        return max(- min_sum + 2, 1)

#
# class Solution:
#     def getHappyString(self, n: int, k: int) -> str:
#
#         count = 0
#         h_set = {'a', 'b', 'c'}
#
#         s = ""
#         cur_len = 0
#         self.cur_num = 0
#
#         def bc(s, cur_len):
#
#             if cur_len < n:
#
#                 if s == "":
#                     ava_set = h_set
#                 else:
#                     ava_set = h_set.difference(s[-1])
#
#                 for char in sorted(ava_set):
#                     s += char
#                     cur_len += 1
#                     bc(s, cur_len)
#
#                     s = s[:-1]
#                     cur_len -= 1
#
#             elif cur_len == n:
#                 self.cur_num += 1
#                 if self.cur_num == k:
#                     self.ans = s
#
#         bc(s, cur_len)
#         if self.ans:
#             return self.ans
#
#         return ""
#
# print(Solution().getHappyString(1, 3))


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        n = len(s)
        pos = 0
        self.count = 0

        def bc(pos):

            if pos < n:

                for i in range(pos, n):
                    if int(s[pos:i + 1]) <= k and (i == n - 1 or s[i + 1] != '0'):
                        bc(i + 1)

            elif pos == n:
                self.count += 1

        bc(pos)
        return self.count % (10 ** 9 + 7)

print(Solution().numberOfArrays('1000', 10000), 1)
print(Solution().numberOfArrays('1317', 2000), 8)
print(Solution().numberOfArrays('1234567890', 90), 34)
print(Solution().numberOfArrays('2553462832281151811513004352253111', 456), 34)
