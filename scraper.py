import json
import time
import json
from pprint import pprint
import urllib.parse
import requests
from bs4 import BeautifulSoup



import sqlite3

from sqlite3 import Error

letters = [
    ['Α', 8230, '&lq=Α*&dq='],
    ['Β', 1130, '&lq=Β*&dq='],
    ['Γ', 1250, '&lq=Γ*&dq='],
    ['Δ', 2120, '&lq=Δ*&dq='],
    ['Ε', 4220, '&lq=Ε*&dq='],
    ['Ζ', 370, '&lq=Ζ*&dq='],
    ['Η', 340, '&lq=Η*&dq='],
    ['Θ', 560, '&lq=Θ*&dq='],
    ['Ι', 570, '&lq=Ι*&dq='],
    ['Κ', 4510, '&lq=Κ*&dq='],
    ['Λ', 1070, '&lq=Λ*&dq='],
    ['Μ', 3020, '&lq=Μ*&dq='],
    ['Ν', 960, '&lq=Ν*&dq='],
    ['Ξ', 800, '&lq=Ξ*&dq='],
    ['Ο', 1200, '&lq=Ο*&dq='],
    ['Π', 5180, '&lq=Π*&dq='],
    ['Ρ', 710, '&lq=Ρ*&dq='],
    ['Σ', 3920, '&lq=Σ*&dq='],
    ['Τ', 2040, '&lq=Τ*&dq='],
    ['Υ', 890, '&lq=Υ*&dq='],
    ['Φ', 1410, '&lq=Φ*&dq='],
    ['Χ', 1120, '&lq=Χ*&dq='],
    ['Ψ', 430, '&lq=Ψ*&dq='],
    ['Ω', 140, '&lq=Ω*&dq=']

]


def getwords(page_num, endpoint):
    all_words = []
    baseurl = "https://www.greek-language.gr/greekLang/modern_greek/tools/lexica/triantafyllides/search.html?start="
    for tick in range(0, page_num, 10):
        #time.sleep(0.2)
        URL = baseurl + str(tick) + endpoint
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        for a in soup.findAll('a', href=True):
            a.extract()
        temp_data = soup.find_all("dt")
        for temp1 in temp_data:
            print(str(temp1.text))
            all_words.append(str(temp1.text))
    return all_words

if __name__ == "__main__":
    ALL_DATA = {}

    for i in range(0, len(letters)):
        temp = getwords(letters[i][1], letters[i][2])
        ALL_DATA[letters[i][0]] = temp

    print("Data scrape complete.")
    print("Dumping to \"greek_dictionary.json\"")
    with open('greek_dictionary.json', 'w') as fp:
        json.dump(ALL_DATA, fp, ensure_ascii=False)
