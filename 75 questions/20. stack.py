class Solution:
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
            