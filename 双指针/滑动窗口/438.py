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
            # 到了长度就先减一个，然后再加一个，然后再check是不是相同的
            while end - start + 1>=len(p):
                word[s[start]] -= 1
                if word[s[start]] == 0:
                    del word[s[start]]
                start += 1
        return res