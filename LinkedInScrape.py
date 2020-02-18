from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
import time

un="Redacted"
pw="Redacted"

# initialize browser, --incognito for cache/cookies
option = webdriver.ChromeOptions()
option.add_argument("— incognito")

# replace 'C:/bin/chromedriver.exe' to where chromedriver is installed on your system
driver= webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=option)
driver.get("https://www.linkedin.com/")

time.sleep(2)

# log in
driver.find_element_by_xpath("/html/body/nav/section[2]/form/div[1]/div[1]/input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/nav/section[2]/form/div[1]/div[1]/input").send_keys(un)
driver.find_element_by_xpath("/html/body/nav/section[2]/form/div[1]/div[2]/input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/nav/section[2]/form/div[1]/div[2]/input").send_keys(pw)
driver.find_element_by_xpath("/html/body/nav/section[2]/form/div[2]/button").click()
time.sleep(3)

# search people
person = "Tuan Dau"
driver.get("https://www.google.com")

search_query = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search_query.send_keys('site:linkedin.com/in/ AND "York University" ' + person)
search_query.send_keys(Keys.RETURN)
