from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
import time

# initialize browser, --incognito for cache/cookies
option = webdriver.ChromeOptions()
option.add_argument("— incognito")

# replace 'C:/bin/chromedriver.exe' to where chromedriver is installed on your system
driver= webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=option)

person = "Tuan Dau"
driver.get("https://www.google.com")

search_query = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search_query.send_keys('site:linkedin.com/in/ AND "York University" ' + person)
search_query.send_keys(Keys.RETURN)

linkedin_urls = driver.find_elements_by_class_name('iUh30')
linkedin_urls = [url.text for url in linkedin_urls]

linkedin_urls

print(len(linkedin_urls))
print(linkedin_urls[0])

