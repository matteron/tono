from mpd import MPDClient

HOST, PORT = "127.0.0.1", 6600
client = MPDClient()

class Player:
	def __init__(self):
		client.timeout = 10
		client.idletimeout = None
		client.connect(HOST, PORT)

	def connect(self):
		client.connect(HOST, PORT)
	# Loads and plays the first song in the album.
	def load(self, playlist):
		connect()
		client.clear()
		client.load(playlist)
		client.play(0)

	# Play/Pause client.  0 for Play, 1 for Pause
	def pause(self,value):
		connect()
		client.pause(value)

	def next(self):
		connect()
		client.next()

	def prev(self):
		connect()
		if(client.status() > 0):
			client.previous()

	def stop(self):
		connect()
		client.stop()
