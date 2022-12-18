class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hashmap1 = {}
        for i in range(len(s1)):

            hashmap1[s1[i]] = hashmap1.get(s1[i],0)+1
        hashmap2 = {}
        start = 0
        for end in range(len(s2)):
            hashmap2[s2[end]] = hashmap2.get(s2[end],0)+1
            if end - start + 1 > len(s1):
                hashmap2[s2[start]] -= 1
                if hashmap2[s2[start]] == 0:
                    del hashmap2[s2[start]]
                start += 1
            if hashmap1 == hashmap2:
                return True
        return False
            