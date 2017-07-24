import requests
from html.parser import HTMLParser

class CaledoniaParser(HTMLParser):
	def handle_data(self, data):
		filter = ["", "Caledonia Lounge", "BOOKING", "DIRECTIONS", "CALENDAR", "event page", "here.", "Purchase here.", "Be our fan on", "Facebook", "Follow us on", "Twitter", ".", "Booking is done through email:", "caledonialounge@gmail.com", "Technical Specifications", "Missed a show or just want to relive the memories?  Chances are these guys have got you covered:", "Deadly Designs", "Southern Shelter"]
		data = data.strip()
		if "(18-20)" in data and "$" in data:
			print(data)
			print("-------------------------------")
		elif data not in filter:
			print(data)

parser = CaledoniaParser();
parser.feed(requests.get("http://caledonialounge.com/").text)
