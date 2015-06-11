# test page https://www.thepartysource.com/express/item.php?id=12325
## Beautiful Soup document http://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-string
## http://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table


from bs4 import BeautifulSoup
import urllib
html = urllib.urlopen('https://www.thepartysource.com/express/item.php?id=12325')
soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class':'itemHotspot'})
#print table
rows = table.find_all('tr')
for row in rows:
	cols = row.find_all('td')
	print cols
#rows = table_body.find_all('tr')







