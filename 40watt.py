import requests
from html.parser import HTMLParser

class FortyWattParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.out = 0
		self.filter = ["", "40 Watt", "706.549.7871", "More Info", "Tickets"]
		self.tag_filter = ["script", "title", "style", "meta"]
		self.attr_filter = [("class", "sidebar floatright")]
	
	def handle_starttag(self, tag, attrs):
		if tag in self.tag_filter:
			self.out += 1
		elif ("id", "tfly-featured-events") in attrs:
			self.out = 100000
		elif ("class", "list-view") in attrs:
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
		if data not in self.filter and not self.out:
			if "Doors: " in data or data == "/":
				print(data, end="")
			elif "$" in data and "." in data:
				print(data)
				print("------------------------")
			else:
				print(data)

parser = FortyWattParser();
parser.feed(requests.get("http://www.40watt.com/").text)
