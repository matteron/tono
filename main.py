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
		playing = False
		running = False
		b.resetStates()

	if playing:
		if g.cartStatus:
			if not g.cartActive:
				playing = False
				player.stop()
				print("Ejected!")
				g.cartStatus = False

		if b.state_pau:
			if pauseState == 0:
				pauseState = 1
				print("Pause")
			elif pauseState == 1:
				pauseState = 0
				print("Play")
			player.pause(pauseState)
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
		if regState:
			if b.state_pau:
				print("Exiting Registration")
				regState = False
				g.cardStatus = False
				g.readID = []
				b.resetStates()

		if g.cartStatus:
			if g.cartActive:
				g.cartStatus = False
				playingID = g.readID
				playlist = cartData.getCartPlaylist(playingID)
				if playlist == None:
					regState = True
					print("Registering...")
					print(playingID[0], playingID[1], playingID[2], playingID[3])
				else:
					playing = True
					print(playingID[0], playingID[1], playingID[2], playingID[3])
					player.load(playlist)
print("Shut off")
# Uncomment once pi is ready for full use.
# subprocess.call(['shutdown', '-h', 'now'], shell=False)