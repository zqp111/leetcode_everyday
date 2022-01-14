#
# @lc app=leetcode.cn id=2043 lang=python3
#
# [2043] 简易银行系统
#

# @lc code=start
from re import S


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance


    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.isExist(account1) or not self.isExist(account2): return False

        if self.withdraw(account1, money):
            self.deposit(account2, money)
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if not self.isExist(account): return False
        self.balance[account-1] += money
        return True

    def isExist(self, account: int):
        if account > len(self.balance): return False
        return True


    def withdraw(self, account: int, money: int) -> bool:
        if not self.isExist(account): return False
        if self.balance[account-1] >= money:
            self.balance[account-1] -= money
            return True
        return False



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
# @lc code=end

