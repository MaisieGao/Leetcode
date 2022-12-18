class Solution:
    #首先把六个放到hashmap里
    #如果go through的过程中在key里，stack append
    #如果不在key里，说明是杂的或是另一半。
    #如果stack是empty,说明另一半早了
    #如果stack里有东西，pop stack, 如果hashmap的value 和现在的值不相等，return false
    #完成后如果stack里面有值，return false
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"(":")","[":"]","{":"}"}
        for i in range(len(s)):
            if s[i] in hashmap.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    cur = stack.pop()
                    if hashmap[cur] != s[i]:
                        return False
        if stack:
            return False
        else:
            return True
            