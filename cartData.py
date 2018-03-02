import csv
import sys

class cartData:
	# Returns the name of the playlist stored in the database.csv file
	def getCartPlaylist(self, uid):
		self.f = open('database.csv', "rb")
		self.csv_file = csv.reader(self.f, delimiter=",")
		for row in self.csv_file:
			if row[0] == str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3]):
				self.f.close()
				return row[1]
		self.f.close()
		return None
