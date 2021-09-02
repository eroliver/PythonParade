import requests
from bs4 import BeautifulSoup


def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/92.0.4515.159 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=junior%20developer&l=Remote&start=10{page}&vjk=1d22fae19e010810'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup
# home user agent Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                             'Chrome/93.0.4577.63 Safari/537.36
# work user agent Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                              'Chrome/92.0.4515.159 Safari/537.36



def transform(soup):
    divs = soup.find_all('div', class_='slider_container')
    # for testing 1 post at a time
    # div = divs[8]
    # company_name = div.find('span', class_='companyName').text.strip()
    # spans = div.find_all('span')
    # for span in spans:
    #     attributes = span.attrs
    #     if 'title' in attributes:
    #         job_title = attributes['title'].strip()
    # print(f'{job_title} : {company_name}')

    for div in divs:
        company_name = div.find('span', class_='companyName').text.strip()
        spans = div.find_all('span')
        for span in spans:
            attributes = span.attrs
            if 'title' in attributes:
                job_title = attributes['title'].strip()
        try:
            salary = div.find('span', class_='salary-snippet').text.strip()
        except:
            salary = 'Not Listed'
        print(f'{job_title} : {company_name} : {salary}')
    return


c = extract(0)
transform(c)
