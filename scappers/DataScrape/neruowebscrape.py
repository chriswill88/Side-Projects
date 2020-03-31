#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.reddit.com/"
res = requests.get(URL)
print("response is ->", res.content)

soup = BeautifulSoup(res.text, 'lxml')
funny = soup.find_all('reddit')
print(funny)