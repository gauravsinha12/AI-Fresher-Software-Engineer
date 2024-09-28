import requests
from bs4 import BeautifulSoup

# Example of scraping news from NDTV
url = 'https://www.ndtv.com/latest'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all news articles
articles = soup.find_all('div', {'class': 'news_Itm'})

# Print and save the articles
with open('news_articles.txt', 'a') as f:
    for article in articles:
        print(article.text)
        f.write(article.text + '\n')