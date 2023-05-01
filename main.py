import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import csv

stock_data =[]
url = 'https://13f.info/13f/000091341423000035-blackrock-inc-q4-2022'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
response =response.content
soup=BeautifulSoup(response,'html.parser')

data = soup.find_all('table', id_='filingAggregated')

for dada in data:
    name = dada.find('td', class_='truncate group hover:overflow-visible').text
    nom = name.attrs['title']
    shares = data.find('td', class_='text-right').text


    print(nom, shares)

    stock_data.append(name,shares)


print(stock_data)