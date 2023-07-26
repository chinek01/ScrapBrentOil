"""

Portfolio: ScrapBrentOil
#100DaysOfCode with Python
Day: 91
Date: 2023-07-23
Author: MC

"""

from bs4 import BeautifulSoup
import pandas as pd
import requests


# example url
url = "https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=RBRTE&f=M"

response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

table = soup.find('table', attrs={'class': 'FloatTitle'})

data = []

table_head = table.find('thead')
rows = table_head.find_all('tr')

for row in rows:
    cols = row.find_all('th')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])  # Get rid of empty values

table_body = table.find('tbody')

# print(table)

rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])  # Get rid of empty values

# print(data)

df = pd.DataFrame(data)

print(df.head())

df.columns = df.iloc[0]
df = df[1:]

df_nan = df.dropna()

print(df_nan.head())

df_nan.to_csv('data.csv', index=False)

