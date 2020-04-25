import requests
import URLS
from bs4 import BeautifulSoup


def update_2d_facts_main_page(url):
    page = requests.get(url)
    titlesArray = getTitles(page)
    linksArray = getLinks(page)
    list2d = []

    for i in range(len(titlesArray)):
        list2d.append([titlesArray[i], linksArray[i]])

    return list2d


def update_facts_main_page(url):
    page = requests.get(url)
    titlesArray = getTitles(page)
    linksArray = getLinks(page)
    separated_info = [titlesArray, linksArray]
    return separated_info


def getLinks(page):
    urlsArray = []
    links_soup = BeautifulSoup(page.content, 'lxml')
    all_links = links_soup.find_all('a', class_='btn btn-default btn-sm')
    for fact_link in all_links:
        urlsArray.append(fact_link.get('href'))
    return urlsArray


def getTitles(page):
    titlesArray = []
    titles_soup = BeautifulSoup(page.content, 'html.parser')

    all_titles = titles_soup.find_all('h3')

    for title in all_titles:
        titlesArray.append(title.text.strip())

    titlesArray.pop(len(titlesArray) - 1)
    return titlesArray

