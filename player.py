from mpd import MPDClient

client = MPDClient()

class Player:
	def __init__(self):
		client.timeout = 10
		client.idletimeout = None
		client.connect("localhost", 6600)
		self.playingPath = "0"

	def addTest(self):
		client.playlist()s