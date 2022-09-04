from bs4 import BeautifulSoup
import requests, openpyxl

excelFile = openpyxl.Workbook()
# printing the below to know how many sheets are active
print(excelFile.sheetnames)
# choosing the active sheet to work on
activeSheet = excelFile.active
# giving a title to the active sheet
activeSheet.title = '2022 Top World 200 Universities'
print(excelFile.sheetnames)
# creating columns for the active sheet
activeSheet.append(['RANK', 'UNIVERSITY', 'COUNTRY', 'COUNTRY ABBRV'])
try:
    # requesting the url of the website to scrap
    source = requests.get('https://www.4icu.org/top-universities-world/')
    source.raise_for_status()

    # get all the source code from the webiste
    getHMTLCODE = BeautifulSoup(source.text,'html.parser')

    #  filter out  the table elements of the html page which carries the data to be scrapped
    universities = getHMTLCODE.find('tbody').find_all('tr')

    for university in universities:
        name = university.find_all('td')[1].a.text
        rank = university.find_all('td')[0].b.text
        country = university.find_all('td')[2].text
        for Text in university.find_all('img', alt=True):
            break
        CountryName= Text['alt']
        print(rank, name, CountryName)
        activeSheet.append([rank, name, CountryName, country])
except Exception as e:
    print(e)
    # saving the file as an Excel File
excelFile.save('2022 Top World Universities.xlsx')