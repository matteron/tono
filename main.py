from rfid import RFID
from cartData import cartData
from buttons import Buttons
import rfidGlobals

rfidGlobals.init()

reader = RFID()
cartData = cartData()
b = Buttons(7,11,13,15)

regState = False
playing = False
playingID = "0"
playingPath = "0"

reader.start()

while True:
	if b.state_pwr:
		b.resetStates()
		break
	if playing:
		if cartStatus:
			playing = False
		if b.state_pau:
			b.resetStates()
			#pause track
		if b.state_fwd:
			b.resetStates()
			#forward track
		if b.state_bak:
			b.resetStates()
			#previous track
	else:
		if cartStatus:
			if cartActive:
				cartStatus = False
				playingID = readID
				playingPath = cartData.getCartPath(readID)
				if playingPath == None:
					regState = True
				else:
					playing = True
					print(uid)
					#start player here
reader.terminate()
#start shutdown