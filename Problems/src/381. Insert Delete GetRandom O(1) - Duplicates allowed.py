class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(set)
        self.l = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.d[val].add(len(self.l))
        self.l.append(val)
        return len(self.d[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """

        if len(self.d[val]) > 0:
            # remove val from d
            idx = self.d[val].pop()

            # change index of last element
            self.d[self.l[-1]].add(idx)
            self.d[self.l[-1]].remove(len(self.l) - 1)

            # exchange last element with val
            self.l[idx], self.l[-1] = self.l[-1], self.l[idx]

            # remove val from l and d
            self.l.pop()

            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if self.l: return random.choice(self.l)

    # Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()