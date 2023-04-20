import httpx
from selectolax.parser import HTMLParser


def get_data(url):
    response = httpx.get(url)
    parser = HTMLParser(response.content)
    h1_elements = parser.css('h1')
    for h1 in h1_elements:
        print(h1.text())
    a_elements = parser.css('a')
    for a in a_elements:
        print(a.attributes['href'])


url = 'https://www.example.com'
get_data(url)
