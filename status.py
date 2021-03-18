from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def Status():
	   driver = webdriver.Chrome()
       wait = WebDriverWait(driver, 10)
	   #Avoiding mixing up of different elements
	   #while transitioning
       driver.get("https://web.whatsapp.com")
       #The method of logging into whatsapp
	   elem = driver.find_element_by_class("_18-9u _1bvi5 _3-8er")
	   elem.click()
	   #Opens the profile

	   
       elem2 = driver.find_element_by_class("_3-8er")
	   #Image
 	   elem2.click()
	   val1 = input("Enter your number: ")
       val = int(val1) 
           #gets the number for the list 
	   #dividing it into functions 
	   if val==1:
	      elem3=driver.find_element_by_xpath("//div[@aria-label='View photo']/div[@class='_11srW _2xxet'][text()='View photo']")  	
	   elif val==2:
	      elem3=driver.find_element_by_xpath("//div[@aria-label='Take photo']/div[@class='_11srW _2xxet'][text()='Take photo']") 
	   elif val==3:
	      elem3=driver.find_element_by_xpath("//div[@aria-label='Upload photo']/div[@class='_11srW _2xxet'][text()='Upload photo']") 
	   elif val==4:
	      elem3=driver.find_element_by_xpath("//div[@aria-label='Remove photo']/div[@class='_11srW _2xxet'][text()='Remove photo']") 
	   else:
	      break