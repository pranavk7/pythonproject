import urllib.request as ur
from bs4 import BeautifulSoup,SoupStrainer
import re

#function to check if the link is broken and if not, return our response
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

#Main
master_list_of_people_url = list();
depth_limit=2 
root_url = 'https://en.wikipedia.org/wiki/The_World%27s_Billionaires#2015'
unsearched_links=list()
searched_links = list()
unsearched_links.append(root_url)
tablelist = list()
while unsearched_links:
    current_link=unsearched_links.pop()
    searched_links.append(current_link)

    #These three lines will take care of all url issues for us!
    response=check_url_exists_and_get_data(link)
    if not response: #Add this to skip any None returned by get_url_data
        continue

    soup = BeautifulSoup(response,"lxml")
    tables = soup.findAll("table", {"class":"wikitable sortable"})
    for table in tables:
        tablelist.append(table)

links = list()
for table in tablelist:
    #soup = BeautifulSoup(table,"lxml")
    links.append(table.findAll("a"))

print(links)
