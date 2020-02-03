import ssl

from bs4 import BeautifulSoup
from googlefinance import getQuotes
import json
import sys
import urllib
import re
import pandas as pd
import os
def appendToCSV(df):
    dirpath = os.path.dirname(__file__)
    dirpath = dirpath + '/DataSet/'
    print(dirpath)
    dataset = pd.read_csv(dirpath + "SET 50 Historical Data.csv")
    #dataset = dataset.set_index("Date")
    #dataset = dataset.append(df)
    dataset = pd.concat([pd.DataFrame(dataset),df],ignore_index=True)
    dataset.to_csv("DataSet/SET50Data.csv")
    return 0

def get_quote(symbol):
    base_url = 'https://www.investing.com/indices/set-50-historical-data'
    #context = ssl._create_unverified_context()
    req = urllib.request.Request(base_url,headers={"User-Agent": "Mozilla/5.0"})
    content = urllib.request.urlopen(req).read()

    soup = BeautifulSoup(content)
    m = re.search("genTbl closedTbl historicalTbl.*",soup.decode())
    #print(m)
    if m:
        allText = soup.decode()
        #print(allText)
        timeIND = allText.find("ข้อมูลล่าสุด")
        table = allText.find('class="first left bold noWrap"')
        #print("This table :",table)
        print(allText[table:table + 350])
        set50String = allText[table:table + 351]
        set50String = re.sub(r' <td class="bold redFont">', '\n', set50String)
        set50String = set50String.replace("</td>", "")
        set50String = re.sub(r'<.*>', '', set50String)
        set50String = re.sub(r'^class.*>', '', set50String)
        arrySet50 = set50String.split("\n")
        print("--------------")
        print(set50String)
        print(arrySet50)
        timeUpdatTable = allText[timeIND:timeIND + 35].split(" ")


        #print(timeUpdatTable)
        df = pd.DataFrame({
                        "Date"  :  [arrySet50[0]],
                        "Price"  :  [arrySet50[1]],
                        "Open"  :  [arrySet50[2]],
                        "High"  :  [arrySet50[3]],
                        "Low"  :  [arrySet50[4]],
                        "Vol."  :  [arrySet50[5]],
                        "Change %"  :  [arrySet50[6]],
                           })
        #df = df.set_index("Date")
        appendToCSV(df)
        #print(df)

    return "Fin"
"""    if m:
        quote = m.group(1)
    else:
        quote = 'no quote available for: ' + symbol """

print(get_quote("goog"))
