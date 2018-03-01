def init():
	# Global Variables for Threading with RFID scanner.
	global cartStatus		#True for a change, false for the same.
	cartStatus = False

	global readID			# -1 for no cart found.
	readID = "-1"

	global cartActive		# False if no cart is inserted
	cartActive = False 		