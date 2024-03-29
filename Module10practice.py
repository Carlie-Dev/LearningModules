#import calc
# from calc import calculator
# my_num1 = 10
# my_num2 = 15

# #prints 25
# print(calculator.add(my_num1,my_num2))

#Importing library
import requests
from bs4 import BeautifulSoup

#Set url of page
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

#Send a get request to the webpage
response = requests.get(url)

#Parsing the html of the webpage
soup = BeautifulSoup(response.text)

#Find the hyper links with the text and replace the link with the text
for a_tag in soup.find_all('a'):
    a_tag.replace_with(a_tag.text)

tables = soup.find_all('table')
if len(tables) > 1:
    table = tables[1]
else:
    table = tables[0]

#initialize list to hold straight data
table_data = []

#extract table headers and add to list
headers = []
for header in table.find_all('th'):
    headers.append(header.text.strip())

table_data.append(headers)

#Extracting rows from the table
for row in table.find_all('tr'):
    cells = []
    for cell in row.find_all('td'):
        cell_data = str(cell.text.strip())
        #Instead of pulling a space it will pull this
        cell_data.replace('\\xao',' ')
        cells.append(cell_data)

    if cells: #If cells is not null
        table_data.append(cells)

for row in table_data:
    print(row)