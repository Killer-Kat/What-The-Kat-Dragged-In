#Web scraper take 2
#I need to get the value of gold.
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

my_url = "https://www.jmbullion.com/charts/gold-price/"
#this part gets the web page and scrapes it for its html data.
gold_url = urlopen(my_url)
page_html = gold_url.read()
gold_url.close()

page_soup = BeautifulSoup(page_html, "html.parser")
containers = page_soup.findAll("div", {"id": "gounce"})
#this prints the output and extracts the price of gold as a float.
print(containers)
gold_price = float("".join(filter(lambda d: str.isdigit(d) or d == '.', str(containers)))) #dont know how this works, it was written by thund on stack overflow
print(gold_price)
input("end?")