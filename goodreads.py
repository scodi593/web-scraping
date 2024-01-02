import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
html = "https://www.goodreads.com/quotes/"

page = requests.get(html)
page.text

driver = webdriver.Chrome("C:\\Users\\Mohammed\\Desktop\\web-scraping\\chromedriver.exe")
driver.get(html)

time.sleep(3)

soup = BeautifulSoup(driver.page_source,'html.parser')

print(soup.prettify())

driver.close()

results = soup.find(class_='list')

need = {"Quotes":[], "Author":[], "Tags":[]}

tag = soup.find("div",class_="quotes")
quote_list = tag.find_all("div",class_="quote")
tags = quote_list.find_all("div", class_ = "quoteFooter")
for quote in quote_list:
  d = quote.find("div",class_="quoteText")
  author = d.find("span",class_="authorOrTitle")
  req_tags = list(tags)[0].text.replace('\n', '').strip().replace("\t", "")
  need["Quotes"].append(d.text)
  need["Author"].append(author.text)
  need["tags"].append(req_tags)

  
df = pd.DataFrame(need)
df.to_csv("C:/Users/Mohammed/Desktop/web-scraping/Goodreads.com1_data.csv",index=False)
