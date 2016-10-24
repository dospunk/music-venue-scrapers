from bs4 import BeautifulSoup as a
import urllib.request as  c
d = c.urlopen('https://en.wikipedia.org/wiki/Lorem_ipsum')
b = a(d.read(), 'html.parser')
print(b.blockquote.get_text())