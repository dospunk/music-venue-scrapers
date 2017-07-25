import requests
from html.parser import HTMLParser

class MasqParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.out = 0
		self.filter = ["", "Buy Tickets", "More Info", "The Masquerade Presents", "View All Shows"]
		self.tag_filter = ["script", "title", "style", "meta"]
		self.attr_filter = [("class", "col col-md-1-4 sidebar")]
		self.days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
		self.locations = ["Hell", "Purgatory", "Heaven", "Other Location"]
		self.events = 0
	
	def handle_starttag(self, tag, attrs):
		if tag in self.tag_filter:
			self.out += 1
		elif ("id", "featured-carousel slide slick-initialized slick-slider") in attrs:
			self.out = 100000
		elif ("class", "archiveList--homepage list display-shortList") in attrs:
			self.out = 0
		else:
			for attr in attrs:
				if attr in self.attr_filter:
					self.out += 1
					break

	def handle_endtag(self, tag):
		if tag in self.tag_filter:
			self.out -= 1

	def handle_data(self, data):
		data = data.strip()
		if data not in self.filter and not self.out and self.events <= 13:
			try:
				int(data)
				print(data + " ", end="")
			except ValueError:
				if data in self.days or data in self.locations:
					print(data + " ", end="")
				elif "Doors " in data and "/" in data and ":" in data:
					print(data)
					print("------------------------")
					self.events += 1
				else:
					print(data)

parser = MasqParser();
parser.feed(requests.get("http://masq.com/").text)
