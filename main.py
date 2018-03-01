from rfid import RFID
from cartData import cartData
from buttons import Buttons
import rfidGlobals as g

g.init()

reader = RFID()
cartData = cartData()
b = Buttons(7,11,13,15)

running = True
regState = False
playing = False
playingID = []
playingPath = "0"

reader.start()

while running:
	if b.state_pwr:
		print("Power")
		reader.terminate()
		running = False
		b.resetStates()
	if playing:
		if g.cartStatus:
			playing = False
		if b.state_pau:
			print("Pause")
			b.resetStates()
			#pause track
		if b.state_fwd:
			print("Forward")
			b.resetStates()
			#forward track
		if b.state_bak:
			print("Rewind")
			b.resetStates()
			#previous track
	else:
		if g.cartStatus:
			if g.cartActive:
				g.cartStatus = False
				playingID = g.readID
				playingPath = cartData.getCartPath(playingID)
				if playingPath == None:
					regState = True
				else:
					playing = True
					print(playingID[0])
					#start player here
print("Shut off")
