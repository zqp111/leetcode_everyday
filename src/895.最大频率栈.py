#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

# @lc code=start
class FreqStack:

    def __init__(self):
        self.countDict = dict()
        self.stackDict = dict()
        self.topCount = 0


    def push(self, val: int) -> None:
        if self.countDict.get(val, None) is None:
            self.countDict[val] = 1
        else:
            self.countDict[val] += 1

        self.topCount = max(self.countDict[val], self.topCount)
        if self.stackDict.get(self.countDict[val], None) is None:
            self.stackDict[self.countDict[val]] = [val]
        else:
            self.stackDict[self.countDict[val]].append(val)


    def pop(self) -> int:
        if not self.countDict:
            return None
        val = self.stackDict[self.topCount].pop(-1)
        self.countDict[val] -= 1
        if not self.stackDict[self.topCount]:
            self.topCount -= 1
        return val
        



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

