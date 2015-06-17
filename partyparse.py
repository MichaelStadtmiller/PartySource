## Beautiful Soup http://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-string
## http://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table


# new plan.
# enter search terms and get resulting list back.
# https://www.thepartysource.com/express/results.php?i=COCONUT+RUM
# find availability "low-stock" or "in-stock" add to first array (with link)
# open links to get more info on product (QOH) add to second array (with link from first array)
# FINAL ARRAY has all data stored.
# analytics: Product, Liters,Price, QOH, Quantity needed (default=QOH), Subtotal, Discount, Final Cost, Final L, Cost/L
# user input - limit QN to remove discount and limit quantity purchased
# this will help determine if bulk is better then 10% discount


from bs4 import BeautifulSoup
import urllib
def getQOH(myURL):
	html = urllib.urlopen(myURL)
	soup = BeautifulSoup(html)
	table = soup.find('table', attrs={'class':'itemHotspot'})
	rows = table.find_all('tr')
	for row in rows:
		cols = row.find_all('td') #whole column
		if row.strong.string == 'Qty Available':#current QOH
			print cols[1].string

def getProducts(search):
	url = 'https://www.thepartysource.com/express/results.php?o=0&t=&s='+search
	print url

getQOH('https://www.thepartysource.com/express/item.php?id=1850')
getProducts('BOURBON')
