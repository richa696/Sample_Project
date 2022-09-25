import json
import requests
from requests_html import HTMLSession
import schedule
import time
def getWebTableData():
    s=HTMLSession()
    url="https://coinmarketcap.com/"
    r=s.get(url)
    table=r.html.find('table')[0]
    tabledata=[[i.text for i in row.find('td')[2:-2]] for row in table.find('tr')[1:]]
    tableheader=[[i.text for i in row.find('th')[2:-2]] for row in table.find('tr')][0]
    res=[dict(zip(tableheader,t))for t in tabledata]
    for d in res:
        if "1h %" in d:
            d['_1h'] = d.pop('1h %')
        else:
            d['_1h']=""
        if "24h %" in d:
            d['_24h'] = d.pop('24h %')
        else:
            d['_24h']=""
        if "7d %" in d:
            d["_7d"]=d.pop("7d %")
        else:
            d["_7d"]=""
        if "Market Cap" in d:
            d["market_cap"]=d.pop("Market Cap")
        else:
            d["market_cap"]=""
        if "Volume(24h)" in d:
            d["volume"]=d.pop("Volume(24h)")
        else:
            d["volume"]=""
        if "Circulating Supply" in d:
            d["circulating_supply"]=d.pop("Circulating Supply")
        else:
            d["circulating_supply"]=""
        if "Price" not in d:
            d['Price']=""
        
    API_ENDPOINT = "http://localhost:8000/api/saveorupdate/"
    payload=json.dumps({"data":res})
    headers = {"Content-Type": "application/json"}
    # # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = payload, headers=headers)
    print(r)
    
getWebTableData()
    
# schedule.every(4).seconds.do(getWebTableData)
# while 1:
#     schedule.run_pending()
#     time.sleep(1)
    

    
