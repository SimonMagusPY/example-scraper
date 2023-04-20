import requests
from bs4 import BeautifulSoup


def get_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    h1_elements = soup.find_all('h1')
    for h1 in h1_elements:
        print(h1.text)
    a_elements = soup.find_all('a')
    for a in a_elements:
        print(a.get('href'))


url = 'https://www.example.com'
get_data(url)
