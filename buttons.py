import RPi.GPIO as GPIO


class Buttons:
	def __init__(self, pin_pwr, pin_fwd, pin_pau, pin_bak):
		self.pin_pwr = pin_pwr
		self.pin_fwd = pin_fwd
		self.pin_pau = pin_pau
		self.pin_bak = pin_bak
		
		self.state_pwr = False
		self.state_fwd = False
		self.state_pau = False
		self.state_bak = False

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin_pwr, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(pin_pwr,GPIO.RISING,bouncetime=1000)
		GPIO.add_event_callback(pin_pwr,self.pwrHandler)
		GPIO.setup(pin_fwd, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(pin_fwd,GPIO.RISING,bouncetime=1000)
		GPIO.add_event_callback(pin_fwd,self.fwdHandler)
		GPIO.setup(pin_pau, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(pin_pau,GPIO.RISING,bouncetime=1000)
		GPIO.add_event_callback(pin_pau,self.pauHandler)
		GPIO.setup(pin_bak, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(pin_bak,GPIO.RISING,bouncetime=1000)
		GPIO.add_event_callback(pin_bak,self.bakHandler)
	
	def pwrHandler(self,channel):
		self.state_pwr = True
	def fwdHandler(self,channel):
		self.state_fwd = True
	def pauHandler(self,channel):
		self.state_pau = True
	def bakHandler(self,channel):
		self.state_bak = True
	def resetStates(self):
		self.state_pwr = False
		self.state_fwd = False
		self.state_pau = False
		self.state_bak = False