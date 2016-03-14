#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 03, 2016 by 8:16 PM

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self,hours):
        self.hours = hours
        return super(PartTimeEmployee,self).calculate_wage(hours)
        '''
        You can directly access the attributes or methods of a superclass with
        Python's built-in super call.
        class Derived(Base):
            def method(self,arg):
                return super(Derived, self).method(arg)
        '''


milton = PartTimeEmployee('Azrael')
print milton.full_time_wage(10)
print milton.calculate_wage(10)


class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self): #we can tell Python how to represent an object of our class (for instance, when using a print statement).
        return "(%d, %d, %d)"%(self.x, self.y, self.z)

my_point = Point3D(1,2,3)
print my_point


