from bs4 import BeautifulSoup
import requests

link = input("Copy and paste the youtube link")
youtube = requests.get(link)

soup = BeautifulSoup(youtube.text, 'lxml')
heading = soup.find("title")

film_title = heading.text
print(film_title)