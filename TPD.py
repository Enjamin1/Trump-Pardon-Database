
import sqlite3
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


list1 = list()



ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.justice.gov/pardon/pardons-granted-president-donald-trump'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'


#url = "https://www.yesbank.in/pdf/forexcardratesenglish_pdf"
headers={'User-Agent':user_agent,}
request=urllib.request.Request(url,None,headers)


#read and parse the html
r = urllib.request.urlopen(request).read().decode()
soup = BeautifulSoup(r, 'html.parser')


#searching for the part of the site where the pardons are
tags = soup.find_all('table', attrs={'summary':'This table provides information on the Number of Pardons Granted by President Trump'})


# tag ~ the dates trump pardoned people and appending them to list

count = 0
for tag in tags:
  dates = tag.find_all('tr')

  for pardon in dates:
  
    listp = pardon.find_all('td')
    list1.append(listp)
for item in list1:
  try:
    if len(item) < 1:
      continue
    else:
      name = item[0].text
      print("Name:        ", name)
      district = item[1].text
      print("District:    ",district)
      sentance = item[2].text
      print("Sentnace:    ",sentance)
      crime = item[3].text
      print("Crime:       ",crime)
      print('\n')
      print('\n')
      count += 1

  except:
    pass
