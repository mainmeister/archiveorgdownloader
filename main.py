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
#from internetarchive import get_session
from internetarchive import get_item
from internetarchive import File
import easygui
import sys

msg = "Enter your search criteria"
title = "Archive.org Downloader"
fieldNames = ["Search value","File type", "Filename includes (leave blank for all)"]
fieldValues = []  # we start with blanks for the values
fieldValues = easygui.multenterbox(msg,title, fieldNames)
searchvalue = fieldValues[0]
filetype = fieldValues[1]
filenameincludes = fieldValues[2]

#s = get_session()
search_results = search_items(searchvalue)
for i in search_results:
    try:
        identifier = i['identifier']
        item = get_item(identifier)
        for file in item.files:
            format = str(file['format']).lower()
            name = str(file['name'])
            #print name + ' -- ' + format
            if format.find(filetype) != -1:
                if filenameincludes:
                    if name.lower().find(filenameincludes) == -1:
                        continue
                fi = File(item, name)
                fi.download(destdir='./download/' , verbose=True)
    except:
        print sys.exc_info()[0]
