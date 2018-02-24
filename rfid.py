from pirc522 import RFID

reader = RFID()
class RFID:

	def getUID(self):
		
		reader.wait_for_tag()
		(err, tag_type) = reader.request()
		if not err:
			(err, uid) = reader.anticoll()
			if err:
				reader.stop_crypto()	
				return None
			else:
				reader.stop_crypto()
				return uid
		else:
			reader.stop_crypto()
			return None
	def cleanup(self):
		reader.cleanup()
