from bs4 import BeautifulSoup
import requests
page = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(page.text,"html.parser")
tag = soup.find("div",class_ = "col-sm-8 col-md-9");
sec = tag.find("section")
books = sec.find_all("li",class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")
book_list = {}
for book in books:
  name = book.find("h3")
  price = book.find("p",class_ = "price_color")
  avail = book.find("p",class_ = "instock availability")
  b = str(avail.text)
  book_list[name.text] = (price.text,b.strip())

print(book_list)
