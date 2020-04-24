class Solution:
    """
    online dp sol - state machine thinking!
    time n, space 1
    """
    def maxProfit(self, prices: List[int]) -> int:
        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, notHold, notHold_cooldown = max(
                hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        return max(notHold, notHold_cooldown)
