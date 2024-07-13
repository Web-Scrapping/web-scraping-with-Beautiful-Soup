import pandas as pd
import requests
from bs4 import BeautifulSoup

'''
    This is a basic web scraping (with BeautifulSoup) program
    we extract from just one webpage
'''

# define the url of the website
url = 'https://books.toscrape.com/'

# send a get request to website and parse the html
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# fetch the container of contents
books = soup.find_all('article', class_='product_pod')

# loop thro content and extract details
reviews = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()

    reviews.append({
        'Title': title,
        'Price': price,
        'Stock Availability': availability
    })

df = pd.DataFrame(reviews)
df.to_csv('reviews-basic.csv', index=False)
