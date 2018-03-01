from pirc522 import RFID
from threading import Thread
import rfidGlobals as g

reader = RFID()
class RFID:
	def __init__(self):
		self.sentMessage = False
		self.readerThread = Thread(target=self.run)
	
	def start(self):
		self.running = True
		self.readerThread.start()

	def terminate(self):
		self.running = False

	def sendMessage(self, uid, active):
		g.cartStatus = True
		self.sentMessage = True
		g.readID = uid
		g.cartActive = active

	def run(self):
		while self.running:
			if self.sentMessage:
				if not g.cartStatus:
					self.sentMessage = False
			else:
				reader.wait_for_tag()
				(err, tag_type) = reader.request()
				if not err:
					(err, uid) = reader.anticoll()
					reader.stop_crypto()
					if g.readID != uid:	
						self.sendMessage(uid, True)
				else:
					if g.cartActive:
						self.sendMessage(["-1"], False)
		reader.cleanup			
