from selenium import webdriver
#from selenium.webdriver.firefox.webdriver import FirefoxProfile

#profile = FirefoxProfile("C:\\Users\\user\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\zahyinl2.Selenium")

#driver = webdriver.Firefox(profile)
driver = webdriver.Firefox()
driver.get("http://www.40Watt.com")

debugging = false

bands = driver.find_elements_by_xpath("//h1[@class='headliners summary']/a[1]")
days = driver.find_elements_by_xpath("//h2[@class='dates']")
doors = driver.find_elements_by_xpath("//span[@class='doors']")
prices = driver.find_elements_by_xpath("//h3[@class='price-range']")

band_max_len = 0
day_max_len = 0
price_max_len = 0

for band in bands:
	if len(band.text) > band_max_len:
		band_max_len = len(band.text)
		
for day in days:
	if len(day.text) > day_max_len:
		day_max_len = len(day.text)

for price in prices:
	if len(price.text) > price_max_len:
		price_max_len = len(price.text)

if debugging:
	print(band_max_len)
	print(day_max_len)
	print(price_max_len)

for i in range(0, len(days)):
	bands_text = bands[i].text
	print('Band: {0}'.format(bands_text), end="")
	for j in range(1, band_max_len - len(bands[i].text) + 4):
		print(" ", end="")
	print("|", end="")
	print("    ", end="")
	
	days_text = days[i].text
	print('Date: {0}'.format(days_text), end="")
	for k in range(1, day_max_len - len(days[i].text) + 4):
		print(" ", end="")
	print("|", end="")
	print("    ", end="")
	price_text = prices[i].text
	print('{0}'.format(price_text), end="")
	for l in range(1, price_max_len - len(prices[i].text) + 4):
		print(" ", end="")
	print("|", end="")
	print("    ", end="")
	
	times_text = doors[i].text
	print('Price: {0}'.format(times_text))
	
	print(" ")

driver.quit()