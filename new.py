## Beautiful Soup
    # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-string
    # http://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table


## PLAN:
# Enter search terms and get resulting list back.
    # e.g. https://www.thepartysource.com/express/results.php?i=COCONUT+RUM
# Pass link to get details if availability is "low or in-stock"
# On product page, get info and print or add to array or add to database.

from bs4 import BeautifulSoup
import requests

def main():
    search = raw_input('Enter a search term: ')
    URL = 'https://www.thepartysource.com/express/results.php?o=0&t=&s='+search.replace(' ','+')#+'&sort=invQOH'
    getProducts(URL)
#    URL = 'https://www.thepartysource.com/express/item.php?id=26663'
#    getQOH(URL)

def getProductDetail(myURL):
    html = requests.get(myURL)
    soup = BeautifulSoup(html.text)
    table = soup.find('table', attrs={'class':'itemHotspot'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td') #whole column
        if row.strong.string == 'Qty Available':#current QOH
            print cols[1].string

def getProducts(myURL):
    html = requests.get(myURL)
    soup = BeautifulSoup(html.text)
    table = soup.find('table', attrs={'class':'searchResults'})
    rows = table.find_all('tr', class_=lambda x : x !='legend')
    for row in rows:
        cols = row.find_all('td') #whole colum
        if cols[5].string.strip() in ['low-stock','in-stock']:
            getProductDetail('https://www.thepartysource.com/express/'+cols[1].find('a').get('href'))

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

