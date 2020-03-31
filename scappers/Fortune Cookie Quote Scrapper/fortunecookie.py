#!/usr/bin/python3
import tkinter as tk
import requests
from bs4 import BeautifulSoup

a = requests.get("http://www.fortunecookiemessage.com/")
soup = BeautifulSoup(a.text, 'html.parser')
phrase = soup.find(class_='cookie-link').get_text()

root = tk.Tk()
T = tk.Text(root, height=2, width=40)
T.pack()
T.insert(tk.END, f"{phrase}")
tk.mainloop()
