import requests
from requests_html import HTMLSession

# web scraper

page = 1
url = "https://oglobo.globo.com/ultimas-noticias/index/feed/pagina-" + str(page) + ".ghtml"
count = 0

try:
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1, scrolldown=100)
    articles = response.html.find("h2")
    results = []
    

    while (len(results) < 25000):
        # creates array with titles and links
        for heading in articles:
            newsarticle = {
                'title' : heading.text,
                'link' : heading.absolute_links
            }
    
            if ((newsarticle.get('title') != '') and (page > 1)):
                for i in range (len(results) - 32, len(results)):
                    if (newsarticle.get('title') == results[i].get('title')):
                        break
                else:
                    results.append(newsarticle)
                    print(newsarticle)
                    count += 1
            elif (newsarticle.get('title') == ''):
                print(f"Number of articles on this page: {count} Current page: {page}")
                page += 2
                count = 0
                url = f"https://oglobo.globo.com/ultimas-noticias/index/feed/pagina-" + str(page) + ".ghtml"

                response = session.get(url)
                response.html.render(sleep=1, scrolldown=100)
                articles = response.html.find("h2")
            else:
                results.append(newsarticle)
                print(newsarticle)
                count += 1


except requests.exceptions.RequestException as e:
    print(e)

print(f"Total articles scrape: {len(results)}")