# Web Scraping Project: Quotes Scraper

## Overview

This project involves web scraping to extract quotes from a website using Python. The primary script, `scrape_quotes.py`, 
is designed to efficiently collect quotes from multiple pages of a website, handling pagination and errors robustly. 
This script demonstrates how to perform web scraping, manage HTTP requests, and process HTML content to gather data.

## Project Structure

The project is organized as follows:

```
web-scraping/
├── scripts/
│   ├── scrape_quotes.py
├── data/
│   ├── quotes.csv
├── README.md
├── requirements.txt
```

- **`scripts/scrape_quotes.py`**: The main script for scraping quotes from the website.
- **`data/quotes.csv`**: The output CSV file containing the scraped quotes.
- **`README.md`**: This file, providing an overview and instructions for the project.
- **`requirements.txt`**: This file lists all the dependencies required to run the script

## Setup

### Prerequisites

Ensure you have the following packages installed:

- `pandas==1.3.3`
- `requests==2.26.0`
- `beautifulsoup4==4.10.0`

You can install these dependencies using the following command:

```sh
pip install requirements.txt
```


## Purpose

The goal of the `scrape_quotes.py` script is to extract quotes from the "Quotes to Scrape" website, which features 
various quotes along with their authors and associated tags. The script is designed to:

1. **Scrape Data**: Collect quotes, authors, and tags from multiple pages.
2. **Handle Pagination**: Navigate through all available pages on the website.
3. **Manage Errors**: Implement error handling to manage network issues and parsing errors.
4. **Save Data**: Output the collected data into a CSV file for further analysis or use.

## Features

### 1. Data Extraction

The script extracts the following details from each quote:
- **Quote**: The text of the quote.
- **Author**: The person who authored the quote.
- **Tags**: Keywords associated with the quote.

### 2. Pagination Handling

The script is capable of navigating through multiple pages of quotes. It automatically follows the "Next" link to 
continue scraping until all pages have been processed.

### 3. Error Handling

To ensure reliability, the script includes:
- **Retry Mechanism**: Automatically retries failed requests with exponential backoff.
- **Error Reporting**: Prints informative error messages for connection issues or parsing errors.

### 4. Output

The collected data is saved in a CSV file named `quotes.csv` located in the `data` directory. This file contains all the 
quotes, authors, and tags gathered from the website.

## Installation

To use the script, follow these steps:

1. **Clone the Repository**: 
    ```sh
    git clone https://github.com/mrowurakwarteng/Web-Scrapping/web-scraping-with-Beautiful-Soup.git
    cd web-scraping-with-Beautiful-Soup
    ```

2. **Install Required Packages**: Ensure you have the necessary Python packages installed.
    ```sh
    pip install requirements.txt
    ```

## Usage

### Running the Script

1. **Navigate to the Scripts Directory**:
    ```sh
    cd scripts
    ```

2. **Execute the Script**:
    ```sh
    python scrape_quotes.py
    ```

3. **Check the Output**: 
   - After execution, the scraped quotes will be saved in `../data/quotes.csv`.

### What to Expect

Upon successful execution, the script will:
- Print each quote along with its author and tags to the console.
- Save the complete dataset in a CSV file for easy access and analysis.

## Troubleshooting

- **Connection Errors**: If you encounter connection errors, check your internet connection and try running the script 
    again. The script includes retry logic to handle temporary issues.
- **Parsing Errors**: If the website's structure changes, the script might not work as expected. In such cases, review 
    and update the parsing logic in the script.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request 
with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

---
