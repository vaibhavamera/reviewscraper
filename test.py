from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

searchString = "iphone"
flipkart_url = "https://www.flipkart.com/search?q=" + searchString
uClient = uReq(flipkart_url)
flipkartPage = uClient.read()
uClient.close()
flipkart_html = bs(flipkartPage, "html.parser")
bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
del bigboxes[0:3]
box = bigboxes[0]
productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
prodRes = requests.get(productLink)
prodRes.encoding='utf-8'
prod_html = bs(prodRes.text, "html.parser")
print(prod_html)
commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

filename = searchString + ".csv"
fw = open(filename, "w")
headers = "Product, Customer Name, Rating, Heading, Comment \n"
fw.write(headers)
reviews = []