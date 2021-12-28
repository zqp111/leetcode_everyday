class CQueue:

    def __init__(self):
        self.stack1= []
        self.stack2= []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)


    def deleteHead(self) -> int:
        if not self.stack1 and not self.stack2:
            return -1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
        return self.stack2.pop(-1)


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()