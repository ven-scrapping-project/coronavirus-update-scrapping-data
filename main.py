#this is a scrapping data bukapalapk

import requests
import csv
from bs4 import BeautifulSoup

class Coronavirus :
    def __init__(self):
        pass
    def srapping_data(self):
        pass
    def tampilkan_data(self):
        pass

url = 'https://www.worldometers.info/coronavirus/country/indonesia/'

r = requests.get(url)
status = r.status_code




if status == 200 :

    after_bs = BeautifulSoup(r.content, 'html.parser')
    # scrapping 1
    country = after_bs.find('div', { 'class' : 'label-counter' } )
    print(country.text.replace('World / Countries /\n', ''))

    # scrapping 2
    find_data = after_bs.find_all(id='maincounter-wrap')
    #print(find_data.prettify())
    #print( find_data.text)
    #print(find_data)
    # text = text.replace('/n', '')

    for i in find_data:
        print(i.text.replace('\n', ''))
else:
    print("url yang anda masukan tidak valid")
