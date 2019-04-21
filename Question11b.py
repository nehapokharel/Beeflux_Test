class Count:
    def __init__(self, low=0, high=10):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self): 
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
    def print(self):
            print(c)

c = Count()
c.print()
