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

running = True			# If main program is running
regState = False		# If program is in registration state.
active = False			# If we are playing or not
ignition = False		# If we have loaded the playlist but haven't started play yet

playindID = []			# an array of strings for the UID
playlist = "0"			# playlist string from the database.csv

reader.start()

player.load("startup")
player.start()
while player.playing():
	pass
print("ready")

while running:
	if b.state_pwr:
		print("Button Pressed: Power")
		reader.terminate()
		player.stop()
		b.resetStates()
		running = False
		active = False
		break
	if active:
		if player.playing():
			if b.state_pau:
				print("Button Pressed: Pause")
				player.pause(1)
				print("Pausing...")
				b.resetStates()
			if b.state_fwd:
				print("Button Pressed: Next")
				player.next()
				print("Next Track...")
				b.resetStates()
			if b.state_bak:
				print("Button Pressed: Previous")
				player.prev()
				print("Previous Track...")
				b.resetStates()
		else:
			if b.state_pau:
				print("Button Pressed: Play")
				player.pause(0)
				print("Resuming...")
				b.resetStates()
			if g.cartStatus:
				if not g.cartActive:
					print("Ejected!")
					player.stop()
					active = False
				g.cartStatus = False
	else:
		if regState:
			if b.state_pau:
				print("Pause Pressed: Exiting Registration")
				regState = False
				g.cartStatus = False
				g.readID = []
				b.resetStates()
		elif ignition:
			if b.state_pau:
				print(playlist)
				player.start()
				ignition = False
				active = True
				print("Ignition!")
				b.resetStates()
			if g.cartStatus:
				if not g.cartActive:
					ignition = False
					print("Ejected!")
					print("igniton: off")
				g.cartStatus = False
				b.resetStates()
		elif g.cartStatus:
			if g.cartActive:
				playingID = g.readID
				playlist = cartData.getCartPlaylist(playingID)
				if playlist == None:
					regState = True
					print("Enterin Registration")
					print(playingID[0], playingID[1], playingID[2], playingID[3])
				else:
					ignition = True
					print(playingID[0], playingID[1], playingID[2], playingID[3])
					print(playlist)
					player.load(playlist)
					print("ignition: on")
			g.cartStatus = False
print("Shutting Off")
subprocess.call(['shutdown', 'now'], shell=False)
