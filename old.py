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

def main():
	search = raw_input('Enter a search term: ')
	URL = 'https://www.thepartysource.com/express/results.php?o=0&t=&s='+search.replace(' ','+')#+'&sort=invQOH'
	getProducts(URL)

def getQOH(myURL):
	html = urllib.urlopen(myURL)
	soup = BeautifulSoup(html)
	table = soup.find('table', attrs={'class':'itemHotspot'})
	rows = table.find_all('tr')
	for row in rows:
		cols = row.find_all('td') #whole column
		if row.strong.string == 'Qty Available':#current QOH
			print cols[1].string

def getProducts(myURL):
	html = urllib.urlopen(myURL)
	soup = BeautifulSoup(html)
	table = soup.find('table', attrs={'class':'searchResults'})
	rows = table.find_all('tr', class_=lambda x : x !='legend')
	for row in rows:
		cols = row.find_all('td') #whole colum
		if cols[5].string.strip() in ['low-stock','in-stock']:
			for a in range(0,len(cols)-4): #uncomment to get all data
#			for a in range (1,2): #test to write name ONLY - delete when writing to csv.
				print cols[a].string.strip()
				if a==1:
					getQOH('https://www.thepartysource.com/express/'+cols[a].find('a').get('href'))

	#more product - next page is coming back sorted and is duplicating from the first page and/or missing product completely
	rs = table.find_all('tr', class_=lambda x : x=='legend')
	for r in reversed(rs):
		cs = r.find_all('td')
		try:
			URL = 'https://www.thepartysource.com/express/'+cs[2].find('a').get('href')
			getProducts(URL)
			break
		except:
			break

if __name__ == '__main__':
	main()

