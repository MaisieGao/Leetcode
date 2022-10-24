class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        maxLength = 0
        word = collections.defaultdict(int)
        start = 0
        for end in range(len(s)):
            word[s[end]] += 1
            other = end-start+1- max(word.values())
            if other <= k:
                length = end- start + 1
                maxLength = max(length, maxLength)
            
            else:
                word[s[start]] -= 1
                start += 1
        return maxLength