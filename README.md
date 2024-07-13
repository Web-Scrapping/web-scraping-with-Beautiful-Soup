# Web Scraping Projects

This repository contains two web scraping projects demonstrating the use of Beautiful Soup and Requests to extract data from two different websites. 
The first project involves scraping quotes from the website [Quotes to Scrape](http://quotes.toscrape.com), including pagination and error handling. 
The second project involves scraping book information from the homepage of [Books to Scrape](http://books.toscrape.com).

## Project 1: Quotes to Scrape

### Description

In this project, we scrape quotes, authors, and tags from [Quotes to Scrape](http://quotes.toscrape.com). The project demonstrates how to handle pagination to 
scrape data from multiple pages and includes error handling to manage potential issues during the scraping process.

### Features

- **Pagination Handling**: Automatically navigates through multiple pages to scrape all quotes.
- **Error Handling**: Robust error handling for network requests and HTML parsing to ensure the script can manage various issues gracefully.

### Files

- `scrape_quotes.py`: The main script for scraping quotes, authors, and tags from [Quotes to Scrape](http://quotes.toscrape.com).

### Sample Output
`"Your time is limited, so don't waste it living someone's life." - Steve Jobs`<br>
`Tags: life, inspirational`

--------------------------------------------------------------------------------
`"It is our choices, Harry, that show what we truly are, far more than our abilities." - J.K. Rowling` <br>
`Tags: abilities, choices`

--------------------------------------------------------------------------------
...


## Project 2: Books to Scrape

### Description

This project involves scraping book titles, prices, and availability information from the homepage of [Books to Scrape](http://books.toscrape.com). It demonstrates the basics of web scraping using Beautiful Soup and Requests libraries, focusing on extracting data from a straightforward HTML structure.

### Features

- **Basic Scraping**: Extracts book titles, prices, and availability from the homepage.
- **Simple HTML Parsing**: Illustrates how to parse and extract data from a simple HTML layout.

### Files

- `scrape_books.py`: The main script for scraping book information from the homepage of [Books to Scrape](http://books.toscrape.com).

### Sample Output
Title: A Light in the ...<br>
Price: £51.77<br>
Availability: In stock (22 available)

--------------------------------------------------------------------------------
Title: Tipping the Velvet<br>
Price: £53.74<br>
Availability: In stock (20 available)

--------------------------------------------------------------------------------
...
