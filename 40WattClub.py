#I would suggest uncommenting the profile lines and adding a firefox profile that doesn't load images
#to save bandwidth

from selenium import webdriver
import re
#from selenium.webdriver.firefox.webdriver import FirefoxProfile

#profile = FirefoxProfile("C:\\Users\\user\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\zahyinl2.Selenium")

#driver = webdriver.Firefox(profile)
driver = webdriver.Firefox()
driver.get("http://www.40Watt.com")

debugging = False

bands = driver.find_elements_by_xpath("//h1[@class='headliners summary']/a[1]")
days = driver.find_elements_by_xpath("//h2[@class='dates']")
doors = driver.find_elements_by_xpath("//span[@class='doors']")
raw_prices = driver.find_elements_by_class_name("ticket-price")
prices = [];

u = 0

for p in raw_prices:
	prices.append(p.text.translate({ord(c): None for c in 'Tickets'}).replace("\n", ""))
	u = u+1

for pr in range(0, len(prices)):
	if prices[pr] == "Fr":
		prices[pr] = "Free"

band_max_len = 0
day_max_len = 0
price_max_len = 0

if debugging:
	print(band_max_len)
	print(day_max_len)
	print(price_max_len)

for i in reversed(range(0, len(days))):
	bands_text = bands[i].text
	print('Band: {0}\n'.format(bands_text), end="")
	
	days_text = days[i].text
	print('Date: {0}\n'.format(days_text), end="")

	price_text = prices[i]
	print('Price: {0}\n'.format(price_text), end="")
	
	times_text = doors[i].text
	print('{0}'.format(times_text))
	
	print("------------------------------------------------------------")

driver.quit()
