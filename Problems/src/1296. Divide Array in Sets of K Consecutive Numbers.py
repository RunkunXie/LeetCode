class Solution:
    """my sol under hint - first attempt"""
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        n_set, cur_set = len(nums) / k, 0
        c = Counter(nums)

        for key, val in sorted(c.items(), key=lambda x: x[0]):

            # start from smallest number
            if c[key] > 0:
                new_set = c[key]
                c[key] = 0
            else:
                continue

            # find if new consecutive sets exist
            for num in range(key + 1, key + k):
                if c[num] >= new_set:
                    c[num] -= new_set
                else:
                    return False

            # if exist
            cur_set += new_set
            if cur_set == n_set:
                return True

        return cur_set == n_set