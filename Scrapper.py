import urllib.request
from bs4 import BeautifulSoup

quote_page = 'https://www.bremer.com/business/lending'
page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

print(soup)