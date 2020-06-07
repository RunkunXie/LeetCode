class BrowserHistory:
    """my sol, visit time n, back/forward time 1"""
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.idx = 0
        self.last = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.idx + 1]
        self.history.append(url)

        self.idx += 1
        self.last = self.idx

    def back(self, steps: int) -> str:
        if self.idx - steps >= 0:
            self.idx -= steps
        else:
            self.idx = 0
        return self.history[self.idx]

    def forward(self, steps: int) -> str:
        if self.idx + steps <= self.last:
            self.idx += steps
        else:
            self.idx = self.last
        return self.history[self.idx]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)