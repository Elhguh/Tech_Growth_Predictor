import requests
from bs4 import BeautifulSoup

import pandas as pd
import sqlite3


stock_data =[]

url = f'https://13f.info/13f/000091341423000035-blackrock-inc-q4-2022'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
soup=BeautifulSoup(response.content,'html.parser')

data = soup.find_all('tr', class_=['bg-gray-50 even:bg-white hover:bg-gray-200 odd', 'bg-gray-50 even:bg-white hover:bg-gray-200 even'])

for dada in data:
    name = dada.findall('td', class_="truncate group hover:overflow-visible")
    company = name.attrs['title']

    shares = data.get('td', class_='text-right').text

    print(name, company, shares)

    stock_data.append([name,company, shares])


print(stock_data)

df = pd.DataFrame(stock_data,['Company','Shares'])
df.to_csv(f'blackRock_holdings.csv')


# Read in the CSV file using pandas
df = pd.read_csv('blackrock_holdings.csv')

# Connect to the SQLite database
conn = sqlite3.connect('blackrock_holdings.db')

# Write the DataFrame to a SQLite table
df.to_sql('holdings', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()
