#NOT WORKING SORRY

from selenium import webdriver
import sys, time, traceback
def run():
	driver = webdriver.PhantomJS()
	driver.get("http://caledonialounge.com")
	
	try:
		dates = driver.find_elements_by_tag_name('dt')
		for d in dates:
			print(d.text)
		bands_parent = driver.find_elements_by_xpath('//ul')
		prices_and_doors_parent = driver.find_elements_by_xpath('//p')
		prices_and_doors = []
	
		for k in prices_and_doors_parent:
			if "presents" not in k.text.lower() && "shows_Header" not in k.get_attribute("class"):
				prices_and_doors.append(k.text)
		
		print(prices_and_doors)
		
		for i in reversed(range(0, len(dates))):
			print("Date: " + dates[i].text)
			print("Bands:")
			bands = bands_parent[i+1].find_elements_by_tag_name('li')
			for j in range(0, len(bands)):
				if bands[j].text == "":
					pass
				elif "event page here." not in bands[j].text.lower() and "purchase here." not in bands[j].text.lower() and "purchase tickets here." not in bands[j].text.lower() and " in advance." not in bands[j].text.lower():
					print("  " + bands[j].text)
			doors = prices_and_doors[i].split("\n")[0]
			prices = prices_and_doors[i].split("\n")[0]
			print("Doors: " + doors[9:])
			print("Price: " + prices)
			print("------------------------------------")
		driver.quit()
		print("----------Caledonia Lounge----------")
	except:
		print(str(sys.exc_info()))
		traceback.print_tb(sys.exc_info()[2])
		driver.quit()

while True:
	run()
	time.sleep(43200)
