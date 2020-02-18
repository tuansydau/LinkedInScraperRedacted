import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd
import xlrd


def namesAndEmails():
    loc = "pathToAlumniListCSV"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(4)

    master = []
    for i in range(1,5746):
        if (sheet.cell_value(i,2) != ""):
            master.append([sheet.cell_value(i,0),sheet.cell_value(i,1),sheet.cell_value(i,2)])
    return master

#initialize browser
driver = webdriver.ChromeOptions()
driver.add_argument("- incognito")
browser = webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=driver)

#getting strings to search bing
nameList = namesAndEmails()
person = []
'site:linkedin.com/in/ AND "york university" AND "Tuan Dau"'
for i in nameList:
    person.append( 'site:linkedin.com/in/ AND "york university" AND "'+i[0]+" "+i[1]+'"')

linkedin_url_master=[]
#go to bing to get urls
for i in person:
    url = "https://www.bing.com/"
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys(i)
    time.sleep(0.001)
    browser.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys(Keys.RETURN)
    time.sleep(0.001)
    linkedin_urls = browser.find_elements_by_tag_name('cite')
    linkedin_urls = [url.text for url in linkedin_urls]
    if (linkedin_urls!=[]):
        linkedin_url_master.append(linkedin_urls[0]) 
        print (linkedin_urls[0])

df_urls = pd.DataFrame(linkedin_url_master)

df_urls.to_csv(r'savePathtoCSV')
