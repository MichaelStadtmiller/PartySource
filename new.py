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
#    search = raw_input('Enter a search term: ')
    search = 'Four Roses'
    URL = 'https://www.thepartysource.com/express/results.php?o=0&t=&s='+search.replace(' ','+')#+'&sort=invQOH'
    getProducts(URL)
#    URL = 'https://www.thepartysource.com/express/item.php?id=26663'
#    getQOH(URL)

def getPriceQOH(myURL):
    html = requests.get(myURL)
    soup = BeautifulSoup(html.text)
    
    #get Price/QOH
    table = soup.find('table', attrs={'class':'itemHotspot'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if row.strong.string == 'Price:':
            try:
                price = row.strong.find_next_sibling("font").string.strip()
            except:
                price = cols[0].next_element.next_element.next_element.strip()
        if row.strong.string == 'Qty Available':#current QOH
            QOH = cols[1].string.strip()
    print 'Price: ' + price
    print 'QOH: ' + QOH

def getProductDetail(myURL):
    html = requests.get(myURL)
    soup = BeautifulSoup(html.text)
    table = soup.find('table', attrs={'class':'itemDisplay'})
    rows = table.find_all('tr')

    name = rows[0].find('strong').string
    #Image and Description
    cols = rows[7].find_all('td')
    img=cols[0].find('img')['src']
    desc=cols[1].string

    category = rows[8].find_all('a')[0].string
    origin = rows[8].find_all('a')[1].string
    classi = rows[9].find_all('a')[0].string
    region = rows[9].find_all('a')[1].string
    prodtype = rows[10].find_all('a')[0].string
    ABV = rows[10].find_all('a')[1].string
    style = rows[11].find_all('a')[0].string
    size = rows[11].find_all('a')[1].string
    age = rows[13].find_all('a')[0].string
    container = rows[13].find_all('a')[1].string
    brand = rows[14].find_all('a')[0].string 
    
    print 'name: ' + name
    print img
    print desc
    print category
    print origin
    print classi
    print region
    print prodtype
    print ABV
    print style
    print size
    print age
    print container
    print brand

def getProducts(myURL):
    html = requests.get(myURL)
    soup = BeautifulSoup(html.text)
    table = soup.find('table', attrs={'class':'searchResults'})
    rows = table.find_all('tr', class_=lambda x : x !='legend')
    for row in rows:
        cols = row.find_all('td') #whole colum
        if cols[5].string.strip() in ['low-stock','in-stock']:
            getPriceQOH('https://www.thepartysource.com/express/'+cols[1].find('a').get('href'))
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

