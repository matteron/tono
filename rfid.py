from pirc522 import RFID
from threading import Thread

reader = RFID()
class RFID:
	def __init__(self):
		global cartStatus
		global readID
		global cartActive
		self.sentMessage = False
		readerThread = Thread(target=run)
	
	def start(self):
		self.running = True
		readerThread.start()

	def terminate(self):
		self.running = False

	def sendMessage(self, uid, active):
		cartStatus = True
		self.sentMessage = True
		readID = uid
		cartActive = active

	def run(self):
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
