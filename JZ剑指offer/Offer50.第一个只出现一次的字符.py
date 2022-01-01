class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not len(s): return ' '

        seen = dict()
        for i in range(len(s)):
            if seen.get(s[i], None) is not None:
                seen[s[i]] += 1
            else:
                seen[s[i]] = 1
        for key, item in seen.items():
            if item == 1:
                return key
        return ' '