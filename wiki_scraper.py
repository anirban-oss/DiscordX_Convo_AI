# wikipedia data science article web scraper
# selecting and collecting all the relevant articles for learning 
# about machine learning, data science and artificial intelligence.

import requests
from bs4 import BeautifulSoup

# Define the URL of the Wikipedia page containing data science articles
url = 'https://en.wikipedia.org/wiki/Category:Data_science'

# Use the requests library to fetch the HTML content of the page
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article links within the page
articles = soup.find_all('div', {'class': 'mw-category'})[0].find_all('a')

# Print the article titles and URLs
for article in articles:
    title = article.text
    link = f"https://en.wikipedia.org{article.get('href')}"
    print(f"{title}: {link}")
