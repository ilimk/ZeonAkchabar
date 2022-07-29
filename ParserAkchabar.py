import requests
import json
from bs4 import BeautifulSoup
import csv
import datetime
AkchabarUrl = 'https://www.akchabar.kg/ru/exchange-rates/'

headersForAkchabar = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

reqAkchabar = requests.get(AkchabarUrl, headers = headersForAkchabar)
srcAkchabar = reqAkchabar.text

soup = BeautifulSoup(srcAkchabar, 'lxml')


all_rates = soup.find("table", {"class": "tablesorter table-hover hidden-xs"})

tableAkchabar = []

headers = all_rates.find_all('th')
data = all_rates.find_all('tr')
for i in data:
    tableAkchabar_local = []
    for j in i:
        if j.get('colspan'):
            tableAkchabar_local.append(j.text)
            tableAkchabar_local.append(j.text)
        else:
            tableAkchabar_local.append(j.text)
    tableAkchabar.append(tableAkchabar_local)

with open(str(datetime.datetime.now()) + ".csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(
        tableAkchabar
    )









