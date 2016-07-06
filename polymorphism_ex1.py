#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 21, 2016 by 3:09 AM

# Polymorphism in Computer Science is the ability to present the same interface for differing underlying forms.
# We can have in some programming languages polymorphic functions or methods for example. Polymorphic functions or
# methods can be applied to arguments of different types, and they can behave differently depending on the type
# of the arguments to which they are applied

###################################
# Python is implicitly polymorphic#
###################################
def f(x, y):
    print "values: ", x, y

f(42,43)
f(42, 43.7)
f(42.3,43)
f(42.0, 43.9)
f([3,5,6],(3,5))
f("A String", ("A tuple", "with Strings"))
f({2,3,9}, {"a":3.4,"b":7.8, "c":9.04})

# In typed programming languages like Java or C++, we would have to overload f for the various type combinations.
# Our example could be implemented like this in C++:

# #include <iostream>
# using namespace std;
#
# void f(int x, int y ) {
#     cout << "values: " << x << ", " << x << endl;
# }
#
# void f(int x, double y ) {
#     cout << "values: " << x << ", " << x << endl;
# }
#
# void f(double x, int y ) {
#     cout << "values: " << x << ", " << x << endl;
# }
#
# void f(double x, double y ) {
#     cout << "values: " << x << ", " << x << endl;
# }
#
#
# int main()
# {
#     f(42, 43);
#     f(42, 43.7);
#     f(42.3,43);
#     f(42.0, 43.9);
# }


