import requests
from bs4 import BeautifulSoup


def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/93.0.4577.63 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=junior%20developer&l=Remote&start={page}&vjk=1d22fae19e010810'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup):
    divs = soup.find_all('div', class_='slider_container')
    for div in divs:
        if div.span['title'] is not None:
            title = div.span['title']
        print(title)
    return


c = extract(0)
transform(c)
