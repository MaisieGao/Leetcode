def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = {}
    for s in strs:
        a = "".join(sorted(s))
        if a not in res:
            res[a] = [s]
        else:
            res[a].append(s)
    return res.values()
#用hashmap来append data