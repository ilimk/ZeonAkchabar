import requests
import json
from bs4 import BeautifulSoup
import csv
import datetime
# AkchabarUrl = 'https://www.akchabar.kg/ru/exchange-rates/'
#
# headersForAkchabar = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
# }
#
# reqAkchabar = requests.get(AkchabarUrl, headers = headersForAkchabar)
# srcAkchabar = reqAkchabar.text

# with open('index.html', 'w') as file:
#     file.write(srcAkchabar)
with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
#tablesorter table-hover hidden-xs tablesorter-default
all_rates = soup.find("div", {"id": "the-content"}) #Находим div у котого id = the_content

all_rates_string =  all_rates.script.text
rates_start_cuts = all_rates_string[all_rates_string.find("{"):] #Находим первый символ = {
reversed_rates_start_cuts = rates_start_cuts[::-1] #переворачиваем его
reversed_rates_end_cuts = reversed_rates_start_cuts[reversed_rates_start_cuts.find(";")+1:] #и у перевернутого текста находим первую смвол = ;
dict_rate = eval(reversed_rates_end_cuts[::-1]) # и еще раз переворачиваем тем самым возвращая его в исходное положение и запускаем его в dict_rate

del dict_rate['nbkr']
list_rates = [['Bank_Name', 'USD_Buy', 'USD_Sell', 'EURO_Buy', 'EURO_sell', 'RUB_Buy', 'RUB_Sell', 'KZT_Buy', 'KZT_Sell']]

for i in dict_rate:
    l = []
    l.append(i)
    for j in dict_rate[i].values():
        for k in j:
            l.append(k)
    list_rates.append(l)

with open(str(datetime.datetime.now()) + ".csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(
        list_rates
    )











