import mpd

HOST, PORT = "127.0.0.1", 6600
client = mpd.MPDClient()

class Player:
	def __init__(self):
		client.timeout = 10
		client.idletimeout = None
		client.connect(HOST, PORT)

	#loads playlist and plays first song.
	def load(self, playlist):
		try:
			client.clear()
			client.load(playlist)
		except mpd.ConnectionError:
			client.connect(HOST, PORT)
			client.clear()
			client.load(playlist)
		
	def start(self):
		try:
			client.play(0)
		except mpd.ConnectionError:
			client.connect(HOST, PORT)
			client.play(0)

	# Play/Pause client.  0 for Play, 1 for Pause
	def pause(self,value):
		try:
			client.pause(value)
		except mpd.ConnectionError:
			client.connect(HOST, PORT)
			client.pause(value)
		
	# Next Track
	def next(self):
		try:
			if(int(client.status()['song']) < int(client.status()['playlistlength'])):
				client.next()
		except mpd.ConnectionError:
			client.connect(HOST, PORT)
			if(int(client.status()['song']) < int(client.status()['playlistlength'])):
				client.next()

	# Previous Track
	def prev(self):
		try:
			if(int(client.status()['song']) > 0):
				client.previous()
		except mpd.ConnectionError:
			client.connect(HOST, PORT)
			if(int(client.status()) > 0):
				client.previous()
		
	# Stop Client
	def stop(self):
		try:
			client.stop()
		except mpd.ConnectionError:
			client.connect(HOST, PORT)
			client.stop()

	# Tests to see if we are playing music right now.
	def playing(self):
		try:
			if(client.status()['state'] == 'play'):
				return True
			else:
				return False
		except mpd.ConnectionError:
			client.connect(HOST, PORT)
			if(client.status()['state'] == 'play'):
				return True
			else:
				return False