import requests
from bs4 import BeautifulSoup
import pandas
import math


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
            salary = div.find('div', class_='attribute_snippet').text
        except:
            salary = 'Salary Not Listed'
        summary = div.find('div', class_='job-snippet').text.strip()

        job_posting = {
            'title': job_title,
            'company': company_name,
            'salary': salary,
            'summary': summary
        }
        job_list.append(job_posting)
    return


job_list = []

# for page in range(0, 40, 10):

c = extract(0)
transform(c)

print(job_list)
# data_frame = pandas.DataFrame(job_list)
# print(data_frame.head())
# data_frame.to_csv('jobs.csv')
