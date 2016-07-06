#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 17, 2016 by 8:15 PM

class Song(object):
	def __init__(self,title, artist):
		self.title = title
		self.artist = artist

	def __str__(self):
		return ('"%(title)s" by %(artist)s' % self.__dict__)

	@classmethod
	def create_songs(cls,songlist):
		for artist, title in songlist:
			yield cls(title,artist)

songs = (('Glen Hansard', 'Leave'),('Stevie Ray Vaughan', 'Lenny'))

for song in Song.create_songs(songs):
	print song

print dir()




