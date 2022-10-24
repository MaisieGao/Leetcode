class Solution:
    def validPalindrome(self, s: str) -> bool:
        #证明是回文子串
        def palindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True


        left = 0
        right = len(s) -1
        #如果左边右边相等，那么往后看
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            #如果不等，看左边右边去掉一个是否是回文子串
            else:
                if palindrome(s[left:right]) or palindrome(s[left+1:right+1]):
                    return True
                else:
                    return False
        return True
                    
