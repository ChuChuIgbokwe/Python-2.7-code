#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 18, 2016 by 5:12 PM

BaseClass = type("BaseClass",(object,),{})
BaseClass2 = type("BaseClass2",(object,),{})

@classmethod
def Check1(self,myStr):
	return myStr=="ham"

@classmethod
def Check2(self,myStr):
	return myStr == "sandwich"

@classmethod
def Check3(self,myStr):
	return myStr == "with cheese"

#C1 and C2 are subclasses of BaseClass via inheritance
C1 = type("C1",(BaseClass,),{"x":1, "Check": Check1})
C2 = type("C2",(BaseClass,BaseClass2,),{"x":30, "Check": Check2})
C3 = type("C3",(BaseClass,BaseClass2,),{"x":999, "Check": Check3})

def MyFactory(mystr):
	for cls in BaseClass.__subclasses__(): #for each subclass of baseclass
		if cls.Check(mystr): #call the function Check on each of them
			return cls() #create instance of the class and return it if it's true

def MyFactory2(mystr):
	for cls in BaseClass2.__subclasses__():  # for each subclass of baseclass
		if cls.Check(mystr):  # call the function Check on each of them
			return cls()  # create instance of the class and return it if it's true
#
# def MyFactory(myBool):
# 	return C1() if myBool else C2()
#
# m = MyFactory(True)
# v = MyFactory(False)

m = MyFactory("ham")
v = MyFactory("sandwich")
p = MyFactory("with cheese")
print m.x, v.x, p.x

#Have to figure out multiple inheritance works
# c = MyFactory2("ham")
# u = MyFactory2("sandwich")
# i = MyFactory2("with cheese")
# print c.x, u.x, i.x


print BaseClass2.__subclasses__()

