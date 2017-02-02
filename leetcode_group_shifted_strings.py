#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 29, 2016 by 12:14 AM
'''
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep
"shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the lexicographic order.


'''


import collections
def groupStrings(strings):
    """
    :type strings: List[str]
    :rtype: List[List[str]]
    """
    d = collections.defaultdict(list)
    for s in strings:
        shift = tuple([(ord(c) - ord(s[0])) % 26 for c in s])
        d[shift].append(s)

    return map(sorted, d.values())

print groupStrings( ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"] )