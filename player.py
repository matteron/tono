from mpd import MPDClient

HOST, PORT = "127.0.0.1", 6600
client = MPDClient()

class Player:
	def __init__(self):
		client.timeout = 10
		client.idletimeout = None
		self.connect()

	def connect(self):
		try:
			client.connect(HOST, PORT)
			yield
		finally:
			client.close()
        	client.disconnect()

	# Loads and plays the first song in the album.
	def load(self, playlist):
		self.connect()
		client.clear()
		client.load(playlist)
		client.play(0)

	# Play/Pause client.  0 for Play, 1 for Pause
	def pause(self,value):
		self.connect()
		client.pause(value)

	def next(self):
		self.connect()
		client.next()

	def prev(self):
		self.connect()
		if(client.status() > 0):
			client.previous()

	def stop(self):
		self.connect()
		client.stop()
