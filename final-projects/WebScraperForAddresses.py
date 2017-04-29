# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:49:41 2017

@author: simpl
"""

import pandas as pd
import geopandas as gpd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

data = pd.read_csv(r"C:/Users/simpl/Documents/ds-dc-19/final-projects/Computer_Assisted_Mass_Appraisal__Residential.csv")
geodata = gpd.read_file(r"C:/Users/simpl/Documents/ds-dc-19/final-projects/Computer_Assisted_Mass_Appraisal__Residential.geojson")

geodata.geometry
geodata.plot
geodata.columns
data.shape
# 107374 rows

SSL = data.SSL
address = []

browser = webdriver.Chrome(r'C:\Users\simpl\Documents\ds-dc-19\final-projects\chromedriver.exe')
browser.implicitly_wait(2)
browser.get(r"https://www.taxpayerservicecenter.com/RP_Search.jsp?search_type=Sales")
r = requests.post(url)
b = BeautifulSoup(r.text, "html")
b.find('table',attrs={'width':"100%"}).find_all('tr')[2]
XPATH = u"//*[@id=\"form1\"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]"
query = "PAR%2002510068"

for i in SSL:
    square = SSL[i][:4]
    suffix = SSL[i][4:8]
    lot = SSL[i][8:12]