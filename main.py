from rfid import RFID
from cartData import cartData
from buttons import Buttons
from player import Player
import rfidGlobals as g

g.init()

reader = RFID()
cartData = cartData()
b = Buttons(7,11,13,15)
player = Player()

running = True
regState = False
playing = False
pauseState = 0		#0 for Play, 1 for Pause
playingID = []
playlist = "0"

reader.start()

while running:
	if b.state_pwr:
		print("Power")
		reader.terminate()
		player.stop()
		running = False
		b.resetStates()
	if playing:
		if g.cartStatus:
			playing = False
			player.stop()

		if b.state_pau:
			print("Pause")
			if pauseState == 0:
				pauseVal = 1
			else if pauseState == 1:
				pauseVale = 0
			player.pause(pauseVal)
			b.resetStates()

		if b.state_fwd:
			print("Forward")
			player.next()
			b.resetStates()

		if b.state_bak:
			print("Rewind")
			player.prev()
			b.resetStates()

	else:
		if g.cartStatus:
			if g.cartActive:
				g.cartStatus = False
				playingID = g.readID
				playlist = cartData.getCartPlaylist(playingID)
				if playlist == None:
					regState = True
				else:
					playing = True
					print(playingID[0] + playingID[1] + playingID[2] + playingID[3])
					player.load(playlist)
print("Shut off")
