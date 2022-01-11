#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#
import collections

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = collections.OrderedDict()


    def get(self, key: int) -> int:
        if key not in self.queue: return -1
        self.queue.move_to_end(key)
        return self.queue[key]


    def put(self, key: int, value: int) -> None:
        if len(self.queue) == self.capacity and key not in self.queue:
            self.queue.popitem(last=False)
        self.queue[key] = value
        self.queue.move_to_end(key)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

