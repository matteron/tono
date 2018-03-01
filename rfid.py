from pirc522 import RFID
from threading import Thread
import rfidGlobals

class RFID:
	def __init__(self):
		self.reader = RFID()
		self.sentMessage = False
		self.readerThread = Thread(target=self.run)
	
	def start(self):
		self.running = True
		self.readerThread.start()

	def terminate(self):
		self.running = False

	def sendMessage(self, uid, active):
		global cartStatus
		global readID
		global cartActive

		cartStatus = True
		self.sentMessage = True
		readID = uid
		cartActive = active

	def run(self):
		global cartStatus
		global readID
		global cartActive

		while self.running:
			if self.sentMessage:
				if not cartStatus:
					self.sentMessage = False
			else:
				reader.wait_for_tag()
				(err, tag_type) = reader.request()
				if not err:
					(err, uid) = reader.anticoll()
					reader.stop_crypto()
					if readID != uid:	
						sendMessage(uid, True)
				else:
					if cartActive:
						sendMessage("-1", False)
		reader.cleanup			
