def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        #或者是vowel = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        vowel = set('aeiouAEIOU')
        s = list(s)
        while left < right:
            if s[left] in vowel:
                #前进到遇到元音为止
                while s[right] not in vowel:
                    right -= 1
                #遇到元音换位置
                s[left], s[right] = s[right], s[left]
                #换完之后left和right同时移动
                left += 1
                right -= 1
            #left不是元音时移动left
            else:
                left += 1
        return "".join(s)

        O(n)