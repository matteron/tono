from pirc522 import RFID

global cartStatus
global readID

reader = RFID()
class RFID:
	def __init__(self):
		self.sentMessage = False
		self.running = True
	
	def terminate(self):
		self.running = False

	def sendMessage(self, uid):
		cartStatus = True
		self.sentMessage = True
		readID = uid

	def run(self):
		while self.running:
			if self.sentMessage:
				if !cartStatus:
					self.sentMessage = False
			else:
				reader.wait_for_tag()
				(err, tag_type) = reader.request()
				if not err:
					(err, uid) = reader.anticoll()
					reader.stop_crypto()
					if readID != uid:	
						sendMessage(uid)
				else:
					if readID != "-1":
						sendMessage("-1")
		reader.cleanup			
