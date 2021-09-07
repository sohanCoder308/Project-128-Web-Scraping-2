from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(START_URL)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

temp_list= []
table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

constellation = []
right_ascension = []
declination = []
app_mag = []
distance = []
spectral_type = []
brown_dwarf = []
mass = []
radius = []
discovery_year = []

for i in range(1, len(temp_list)):
    constellation.append(temp_list[i][1])
    right_ascension.append(temp_list[i][2])
    declination.append(temp_list[i][3])
    app_mag.append(temp_list[i][4])
    distance.append(temp_list[i][5])
    spectral_type.append(temp_list[i][6])
    brown_dwarf.append(temp_list[i][0])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
    discovery_year.append(temp_list[i][9])

dataFrame = pd.DataFrame(list(zip(constellation, right_ascension, declination, app_mag, distance, spectral_type, brown_dwarf, mass, radius, discovery_year)),
                columns=["constellation", "right_ascension", "declination", "app_mag", "distance", "spectral_type", "brown_dwarf", "mass", "radius", "discovery_year"])
print(dataFrame)

dataFrame.to_csv('brown_dwarfs_final_data.csv')