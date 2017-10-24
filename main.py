"""
Download files from a search on the archive.org web site.

uses:
    selenium

"""
#from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
#from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# open a browser
# chrome = webdriver.Chrome()
# chrome.get('https://archive.org')
# searchtext = chrome.find_element_by_id("search-bar-1")
# searchtext.send_keys('byte magazine')
# searchtext.submit()

from internetarchive import search_items
from internetarchive import get_session
from internetarchive import get_item
from internetarchive import File


s = get_session()
search_results = search_items("magazine")
for i in search_results:
    identifier = i['identifier']
    item = get_item(identifier)
    for file in item.files:
        format = str(file['format']).lower()
        name = str(file['name'])
        #print name + ' -- ' + format
        if format.find('pdf') != -1: #and name.lower().find('byte') != -1:
            fi = File(item, name)
            try:
                fi.download(destdir='./download/' , verbose=True)
            except:
                pass