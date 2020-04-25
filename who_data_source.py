import requests
import URLS
from bs4 import BeautifulSoup


def update_information_links(url):
    page = requests.get(url)
    informationArray = getNewsInformation(page)
    print(len(informationArray))
    return informationArray


def getLinks(page):
    urlsArray = []
    links_soup = BeautifulSoup(page.content, 'lxml')
    all_links = links_soup.find_all('a', class_='link-container')
    for fact_link in all_links:
        link = fact_link.get('href')
        if not link.startswith('https://www.who.int'):
            link = URLS.who_covid_en_main + link
        if '(' in link:
            link = link.replace('(', '%28')
        if ')' in link:
            link = link.replace(')', '%29')
        urlsArray.append(link)

    return urlsArray


def getTitles(page):
    titlesArray = []
    titles_soup = BeautifulSoup(page.content, 'html.parser')

    results = titles_soup.find(id='PageContent_C229_Col01')
    all_titles = results.find_all('div', class_='sf-content-block content-block')
    for title in all_titles:
        realTitle = title.find_all('h2')
        for rt in realTitle:
            if not rt.text.strip() == '':
                titlesArray.append(rt.text.strip())

    return titlesArray


def getNewsInformation(page):
    text_soup = BeautifulSoup(page.content, 'html.parser')

    results = text_soup.find(id='PageContent_C229_Col01')
    all_div = results.find_all('div', class_='sf-content-block content-block')

    all_paragraphsArray = []
    '''
    for div in all_div:
        all_paragraphs = div.find_all('p')
        paragraphText = ''
        for paragraph in all_paragraphs:
            txt = paragraph.text.strip()
            if not txt == '':
                paragraphText = paragraphText + txt + '\n'
    '''
    for div in all_div:
        print(div.get_text(separator=" "))
        '''
        for myItem in myList.split('X'):
            myString = myString.join(myItem.replace('X', 'X\n'))
        '''
        # print(paragraphText)
        # print('\n\n\n\n\n\n')
        all_paragraphsArray.append(div.get_text())
        # paragraphText = ''

    return all_paragraphsArray

