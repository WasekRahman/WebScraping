

import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/List_of_sovereign_states')

soup = bs4.BeautifulSoup(res.text,'lxml')
#print(soup.prettify())
hi = soup.find_all('b')
for i in hi:
    try:
     print(i.a.text)
    except:
        n =0