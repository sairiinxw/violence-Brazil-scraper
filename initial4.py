import csv
import requests

#LAST RUN: 10/14/25 2:03 PM PST
#scraping text output file: output20.txt
#csv output file: clean_articles20.csv

"""
Begin web scraper program.

Parameters:
    page (int): current page number
    url (string): current url accessed
    count (int): number of articles scraped and cleaned
"""

newspaperName = 'O Globo'
page = 1 # initial page
url = "https://oglobo.globo.com/ultimas-noticias/index/feed/pagina-" + str(page) + ".ghtml" # most recent articles on oglobo
csv_output_file = 'clean_articles20.csv'
scrapeNum = 100 # number of articles you want to scrape


count = 0 # initial count of scraped articles per page
totalcount = 0 # initial count of scraped articles in total

try:
    """
    Initializes an HTML session and accesses url (most recent articles) html to scrape a list of articles

    Parameters:
        articles (String array?): array listing all the article blocks in the url including the names and links, 
            where 'h2' accesses these blocks in the html
        results (Object array): stores the newsarticle objects i.e. cleaned articles with names, links, and article content
    """
    # session = HTMLSession()
    response = requests.get(url)
    html = response.text
    articles = html.split("h2")

    print(articles)
except requests.exceptions.RequestException as e:
    print(e)