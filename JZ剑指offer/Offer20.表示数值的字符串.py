class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        # print(s)
        splited = s.split('e')
        if len(splited) == 1:
            splited = splited[0].split('E')
        # print(splited)
        # print(self.isInteger(splited[1]))

        if len(splited) == 1:
            return (len(splited[0])>0 and \
                (self.isInteger(splited[0]) or self.isFloat(splited[0])))

        elif len(splited) == 2:
            return (len(splited[0])>0 and \
                (self.isInteger(splited[0]) or self.isFloat(splited[0]))) \
                and (len(splited[1])>0 and self.isInteger(splited[1]))
        else:
            return False

    def isInteger(self, s: str) -> bool:
        if not len(s): return True
        index= 0
        if s[0] == '-' or s[0] == '+':
            if len(s) == 1: return False
            index = 1
            
        for i in range(index, len(s)):
            if not s[i].isdigit():
                return False
        return True

    def isFloat(self, s: str) -> bool:
        if not len(s): return True
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
            if not len(s): return False
        splited = s.split('.')
        if len(splited) > 2: return False
        if not len(splited[0]) and not len(splited[1]): return False
        for i in range(len(splited[0])) :
            if not s[i].isdigit():
                return False
        
        for i in range(len(splited[0])+1, len(s)) :
            if not s[i].isdigit():
                return False
        return True