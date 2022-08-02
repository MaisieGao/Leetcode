def longestPalindrome(self, s: str) -> str:
        res = ''
        #最长的长度
        resLength = 0

        #odd length
        for i in range(len(s)):
            left, right = i,i
            #当两个值相同，则是回文串
            while left >= 0 and right < len(s) and s[left] == s[right]:
                #比较现在的长度和resLength哪个长
                if right-left+1 > resLength:
                    #最后一个数不算在res里
                    res = s[left:right+1]
                    resLength = right - left + 1
                left -=1
                right +=1
        
        #even length
            left, right = i,i+1
            #当两个值相同，则是回文串
            while left >= 0 and right < len(s) and s[left] == s[right]:
                #比较现在的长度和resLength哪个长
                if right-left+1 > resLength:
                    #最后一个数不算在res里
                    res = s[left:right+1]
                
                    resLength = right - left + 1
                left -=1
                right +=1
        return res