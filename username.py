import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait 
usernames = []
i=1

with open('users_followed_list.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        usernames.append(row[1])
        

print(usernames)

chromedriver_path = 'C:\\Users\\Atharva\\Desktop\\Insta Bot\\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('YOUR ID')
password = webdriver.find_element_by_name('password')
password.send_keys('YOUR PASSWORD')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(3)

# notnow = webdriver.find_element_by_css_selector('body > div:nth-child(3) > div > div > div:nth-child(3) > button:nth-child(2)')
# notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications



webdriver.find_elements_by_xpath("//button[contains(text(), 'Not Now')]")[0].click()
while(i<=len(usernames)):
	# search_box = webdriver.find_element_by_xpath("//input[@placeholder='Search']")
	# search_box.send_keys(usernames[i])
	# sleep(3)
	# search_box.send_keys(Keys.ENTER)
	# sleep(2)
	# webdriver.find_elements_by_xpath("//a[@href='/"+usernames[i]+"/']")[0].click()
	webdriver.get('https://www.instagram.com/'+ usernames[i])
	sleep(2)
	webdriver.find_element_by_xpath("//button[contains(text(), 'Following')]").click()
	sleep(2)
	webdriver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
	sleep(2)
	i+=1
# webdriver.find_element_by_xpath("//a[@href='/atharva_35/']").click()
# sleep(2)
# webdriver.find_element_by_xpath("//a[@href='/atharva_35/following/']").click()
# sleep(1)
# # webdriver.find_element_by_xpath("document.querySelector('div[role=dialog]')")
# if(webdriver.find_element_by_xpath("//li//a[contains(text(),'miage.tayo')]")):
# 	webdriver.find_element_by_xpath("//li//a[contains(text(),'miage.tayo')]./div[3]/button").click()
