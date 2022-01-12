#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#



# @lc code=start
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        tmp = self.head
        for _ in range(index):
            if tmp is None:
                return -1
            tmp = tmp.next
        if tmp is None: return -1
        return tmp.val


    def addAtHead(self, val: int) -> None:
        tmp = Node(val)
        tmp.next = self.head
        self.head = tmp


    def addAtTail(self, val: int) -> None:
        tail = Node(val)
        if self.head is None:
            self.head = tail
            return
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = tail
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            return self.addAtHead(val)
        tmp = self.head
        for _ in range(index-1):
            if tmp is None:
                return -1
            tmp = tmp.next
        if tmp is None:
            return -1
        newNode = Node(val)
        newNode.next = tmp.next
        tmp.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return -1
        if index == 0 and self.head is not None:
            self.head = self.head.next
            return 1
        tmp = self.head
        for _ in range(index-1):
            if tmp is None:
                return -1
            tmp = tmp.next
        if tmp is None or tmp.next is None:
            return -1
        tmp.next = tmp.next.next
        return 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

