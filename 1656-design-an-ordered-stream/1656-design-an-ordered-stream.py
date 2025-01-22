class OrderedStream:

    def __init__(self, n: int):
        self.array = [None] * n
        self.counter = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey - 1] = value
        results = []
        size = len(self.array)
        while self.counter < size and self.array[self.counter] != None:
            results.append(self.array[self.counter])
            self.counter += 1
        return results
 


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)