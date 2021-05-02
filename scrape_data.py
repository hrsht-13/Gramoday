from kora.selenium import wd
import pandas as pd
from tqdm import tqdm

print("enter the current directory")
path=input()

market=['Achnera', 'Agra', 'Fatehabad','Fatehpur+Sikri', 'Jagnair', 'Jarar', 'Khairagarh','Samsabad']
code=['2551','314','2550','2555','2553','2554','2552','2556']

df=pd.DataFrame()
market=['Achnera', 'Agra', 'Fatehabad','Fatehpur Sikri', 'Jagnair', 'Jarar', 'Khairagarh','Samsabad']
for i in tqdm(range(len(market))):
  print(market[i])
  url=("https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=UP&Tx_District=1&Tx_Market="+str(code[i])+"&DateFrom=01-Jan-2020&DateTo=31-Dec-2020&Fr_Date=01-Jan-2020&To_Date=31-Dec-2020&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Uttar+Pradesh&Tx_DistrictHead=Agra&Tx_MarketHead="+str(market[i]))
  wd.get(url)
  wd.find_element_by_id("cphBody_ButtonExcel").click()
  data=pd.read_html(str(path)+"/Agmarknet_Price_Report.xls")
  df=pd.concat([data[0],df],axis=0)
df.to_csv("data.csv",index=False)
