import requests
from bs4 import BeautifulSoup


url = "https://www.nytimes.com/"
r = requests.get(url)

r_html = r.text

soup = BeautifulSoup(r_html, features="lxml")

titles = soup.select('span')

for title in titles:
    print(title.getText())
