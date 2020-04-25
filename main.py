import URLS
import senderDB

# Commands to update information without affecting db
# URLS.get_updated_information_covid19facts()
# URLS.get_updated_information_who()

# This are the commands to update all the covid19facts information and get it all displayed
# senderDB.update_covid19facts()
# senderDB.select_all('WhiteList')

# Wikipedia black list
# URLS.getBlackListWk()

# senderDB.insertNewLinkBList('bients.com')
senderDB.update_BList()

