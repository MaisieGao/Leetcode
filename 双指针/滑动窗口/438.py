class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        word=collections.defaultdict(int)
        res = []
        start = 0
        dict = collections.defaultdict(int)
        for n in p:
            dict[n] += 1
        for end in range(len(s)):
            word[s[end]]+= 1
            #pair value对相同就行，key的Order不同也算相等
            if word == dict:
                res.append(start)
            # 如果题目的窗口长度固定：用一个if语句判断一下当前窗口长度是否达到了限定长度 
            # 如果达到了，窗口左指针前移一个单位，从而保证下一次右指针右移时，窗口长度保持不变, 
            #所以要缩小一位以便未来再放大
            if end - start + 1>=len(p):
                word[s[start]] -= 1
                if word[s[start]] == 0:
                    del word[s[start]]
                start += 1
        return res