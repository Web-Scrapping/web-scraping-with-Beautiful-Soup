'''
    This is another web scraping (with BeautifulSoup) program
    we extract from all webpages [includes pagination and error handling]
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

# extract details from webpage
def scrape_quotes(page_url):

    try:
        response = requests.get(page_url)
        response.raise_for_status()

    except RequestException as e:
        print(f'Request Error: {e}')
        return None
    except Exception as e:
        print(f'An Error Occurred: {e}')
        return None


    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = []
        quote_elements = soup.find_all('div', class_='quote')

        for quote_element in quote_elements:
            quote = quote_element.find('span', class_='text').text
            quote_author = quote_element.find('small', class_='author').text
            quote_tags = [tag.get_text() for tag in quote_element.find_all('a', class_='tag')]

            quotes.append({
                'Quote': quote,
                'Author': quote_author,
                'Tags': quote_tags
        })

    except AttributeError as e:
        print(f'Attribute Error: {e}')
        return None

    except Exception as e:
        print(f'An error occurred while parsing: {e}')
        return None

    return quotes

# goto next page
def next_page(soup):

    try:
        button = soup.find('li', class_='next')
        if button:
            return 'https://quotes.toscrape.com' + button.find('a')['href']

    except AttributeError as e:
        print(f'Attribute Error: {e}')
        return

    except Exception as e:
        print(f'An error occurred while parsing next page: {e}')
        return None

    return print('We have exhausted all the pages')

# put all quotes together
def scrape_all_quotes(index):
    all_quotes = []
    url = index
    while url:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = scrape_quotes(url)
            all_quotes.extend(quotes)
            url = next_page(soup)

        except RequestException as e:
            print(f'Request error: {e}')
            break

        except Exception as e:
            print(f'An error occurred: {e}')
            break

    return all_quotes

index = 'https://quotes.toscrape.com/'
all_quotes = scrape_all_quotes(index)

# print all the scraped quotes
for quote in all_quotes:
    print(f'"{quote["Quote"]}" - {quote["Author"]}')
    print(f'Tags: {", ".join(quote["Tags"])}')
    print('-' * 120)


