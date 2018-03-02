from mpd import MPDClient
from urlparse import urlparse

client = MPDClient()

class Player:
	def __init__(self):
		client.timeout = 10
		client.idletimeout = None
		client.connect("localhost", 6600)
		self.playingPath = "0"

	def addTest(self):
		url = urlparse("file://~/music/USB/Music/Tyler, The Creator/Flower Boy")
		MPDClient.add(url)
		client.playlist()