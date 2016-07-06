#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 25, 2016 by 6:00 PM
# __metaclass__ = type
class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class NandGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
		# if super(NandGate, self).performGateLogic()==1:
		# 	return 0
		# else:
		# 	return 1

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 0
        else:
            return 1

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class NorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 0
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)
		# LogicGate.__init__(self,n) could be replaced with super(UnaryGate,self).__init__(n)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():
	# g1 = AndGate("G1")
	# g2 = AndGate("G2")
	# g3 = OrGate("G3")
	# g4 = NotGate("G4")
	# c1 = Connector(g1,g3)
	# c2 = Connector(g2,g3)
	# c3 = Connector(g3,g4)
	# print(g4.getOutput())
	# print g1.getOutput()
	# Create a series of gates that prove the following equality NOT (( A and B) or (C and D)) is that same as NOT( A and B ) and NOT (C and D)
	ab = NandGate("AB")
	cd = AndGate("CD")
	ab_or_cd = OrGate("AB||CD")
	not_abcd = NotGate("Not")
	c_1 = Connector(ab,ab_or_cd)
	c_2 = Connector(cd,ab_or_cd)
	c_3 = Connector(ab_or_cd,not_abcd)
	# print ab_or_cd.getOutput()
	# print ab.getOutput()
	# print cd.getOutput()
	# print not_abcd.getOutput()

	ab_1 = NandGate('AB_1')
	cd_1 = NandGate("CD_1")
	ab_and_cd = AndGate("And")
	con_1 = Connector(ab_1,ab_and_cd)
	con_2 = Connector(cd_1, ab_and_cd)
	print ab_and_cd.getOutput() == not_abcd.getOutput()


main()





