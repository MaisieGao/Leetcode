class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = collections.defaultdict(int)
        dict2 = collections.defaultdict(int)
        for n in s1:
            dict1[n] += 1
        start = 0
        for end in range(len(s2)):
            dict2[s2[end]] += 1
            print(dict2)
            if dict1 == dict2:
                return True
            #最好用end和固定的length比较大小
            if end >= len(s1)-1:
                dict2[s2[start]] -= 1
                if dict2[s2[start]] == 0:
                    del dict2[s2[start]]
                start += 1
        return False