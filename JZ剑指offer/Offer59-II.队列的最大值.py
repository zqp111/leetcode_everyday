class MaxQueue:

    def __init__(self):
        self.queue = []
        self.maxValue = []


    def max_value(self) -> int:
        return self.maxValue[0] if self.maxValue else -1


    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while  self.maxValue and self.maxValue[-1] < value:
            self.maxValue.pop(-1)
        self.maxValue = self.maxValue + [value]*(len(self.queue)-len(self.maxValue))

    def pop_front(self) -> int:
        if self.maxValue:
            self.maxValue.pop(0)
            return self.queue.pop(0)
        return -1



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()