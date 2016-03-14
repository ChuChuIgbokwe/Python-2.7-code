#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 2:07 PM

class BaseCharacter(object):
	# def __init__(self,name):
	# 	self.name = name
	def printName(self):
		print self.name

class NonPlayable_Character(BaseCharacter):
	def __init__(self,name):
		pass

class Playable_Character(BaseCharacter):
	def __init__(self):
		self.weapon = Weapon()

class Friendly(NonPlayable_Character):
	def __init__(self):
		pass


class Enemy(NonPlayable_Character):
	def __init__(self):
		self.attackDamage = 5

class Archer(Playable_Character):
	pass

class GreenLAntern(Playable_Character):
	pass

class Butcher(Playable_Character):
	pass

class Weapon(object):
	pass

if __name__ == '__main__':
	enemy = Enemy()
	print enemy.attackDamage
	butcher = Butcher()
	print butcher.weapon



