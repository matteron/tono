from mpd import MPDClient

client = MPDClient()

class Player:
	def __init__(self):
		client.timeout = 10
		client.idletimeout = None
		client.connect("localhost",6600)

	# Loads and plays the first song in the album.
	def load(self, playlist):
		client.load(playlist)
		client.pause(0)

	# Play/Pause client.  0 for Play, 1 for Pause
	def pause(self,value):
		client.pause(value)

	def next(self):
		client.next()

	def prev(self):
		client.previous()

	def stop(self):
		client.stop()
