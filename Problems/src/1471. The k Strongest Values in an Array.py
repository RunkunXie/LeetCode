class Solution:
    """my sol time n"""
    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        arr, ans, start, end = sorted(arr), [], 0, len(arr) - 1
        m, m_idx = arr[end // 2], end // 2

        while k > 0:

            if arr[end] - m >= m - arr[start]:
                ans.append(arr[end])
                end -= 1
            else:
                ans.append(arr[start])
                start += 1

            k -= 1

        return ans



