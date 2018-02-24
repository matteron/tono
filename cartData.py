import csv
import sys

class cartData:
	def __init__(self):
		self.csv_file = csv.reader(open('database.csv', "rb"), delimiter=",")

	def getCartPath(self, uid):
		for row in self.csv_file:
			if row[0] == str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3]):
				return row[1]
		return None
