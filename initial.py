import gspread
from google.oauth2.service_account import Credentials

import requests
from requests_html import HTMLSession

# google spreadsheet initialization (connected to program)

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("creds.json",scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1Yrhk75x-urOaxERNbACSQgT6oh-iZEEnxuP3O3Djsh0"
workbook = client.open_by_key(sheet_id)
sheet = workbook.worksheet("Raw Data")

"""
Begin web scraper program.

Parameters:
    page (int): current page number
    url (string): current url accessed
    count (int): number of articles scraped and cleaned
"""

page = 1 # initial page
url = "https://oglobo.globo.com/ultimas-noticias/index/feed/pagina-" + str(page) + ".ghtml" # most recent articles on oglobo
count = 0 # initial count of scraped articles

try:
    """
    Initializes an HTML session and accesses url (most recent articles) html to scrape a list of articles

    Parameters:
        articles (String array?): array listing all the article blocks in the url including the names and links, 
            where 'h2' accesses these blocks in the html
        results (Object array): stores the newsarticle objects i.e. cleaned articles with names, links, and article content
    """
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1, scrolldown=100)
    articles = response.html.find("h2")
    results = [] # initial array

    """
    Scraping, cleaning, and adding articles to the results array

    Parameters:
        heading (String): individual String element i.e. individual article in html in the articles array 
        articleText (String): list of each p class html text block on the article webpage i.e. the article content
        cleaning (String array): array of the previously comma-separated list of Strings from articleText
        contentBlock: cleaned up 1 paragraph version of all the Strings in the cleaning array (no ads, redundant info, etc.)
    """
    for heading in articles:
        if (len(results) < 2500): # adjusts number of articles to scrape

            # creates a newsarticle object with: title, link, and content - the single contentBlock cleaned, but currently empty
            newsarticle = {
                'newspaper' : 'O Globo',
                'title' : heading.text,
                'link' : heading.absolute_links,
                'content' : ''
            }

            # checks that a non-empty newsarticle object on page 2+ is not a duplicate of a previous article; if non-duplicate -> appends to results and increases count
            if ((newsarticle.get('title') != '') and (page > 1)):
                for i in range (len(results) - 32, len(results)):
                    if (newsarticle.get('title') == results[i].get('title')):
                        break
                else:
                    results.append(newsarticle)
                    sheet.update_cell(len(results) + 1, 1, newsarticle.get('newspaper'))
                    sheet.update_cell(len(results) + 1, 2, newsarticle.get('title'))
                    sheet.update_cell(len(results) + 1, 3, ''.join(newsarticle.get('link')))
                    # count += 1
            # if the current newsarticle is empty, this indicates that there are no more articles on the current page; renders a new url of most recent articles 2 pages ahead
            elif (newsarticle.get('title') == ''):
                print(f"Number of articles on this page: {count} Current page: {page}")
                page += 2
                # count = 0
                url = f"https://oglobo.globo.com/ultimas-noticias/index/feed/pagina-" + str(page) + ".ghtml"

                response = session.get(url)
                response.html.render(sleep=1, scrolldown=100)
                articles.clear()
                articles = response.html.find("h2") # reassigns article array
            # appends non-empty article otherwise and increases count
            else:
                results.append(newsarticle)
                sheet.update_cell(len(results) + 1, 1, newsarticle.get('newspaper'))
                sheet.update_cell(len(results) + 1, 2, newsarticle.get('title'))
                sheet.update_cell(len(results) + 1, 3, ''.join(newsarticle.get('link')))
                # count += 1
        else:
            break
    
    for a in range (len(results)):
        # changes url and renders a page of each individual article one-by-one based on the list of articles (with titles and links)
        url = ''.join(results[a].get('link'))
        response = session.get(url)
        response.html.render(sleep=1, scrolldown=100)
        articleText = response.html.find('div.no-paywall p') # where the article content is without redundant info (basically clean)
        if articleText == []:
            articleText = response.html.find('div.paywall p') # alternative when the div class name is paywall, not no-paywall -> may run into potential other class names (untested)
        cleaning = [] 
        
        # adds each individual p class text block from html into the cleaning array (unclean)
        for textblock in articleText:
            cleaning.append(f"{textblock.text}")
        
        # concatenates individual textblocks into a single textblock without unnecessary website text
        contentBlock = ''
        for b in range (len(cleaning)):
            contentBlock = f"{contentBlock} {cleaning[b]}"
        
        results[a]['content'] = contentBlock
        sheet.update_cell(a + 2, 4, results[a].get('content'))
        count += 1
        articleText.clear()
        
    
    print(f"Total articles scraped: {len(results)} Total number counted: {count}")

except requests.exceptions.RequestException as e:
    print(e)

# print(results[0].title)
# values_list = sheet.row_values(1)
# print(values_list)
