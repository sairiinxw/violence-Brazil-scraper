import gspread
import random
from google.oauth2.service_account import Credentials

import requests
from requests_html import HTMLSession

# connects to google spreadsheet

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("creds.json",scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1Yrhk75x-urOaxERNbACSQgT6oh-iZEEnxuP3O3Djsh0"
workbook = client.open_by_key(sheet_id)
sheet = workbook.worksheet("Raw Data")

# web scraper

x = 1
url = "https://oglobo.globo.com/ultimas-noticias/index/feed/pagina-" + str(x) + ".ghtml"
try:
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1, scrolldown=100)
    articles = response.html.find("h2")
    # articles = h2

    results = []
    # print (h2[0].text)

    while (len(results) <= 2000):
        # creates array with titles and links
        for heading in articles:
            newsarticle = {
                'title' : heading.text,
                'link' : heading.absolute_links
            }
            results.append(newsarticle)
            print(newsarticle)
            # sheet.update_cell(len(results), 1, 'O Globo')
            # sheet.update_cell(len(results), 2, newsarticle.get('title'))
            # sheet.update_cell(len(results), 3, newsarticle.get('link'))
            # time.sleep(random.randrange(1, 40, 2))
            if (newsarticle.get('title') == ''):
                x = x + 2
                url = "https://oglobo.globo.com/ultimas-noticias/index/feed/pagina-" + str(x) + ".ghtml"

                session = HTMLSession()
                response = session.get(url)
                response.html.render(sleep=2, scrolldown=100)
                articles = response.html.find("h2")

except requests.exceptions.RequestException as e:
    print(e)

print(len(results) - 1)


# print(results[0].title)
# values_list = sheet.row_values(1)
# print(values_list)
