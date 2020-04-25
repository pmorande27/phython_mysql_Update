import requests
import pprint

from bs4 import BeautifulSoup


def data_getter(url):
    infoArray = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    textInfo = soup.find('div', class_='post-body')

    for txt in textInfo:
        infoArray.append(txt.text.strip())

    return infoArray




'''

URL = URLS.melanin_skin_url
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')


job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
  title_elem = job_elem.find('h2', class_='title')
  company_elem = job_elem.find('div', class_='company')
  location_elem = job_elem.find('div', class_='location')
  if None in (title_elem, company_elem, location_elem):
    continue
  print(title_elem.text.strip())
  print(company_elem.text.strip())
  print(location_elem.text.strip())
  print()

  python_jobs = results.find_all('h2', string='Python Developer')

  body = soup.find_all('body')
titlesArray = []
informationArray = []

for element in body:
    txt = element.find_all('p')
    titles = element.find_all('h3')

    for title in titles:
        title_text = title.text.strip()
        if title_text != "":
            titlesArray.append(title_text)

    for line in txt:
        line_text = line.text.strip()
        if line_text != "":
            informationArray.append(line_text)
'''

