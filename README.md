# LinkedInScraperRedacted
A version of the LinkedIn web scraper that I made with my friend Vivek Wadhwani with sentitive information redacted.

Dependencies:

Python 3.X
Selenium webdriver
Chromedriver
Pandas

Before use:
- In creatingCsvLife.py, change loc variable to a file path to a .csv file with a list of names, and change line 49 to a file path where you would like to save the .csv file of LinkedIn URLs
- run creatingCsvLife.py to generate a .csv file of URLs.
- In workAndSchoolScrape.py, change un and pw variables on lines 11 and 12 to your LinkedIn username and password respectively. Change the file path in line 15 to where the .csv file of LinkedIn URLs is saved.

To use:
- Run workAndSchoolScrape.py
