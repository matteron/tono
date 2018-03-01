from rfid import RFID
from cartData import cartData
from buttons import Buttons
from threading import Thread

# Global Variables for Threading with RFID scanner.
global cartStatus		#True for a change, false for the same.
cartStatus = False
global readID			# -1 for no cart found.
readID = "-1"
global cartActive	
cartActive = False 		#

reader = RFID()
readerThread = Thread(target=reader.run)
cartData = cartData()
b = Buttons(7,11,13,15)

regState = False
playing = False
playingID = "0"
playingPath = "0"

pwr = b.pwr()
fwd = b.fwd()
pau = b.pau()
bak = b.bak()

readerThread.start()

while True:
	if pwr:
		b.resetStates()
		break
	if playing:
		if cartStatus:
			playing = False
		if pau:
			b.resetStates()
			#pause track
		if fwd:
			b.resetStates()
			#forward track
		if bak:
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
					#start player here
readerThread.terminate()
#star shutdown