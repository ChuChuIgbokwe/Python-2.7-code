#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 15, 2016 by 12:57 AM

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))
print(list(inventory.items()))

for (k,v) in inventory.items():
    print "Got", k, "that maps to", v

for k in inventory:
    print "Got", k, "that maps to", inventory[k]


for akey in inventory.keys():     # the order in which we get the keys is not defined
   print "Got key", akey, "which maps to value", inventory[akey]



ks = list(inventory.keys())
print(ks)

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
keylist = list(mydict.keys())
keylist.sort()
print(keylist[3])

answer = mydict.get("cat") // mydict.get("dog")
print(answer)

total = 0
for akey in mydict:
   if len(akey) > 3:
      total = total + mydict[akey]
print(total)