from selenium import webdriver
import time, sys, traceback

def run():
	driver = webdriver.PhantomJS()
	driver.get("http://www.40Watt.com")
	try:
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
	
		for i in reversed(range(0, len(days))):
			bands_text = bands[i].text
			print('Band: {0}\n'.format(bands_text), end="")
		
			days_text = days[i].text
			print('Date: {0}\n'.format(days_text), end="")
	
			price_text = prices[i]
			print('Price: {0}\n'.format(price_text), end="")
		
			times_text = doors[i].text
			print('{0}'.format(times_text))
		
			print("------------------------------------")
	
		driver.quit()
		print("------------40 Watt Club------------")
	except:
		print(str(sys.exc_info()))
		traceback.print_tb(sys.exc_info()[2])
		driver.quit()

try:
	if sys.argv[1] == '-o':
		run()
	else:
		while True:
			run()
			time.sleep(43200)
except:
	while True:
		run()
		time.sleep(43200)
