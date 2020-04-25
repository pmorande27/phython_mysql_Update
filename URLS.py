import covid19fact_data_source
import covid19fact_information_getter
import who_data_source
import who_information_getter
import wk_black_list_data_source

# This is the main page of covid19facts. It is used as a source of reliable information
covid19facts_en_main = 'https://www.covid-19facts.com/?page_id=82920'
# possibility of adding other languages
# problem, the page is not all in spanish (most of information sills appear in english)
covid19facts_es_main = 'https://www.covid-19facts.com/?page_id=82920&lang=es'

# This is the main page of WHO related to covid-19. It is used as a source of reliable information
who_covid_en_main = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019'
who_covid_news = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/events-as-they-happen'

# This is the list of fake news websites recorded in wikipedia
wk_main = 'https://en.wikipedia.org'
wk_black_list = 'https://en.wikipedia.org/wiki/List_of_fake_news_websites'


def getInformation_covid19():
    urls = covid19fact_data_source.update_2d_facts_main_page(covid19facts_en_main)
    all_information = []
    for url in urls:
        information = covid19fact_information_getter.data_getter(url[1])
        all_information.append(information)
    return all_information


def print_updated_information_covid19facts():
    urls = covid19fact_data_source.update_2d_facts_main_page(covid19facts_en_main)
    for url in urls:
        print(url[1])
        information = covid19fact_information_getter.data_getter(url[1])
        for info in information:
            print(info)
            print('\n\n\n\n\n\n')


def get_updated_information_who():
    urls = who_data_source.update_information_links(who_covid_news)
    print(urls)
    print(len(urls))
    print('\n\n\n\n\n\n')
    print(urls[0])


def getBlackListWk():
    urls = wk_black_list_data_source.getPage(wk_black_list)
    # for url in urls:
    #   print(url)
