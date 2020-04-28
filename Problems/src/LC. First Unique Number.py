from collections import OrderedDict


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dict = OrderedDict()
        self.not_unique = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.dict:
            return next(iter(self.dict))
        return -1

    def add(self, value: int) -> None:
        if value not in self.dict:
            if value not in self.not_unique:
                self.dict[value] = 1
        else:
            self.dict.pop(value)
            self.not_unique.add(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)