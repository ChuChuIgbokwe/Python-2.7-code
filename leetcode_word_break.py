#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 30, 2016 by 1:22 PM

'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of
one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''


def wordBreak(self, s, dict):
    dp = [False for i in range(len(s) + 1)]
    dp[0] = True
    for i in range(1, len(s) + 1):
        for k in range(i):
            if dp[k] and s[k:i] in dict:
                dp[i] = True
    return dp[len(s)]


def wordBreak(self, s, dict):
    segmented = [True];
    for i in range(0, len(s)):
        segmented.append(False)
        for j in range(i, -1, -1):
            if segmented[j] and s[j:i + 1] in dict:
                segmented[i + 1] = True
                break
    return segmented[len(s)]


def word_break(s, words):
 	d = [False] * len(s)
 	for i in range(len(s)):
 		for w in words:
 			if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
 				d[i] = True
 	return d[-1]


# ok[i] tells whether s[:i] can be built.
def wordBreak(s, words):
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(i)),
    return ok[-1]

print wordBreak("leetcode",["leet", "code"])

# for i in range(1,6):
#     for j in range(i):
#         print j,i