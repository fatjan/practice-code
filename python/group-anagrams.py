from collections import defaultdict


def group_anagrams(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26 # a ... z

        for c in s:
            count[ord(c) - ord("a")] += 1
        
        print(count)
        res[tuple(count)].append(s)
    
    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))
