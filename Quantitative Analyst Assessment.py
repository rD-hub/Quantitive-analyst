lnk = "https://data.binance.vision/?prefix=data/spot/daily/trades/BTCUSDT/"

from datetime import datetime
import pandas as pd
from selenium import webdriver
import time
from dateutil import parser
import datetime as dt
import requests

chrome_driver_path = "chromedriver.exe"

Traded_price    = []
Traded_notional = []
Timestamp       = []
date = []

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(lnk)
time.sleep(5)

col_1 = driver.find_elements_by_xpath('//*[@id="listing"]/tr/td[1]')
col_2 = driver.find_elements_by_xpath('//*[@id="listing"]/tr/td[2]')
col_3 = driver.find_elements_by_xpath('//*[@id="listing"]/tr/td[3]')

item = [s.text for s in col_1]
size = [s.text for s in col_2]
last_modified = [s.text for s in col_3]

for t in item[1:]:
    res = parser.parse(t, fuzzy=True) 
    date.append(str(res)[:10])


for tsmp in last_modified[1:]:
    tsmp = str[:-5] 
    tsmp.replace("T", " ")
    ts = datetime.timestamp(tsmp)
    Timestamp.append(ts)


pd_table = {
    'date'            : date,
    'Traded Price'    : Traded_price,
    'Traded Size'     : size,                 
    'Traded Notional' : Traded_notional,
    'Timestamp'       : Timestamp
}

df = pd.DataFrame(pd_table)

for x in len(date):
    if df['date'] >= '2020-03-01' or df['date'] < '2020-03-04':
        if df['size'] == '0.1 kb':
            df.drop().x

print(df)
driver.quit()
