import requests
import URLS
from bs4 import BeautifulSoup

extensionsToCheck = ['.com', '.ml', '.ph', '.info', '.tk', '.org', '.net', '.xyz', '.top', '.fm', '.press', '.club',
                     '.site', '.today', '.co', '.uk', '.ga', '.tv', '.live']

notIncludeWords = ['Cybersquatted.', 'Domain', 'expired', 'Down', 'empty', '404', 'Account', 'Empty', 'No about',
                   'Owned', 'Suspended']


def getPage(url):
    page = requests.get(url)
    # nameArray = getNameSite(page)
    # print(len(nameArray))
    linksArray = getLinks(page)
    # print(len(linksArray))

    return linksArray


def getLinks(page):
    linksArray = []
    links_soup = BeautifulSoup(page.content, 'html.parser')
    all_table = links_soup.find_all('table', class_='wikitable sortable')

    for table in all_table:
        all_td = table.find_all('td')
        for td in all_td:
            url = td.text.strip()

            if not url.startswith('['):

                if any(extension in url for extension in extensionsToCheck):
                    if not ' ' in url:
                        linksArray.append(url)

    return linksArray


def getNameSite(page):
    nameArray = []
    name_soup = BeautifulSoup(page.content, 'html.parser')
    all_tables = name_soup.find_all('table', class_='wikitable sortable')

    all_td = all_tables[len(all_tables) - 1].find_all('td')
    for td in all_td:
        name = td.text.strip()

        if not name.startswith('['):

            if not any(extension in name for extension in extensionsToCheck) and not any(
                    word in name for word in notIncludeWords) and not name == '':

                if len(name.split()) < 5:
                    nameArray.append(name)

    return nameArray
