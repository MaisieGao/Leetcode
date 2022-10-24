def isPalindrome(self, s: str) -> bool:
    res = []
    for n in s:
        if n.isalnum():
            res.append(n.lower())
    return res == res[::-1]
