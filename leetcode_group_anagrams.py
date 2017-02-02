#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 29, 2016 by 12:58 AM

'''
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
import collections
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def groupAnagrams(strs):
    rr = [''.join(sorted(i)) for i in strs]
    set_rr = f7(rr)
    return [[i for i in range(len(rr)) if item1 == rr[i]] for item1 in set_rr]


def anagrams( strs):
    dict = {}
    for word in strs:
        sortedword = ''.join(sorted(word))
        dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
    res = []
    for item in dict:
        if len(dict[item]) >= 2:
            res += dict[item]
    return res

# if __name__ == "__main__":
#     assert groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['nat', 'tan'], ['bat'],
#                                                                                     ['ate', 'eat', 'tea']]


def groupAnagrams( strs):
    ans = []
    dic = collections.defaultdict(list)

    for s in strs:
        dic[str(sorted(s))].append(s)
    print dic
    for value in dic.values():
        ans.append(sorted(value))

    return ans


# print groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

print groupAnagrams([""])