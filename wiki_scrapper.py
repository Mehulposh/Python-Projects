from cgitb import text
import requests
import openpyxl
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'top rated tvshows'
sheet.append(('Show Rank', 'Name', 'Year', 'Rating'))


try:
    source = requests.get("https://www.imdb.com/chart/toptv/")
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')

    shows = soup.find('tbody',class_="lister-list" ).find_all('tr')
    
    for show in shows:
        name = show.find('td', class_ = "titleColumn").a.text
        rank = show.find('td', class_ = "titleColumn").get_text(strip=True).split('.')[0]
        year = show.find('td', class_ = "titleColumn").span.text.strip('()')
        rating = show.find('td', class_ = "ratingColumn imdbRating").strong.text
        print(rank, name, year, rating)
        sheet.append([rank, name, year, rating])
        
except Exception as e:
    print(e)

excel.save('IMDB TV-SHOWS RATING.xlsx')