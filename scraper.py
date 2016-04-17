import urllib.request as ur
from bs4 import BeautifulSoup,SoupStrainer
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime



def check_for_people(links):
    #Please note you will have to update this path based on where you have installed phantomjs
    browser = webdriver.PhantomJS(executable_path='/Users/pranavnagesh/Desktop/PK/Spring 2016/Python/Code work/phantomjs')
    
    master_list = list()
    for link in links:
        browser.get(link) 
        browser.execute_script("window.scrollTo(0,1500)") 
        soup = BeautifulSoup(browser.page_source,"lxml")
        table = soup.findAll("table", {"class":"infobox"})
        if table:
            tablesoup = BeautifulSoup(str(table[0]),"lxml")
            if tablesoup.body.findAll(text='Born'):
                master_list.append(link)
    return master_list


def check_url_exists_and_get_data(url):
    #Pop our imports inside the function so they will always be loaded
    import urllib.request as ur
    import urllib.error as ue
    from bs4 import BeautifulSoup
    try:
        url_req=ur.Request(root_url)
        url_response=ur.urlopen(url_req)
    
    except ue.HTTPError as e:
        print("HTTPError",e, "at url",url)
        return None
    except ue.URLError as e:
        print("URLError",e,"at url",url)
    else:
        return url_response

def get_list_of_people():
    master_list_of_people_url = list();
    depth_limit=2 
    unsearched_links=list()
    searched_links = list()
    unsearched_links.append('https://en.wikipedia.org/wiki/The_World%27s_Billionaires#2015')
    unsearched_links.append('https://en.wikipedia.org/wiki/Forbes_list_of_The_World%27s_Most_Powerful_People')

    tablelist = list()
    while unsearched_links:
        current_link=unsearched_links.pop()
        searched_links.append(current_link)

        #These three lines will take care of all url issues for us!
        response=check_url_exists_and_get_data(current_link)
        if not response: #Add this to skip any None returned by get_url_data
            continue

        soup = BeautifulSoup(response,"lxml")
        tables = soup.findAll("table", {"class":"wikitable sortable"})
        for table in tables:
            tablelist.append(table)

    links = list()
    for table in tablelist:
        results = table.findAll("a")
        for element in results:
            full_link = 'https://en.wikipedia.org' + element.get('href')
            if not full_link in links:
                links.append(full_link)

    master_list_of_people_url.append(check_for_people(links))
    return master_list_of_people_url




print(get_list_of_people())
