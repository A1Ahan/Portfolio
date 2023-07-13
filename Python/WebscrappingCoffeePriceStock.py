#Import Libraries/Tools
import requests
from bs4 import BeautifulSoup
import pandas as pd


#Creating URL and Utilizing BeautifulSoup
url = 'https://www.macrotrends.net/2535/coffee-prices-historical-chart-data'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


#Creating the variable and identifying the Data Location
data = soup.find('table',{'class','table'}).find('tbody').find_all('tr')
data
len(data)


#Year
data[0].find_all('td')[0].get_text()
#Average Closing Price
data[0].find_all('td')[1].get_text()
#Year Open
data[0].find_all('td')[2].get_text()
#Year High
data[0].find_all('td')[3].get_text()
#Year Low
data[0].find_all('td')[4].get_text()
#Year Close
data[0].find_all('td')[5].get_text()
#Annual % Change
data[0].find_all('td')[6].get_text()


#Creating Dataset for Analysis
Year = []
Average_Closing_Price = []
Year_Open = []
Year_High = []
Year_Low = []
Year_Close = []
Annual_Percent_Change = []

for i in data:
    #Year
    Year.append(i.find_all('td')[0].get_text())
   #Average_Closing_Price
    Average_Closing_Price.append(i.find_all('td')[1].get_text())
    #Year Open
    Year_Open.append(i.find_all('td')[2].get_text())
    #Year High
    Year_High.append(i.find_all('td')[3].get_text())
    #Year Low
    Year_Low.append(i.find_all('td')[4].get_text())
    #Year Close
    Year_Close.append(i.find_all('td')[5].get_text())
    #Annual Percent Change
    Annual_Percent_Change.append(i.find_all('td')[6].get_text())
    
coffee_df = pd.DataFrame({'Year':Year,'Average Closing Price': Average_Closing_Price, 'Year Open':Year_Open, 'Year_High':Year_High,
                  'Year Low':Year_Low,'Year Close':Year_Close,'Annual Percent Change':Annual_Percent_Change})
                  
#Create Excel File for access
coffee_df.to_excel('Coffee_PriceStock.xlsx',index=False)                  
    
