class RingBuffer:
    def __init__(self, capacity):
        self.max = capacity
        self.data = []

    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.max:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    class __Full:
        def append(self, item):
            self.data[self.cur] = item
            self.cur = (self.cur+1) % self.max

        def get(self):
            return self.data[self.cur:]+self.data[:self.cur]

