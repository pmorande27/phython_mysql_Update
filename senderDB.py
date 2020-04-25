import pymysql
import URLS
import requests
import covid19fact_data_source
import wk_black_list_data_source

mydb = pymysql.connect(host='localhost',port= 3306, user='root', password="fakeoffserver", database="test_data")
cursor = mydb.cursor()


def update_covid19facts():
    dropTable('WhiteList')
    createTable()
    insertCovid19Information()


def update_BList():
    # dropTable('BlackList')
    # createBList()
    # insertBList()
    print("Update in Process... Please Wait...")
    linksArray = wk_black_list_data_source.getPage(URLS.wk_black_list)
    print('%s links were found and reading to be added to the Black List.' % len(linksArray))
    val = []

    for i in linksArray:
        index = linksArray.index(i)
        if not linksArray[index].lower() in val:
            val.append(linksArray[index].lower())

    counter = 0
    for v in val:
        counter = counter + insertNewLinkBList(v)
    print('\n\n\n' + str(counter) + ' new links are added')


def createTable():
    table = """CREATE TABLE WhiteList( ID INT NOT NULL AUTO_INCREMENT, SOURCE TEXT NOT NULL, TITLE TEXT DEFAULT 'Title', 
    INFORMATION MEDIUMTEXT NOT NULL, PRIMARY KEY(ID)) """
    print('Table created')
    cursor.execute(table)


def dropTable(table_name):
    drop_table = "DROP TABLE IF EXISTS %s"
    cursor.execute(drop_table % table_name)
    print('Table dropped')


def insertCovid19Information():
    print("Insert Process... Please Wait...")
    page = requests.get(URLS.covid19facts_en_main)

    source = covid19fact_data_source.getLinks(page)
    print("%s sources found" % len(source))
    print("Sources collected... Please Wait...")

    title = covid19fact_data_source.getTitles(page)
    print("%s titles found" % len(title))
    print("Titles collected... Please Wait...")

    information = URLS.getInformation_covid19()
    print("%s articles found" % len(information))
    print("Information collected... Please Wait...")
    val = []

    for i in information:
        index = information.index(i)
        val.append((source[index], title[index], '\n'.join(map(str, information[index]))))

    print(val)

    add_order = "INSERT INTO WhiteList (SOURCE, TITLE,INFORMATION) VALUES (%s, %s, %s);"

    cursor.executemany(add_order, val)
    mydb.commit()
    print(cursor.rowcount, "was inserted.")


def close_connection():
    mydb.close()


def select_all(table):
    retrieve = "SELECT * FROM %s"
    cursor.execute(retrieve % table)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    mydb.commit()


def createBList():
    table = """CREATE TABLE BlackList( ID INT NOT NULL AUTO_INCREMENT, LINK TEXT NOT NULL UNIQUE , CONFIRMED BOOLEAN, 
     PRIMARY KEY(ID)) """
    print('Table BlackList created')
    cursor.execute(table)


def insertBList():
    print("Insert Process... Please Wait...")
    linksArray = wk_black_list_data_source.getPage(URLS.wk_black_list)
    print('%s links were found and reading to be added to the Black List.' % len(linksArray))
    val = []

    for i in linksArray:
        index = linksArray.index(i)
        if not linksArray[index].lower() in val:
            val.append(linksArray[index].lower())

    print(val)

    add_order = "INSERT INTO BlackList (LINK, CONFIRMED) VALUES (%s, 1);"

    cursor.executemany(add_order, val)
    mydb.commit()
    print(cursor.rowcount, " was inserted.")


def insertNewLinkBList(url):
    counter = 0
    try:
        insertLink = "INSERT INTO BlackList (LINK, CONFIRMED) VALUES (%s,1);"
        cursor.execute(insertLink, url)
        mydb.commit()
        print(cursor.rowcount, " link inserted to BlackList")
        counter = counter + 1
    except:
        print(url + ' is already in the BlackList')

    return counter