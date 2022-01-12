#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.isEnd = False
        self.next = [None]*26


    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            index = ord(c) - ord('a')
            if cur.next[index] is None:
                cur.next[index] = Trie()
            cur = cur.next[index]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            index = ord(c) - ord('a')
            if cur.next[index] is None: return False
            cur = cur.next[index]
        return cur.isEnd


    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            index = ord(c) - ord('a')
            if cur.next[index] is None: return False
            cur = cur.next[index]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

