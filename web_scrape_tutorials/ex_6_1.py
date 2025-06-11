#Scrape a single page

from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup)

box = soup.find('article', class_="main-article") 
#underscore is used to avoid conflict with Python's built-in keyword 'class'

title = box.find('h1').get_text()  # get_text() is used to extract text from the HTML element
transcription = box.find('div', class_="full-script").get_text(strip=True, separator=' ')  # strip=True removes leading and trailing whitespace
print(title)
print(transcription)