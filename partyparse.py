## test page https://www.thepartysource.com/express/item.php?id=12325
## Beautiful Soup document http://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-string
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
myURL = 'https://www.thepartysource.com/express/item.php?id=7' #166

def 
html = urllib.urlopen(myURL)
soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class':'itemHotspot'})
#print table
rows = table.find_all('tr')
for row in rows:
	cols = row.find_all('td') #whole column
	colhead = row.strong.string	#just column header
	if colhead == 'Price:':		#get Price
		if row.find('font'):	#if special price
			print row.find('font').contents[0].strip()
		else:
			print row.find(colspan='2').contents[1]
	elif colhead == 'Qty Available':#currnet QOH
		print cols[1].string


