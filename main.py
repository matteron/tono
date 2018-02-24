from rfid import RFID
from cartData import cartData
from buttons import Buttons

reader = RFID()
cartData = cartData()
b = Buttons(7,11,13,15)

regState = False
playing = False
playingID = "0"
playingPath = "0"
uid = "0"

pwr = b.pwr() 
fwd = b.fwd()
pau = b.pau()
bak = b.bak()

while True:
	if playing:
		uid = reader.getUID()
		if uid != playingID:
			#Stop Playing
			pass
	else:
		if regState:
			#display UID and then wait for stop button
			pass
		else:
			if(pau):
				print "hi"
			uid = reader.getUID()
			if uid != None:
				playingID = uid
				playingPath = cartData.getCartPath(uid)
				if playingPath == None:
					# Display UID to register new card.
					pass
				elif playingPath != None:
					# Start Player
					pass
