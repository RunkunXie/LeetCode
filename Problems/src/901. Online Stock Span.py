class StockSpanner:
    """my sol, 1 attempt, time n"""
    def __init__(self):
        self.s_price = []
        self.s_span = []

    def next(self, price: int) -> int:
        new_span = 1
        while self.s_price and self.s_price[-1] <= price:
            self.s_price.pop()
            new_span += self.s_span.pop()

        self.s_price.append(price)
        self.s_span.append(new_span)

        return new_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)