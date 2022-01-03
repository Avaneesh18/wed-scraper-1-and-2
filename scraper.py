from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"
browser = webdriver.Chrome("chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Brown_dwarf","constellation","right_ascension","declination","app_mag","distance(ly)","spectral_year","mass","radius","discovery_year"]
    planet_data = []
    
    for i in range(0,488):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        
        for ul_tag in soup.find_all("ul",attrs = {"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            tem_list = []

            for index, li_tag in enumerate(li_tags):
                
                if index == 0:
                    tem_list.append(li_tag.find_all("a")[0].contents[0])

                else:
                    try:
                        tem_list.append(li_tag.contents[0])
                    
                    except:
                        tem_list.append("")
            
            planet_data.append(tem_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    
    with open("scraper_2.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()