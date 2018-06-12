from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
import platform
from time import sleep
# from config import Config
# import _mssql
import decimal
import uuid
# import pymssql

##read config file
# f = file('config.cfg')
# cfg = Config(f)

### set Const Data
SportsNames = ["Soccer", "Basketball", "Hockey", "Baseball", "American Football", "Volleyball", "MMA"]
BASE_URL = "http://www.oddsportal.com"


#connect to ms sql server and create tables
# conn = pymssql.connect(host= cfg.hostname , user=cfg.username, password=cfg.password, database=cfg.database)
# cursor = conn.cursor()
browser = webdriver.Firefox(executable_path="E:\work\pythonworks\odd_scrapping\geckodriver.exe")

# login
print('http://www.oddsportal.com/login/')
browser.get('http://www.oddsportal.com/login/')
browser.find_element_by_id("login-username1").send_keys("ohzoom")
browser.find_element_by_id("login-password1").send_keys("chang0503!")
browser.find_elements_by_xpath("//*[@type='submit']")[0].click()

### Get Sports URLs
browser.get(BASE_URL)
soup = BeautifulSoup(browser.page_source, "html.parser")

sports = soup.find_all("li",{"class":"sport"})
for sport in sports:
    if sport.find("div", {"class": "sport_name"}).text in SportsNames:

        ## get sport Name
        gm_sport_name = sport.find("div", {"class": "sport_name"}).text
        print("----------------------------------------------------------------------")
        print(gm_sport_name)

        ## get countries
        for country in sport.find_all("li", {"class":"country"}):
            if not country.find("a").text.strip()=="Popular":
                countryName = country.find("a").text.strip()
                print(countryName)

                ### get leagues
                print("     -------Leagues-------------------------")
                for leg in country.find_all("li", {"class":"tournament"}):
                    leagName = leg.text.replace('\n',"")
                    print(leagName)
                    legUrl = BASE_URL + leg.find("a").get('href')
                    print(legUrl)
                    driver = webdriver.Firefox(executable_path="E:\work\pythonworks\odd_scrapping\geckodriver.exe")
                    driver.get(legUrl)
                    soup1 = BeautifulSoup(driver.page_source, "html.parser")

                    ## get teamNames
                    for tag in soup1.find_all("table",{"class":"table-main"})[0].find_all("tr",{"class":"odd"}):
                        teamName    = tag.find("td", {"class":"name table-participant"}).find("a").text
                        teamUrl     = BASE_URL + tag.find("td", {"class":"name table-participant"}).find("a").get("href")
                        print( "TEAM NAME  = " + teamName)
                        print("TEAM URL  = " + teamUrl)

                    driver.quit()
                    # sleep(100)

















