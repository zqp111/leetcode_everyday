#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.data = []


    def push(self, x: int) -> None:
        self.data.append(x)


    def pop(self) -> int:
        if self.empty():
            return None
        return self.data.pop(-1)

    def top(self) -> int:
        if self.empty():
            return None
        return self.data[-1]


    def empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

