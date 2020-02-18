from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import numpy as np
from parsel import Selector
import xlrd
import csv

#login info so we dont get stopped by linkedin
un="Redacted"
pw="Redacted"

# get names into dataframe
urlList = pd.read_csv('urls.csv')
# urlList

# initialize browser, --incognito for cache/cookies
option = webdriver.ChromeOptions()
option.add_argument("— incognito")

# replace 'C:/bin/chromedriver.exe' to where chromedriver is installed on your system
driver = webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=option)
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

# driver.get("https://ca.linkedin.com/in/vivekwadhwani12")

# https://www.linkedin.com/in/rakesh-kotla-853a74164?trk=public_profile_browsemap_profile-result-card_result-card_full-click
# https://in.linkedin.com/in/vivek-w-05a6b888?trk=public_profile_samename_profile_profile-result-card_result-card_full-click
# https://ca.linkedin.com/in/vivekwadhwani12
# https://ca.linkedin.com/in/kaizhuang

# find university
# xpath to extract the first h1 text

# lurl = "https://ca.linkedin.com/in/vivekwadhwani12"

# print fields for testing
def print_fields(url):
    driver.get(url)
    time.sleep(1)
    sel = Selector(text=driver.page_source)
    name = sel.xpath('//div[2]/div[2]/div[1]/ul[1]/li[1]/text()').get()
    if not name is None: name = name.strip()
    print(name)
    position = sel.xpath('//div[2]/h3/text()').extract_first()
    if not position is None: position = position.strip()
    print(position)
    company = sel.xpath('//div[2]/p[2]/text()').get() # if this doesn't work, try .extract_first()
    if not company is None: company = company.strip()
    print(company)
    school = sel.xpath('//div[2]/div/h3/text()').get() # only works if the profile has activity, experience, and education profiles
    if not school is None: school = school.strip()
    print(school)
    out_csv(name, position, company, school)

#print the information to csv file
def out_csv(name, position, company, school):
    list1 = [name, position, company, school]

    with open(r"pathToFieldsCSV", "a", encoding="utf-8") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(list1)

# get next url in list of urls
# def getUrl(i):
#    tempurl=urlList.url[i]
#    return(tempurl)

for lurls in urlList['0']:
    print_fields(lurls)

    # drop empty rows
    finalCsv = pd.read_csv('fields.csv')
    finalCsv.dropna()

    # save our beautiful work
    finalCsv.to_csv('finalFields.csv')
