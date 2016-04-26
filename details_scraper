import urllib.request as ur
from bs4 import BeautifulSoup,SoupStrainer
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

def isPerson(browser, url):
    browser.get(url)
    returnVal = False
    soup = BeautifulSoup(browser.page_source,"lxml")
    table = soup.findAll("table", {"class":"infobox"})
    if table:
        tablesoup = BeautifulSoup(str(table[0]),"lxml")
        if tablesoup.body.findAll(text='Born'):
            returnVal = True
    return returnVal

def check_for_people(links):
    #Please note you will have to update this path based on where you have installed phantomjs
    browser = webdriver.PhantomJS(executable_path='/Users/pranavnagesh/Desktop/PK/Spring 2016/Python/Code work/phantomjs')
    master_list = list()
    for link in links:
        if isPerson(browser, link):
            master_list.append(link)
    return master_list


def check_url_exists_and_get_data(url):
    #Pop our imports inside the function so they will always be loaded
    import urllib.request as ur
    import urllib.error as ue
    from bs4 import BeautifulSoup
    try:
        url_req=ur.Request(url)
        url_response=ur.urlopen(url_req)

    except ue.HTTPError as e:
        print("HTTPError",e, "at url",url)
        return None
    except ue.URLError as e:
        print("URLError",e,"at url",url)
    else:
        return url_response

def get_list_of_people():
    depth_limit=2
    unsearched_links=list()
    searched_links = list()

    #TEST LINK ONLY
    #unsearched_links.append('https://en.wikipedia.org/wiki/The_World%27s_Billionaires_2015')

    unsearched_links.append('https://en.wikipedia.org/wiki/The_World%27s_Billionaires')
    unsearched_links.append('https://en.wikipedia.org/wiki/Forbes_list_of_The_World%27s_Most_Powerful_People')
    unsearched_links.append('https://en.wikipedia.org/wiki/The_World%27s_Billionaires#2007_Top_10')
    unsearched_links.append('https://en.wikipedia.org/wiki/The_World%27s_Billionaires_2015')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_female_billionaires')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_Italian_billionaires')
    unsearched_links.append('https://en.wikipedia.org/wiki/Forbes_list_of_Indian_billionaires')
    unsearched_links.append('https://en.wikipedia.org/wiki/Sunday_Times_Rich_List_2015')
    unsearched_links.append('https://en.wikipedia.org/wiki/Sunday_Times_Rich_List_2014')
    unsearched_links.append('https://en.wikipedia.org/wiki/Fortune_Global_500')
    unsearched_links.append('https://en.wikipedia.org/wiki/The_World%27s_Billionaires_2010')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_chief_executive_officers')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_women_CEOs_of_Fortune_500_companies')
    unsearched_links.append('https://en.wikipedia.org/wiki/Category:American_chief_executives_of_Fortune_500_companies')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_NATO_Secretaries_General')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_country#United_States')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_people_on_multiple_governing_boards')
    unsearched_links.append('https://en.wikipedia.org/wiki/Forbes_Celebrity_100')
    unsearched_links.append('https://en.wikipedia.org/wiki/Time_100:_The_Most_Important_People_of_the_Century')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_members_of_the_Forbes_400')
    unsearched_links.append('https://en.wikipedia.org/wiki/The_World%27s_Billionaires')
    unsearched_links.append('https://de.wikipedia.org/wiki/The_World%E2%80%99s_Most_Powerful_People')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_richest_American_politicians')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_Jewish_American_politicians')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_current_United_States_governors')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_current_United_States_Senators')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_former_United_States_Senators')
    unsearched_links.append('https://en.wikipedia.org/wiki/Current_members_of_the_United_States_House_of_Representatives')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_former_members_of_the_United_States_House_of_Representatives')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_monarchs_of_Hawaii')
    unsearched_links.append('https://en.wikipedia.org/wiki/Speaker_of_the_United_States_House_of_Representatives#Notable_elections')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_Secretaries_of_State_of_the_United_States')
    unsearched_links.append('https://en.wikipedia.org/wiki/United_States_Secretary_of_the_Treasury#List')
    unsearched_links.append('https://en.wikipedia.org/wiki/United_States_Secretary_of_Defense')
    unsearched_links.append('https://en.wikipedia.org/wiki/United_States_Attorney_General#Living_former_U.S._Attorneys_General')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_the_oldest_living_members_of_the_United_States_House_of_Representatives')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_female_governors_in_the_United_States')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_U.S._presidential_relatives#Relatives_of_Barack_Obama_-_44th_President')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_United_States_Democratic_Party_presidential_candidates')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_United_States_Democratic_Party_presidential_tickets')
    unsearched_links.append('https://en.wikipedia.org/wiki/Power_100')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_American_Catholics')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States')
    unsearched_links.append('https://en.wikipedia.org/wiki/Forbes_list_of_The_World%27s_Most_Powerful_People')
    unsearched_links.append('https://en.wikipedia.org/wiki/Forbes_list_of_The_World%27s_100_Most_Powerful_Women')
    unsearched_links.append('https://en.wikipedia.org/wiki/Chief_Justice_of_the_United_States')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_United_States_Navy_people')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_United_States_Navy_four-star_admirals')
    unsearched_links.append('https://en.wikipedia.org/wiki/List_of_United_States_Air_Force_four-star_generals')
    unsearched_links.append('https://en.wikipedia.org/wiki/United_States_Secretary_of_the_Air_Force')
    unsearched_links.append('https://en.wikipedia.org/wiki/Chief_of_Staff_of_the_United_States_Air_Force')

    tablelist = list()
    while unsearched_links:
        current_link=unsearched_links.pop()
        if current_link in searched_links:
            continue
        else:
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

    return check_for_people(links)
