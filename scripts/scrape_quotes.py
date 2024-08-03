'''
    This is another web scraping (with BeautifulSoup) program
    we extract from all webpages [includes pagination and error handling]
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

# Function to extract details from a webpage
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
                'Tags': ", ".join(quote_tags)
            })
    except AttributeError as e:
        print(f'Attribute Error: {e}')
        return None
    except Exception as e:
        print(f'An error occurred while parsing: {e}')
        return None

    return quotes

# Function to identify and return the URL of the next page
def next_page(soup):
    try:
        button = soup.find('li', class_='next')
        if button:
            return 'https://quotes.toscrape.com' + button.find('a')['href']
    except AttributeError as e:
        print(f'Attribute Error: {e}')
        return None
    except Exception as e:
        print(f'An error occurred while parsing next page: {e}')
        return None
    return None

# Function to collect quotes from all pages
def scrape_all_quotes(index):
    all_quotes = []
    url = index
    while url:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = scrape_quotes(url)
            if quotes:
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

# Save the scraped quotes to a CSV file
df = pd.DataFrame(all_quotes)
df.to_csv('../data/quotes.csv', index=False)
print('Quotes have been successfully scraped and saved to quotes.csv.')
