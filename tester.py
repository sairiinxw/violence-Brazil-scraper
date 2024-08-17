import requests
from requests_html import HTMLSession

# web scraper

try:
    url = "https://oglobo.globo.com/opiniao/editorial/coluna/2024/08/pec-da-anistia-e-prova-do-fosso-entre-congresso-e-eleitores.ghtml"
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1, scrolldown=100)
    articleText = response.html.find('div.no-paywall p')
    if articleText == []:
        articleText = response.html.find('div.paywall p')

    cleaning = []

    # adds each individual p class text block from html into the cleaning array (unclean)
    for textblock in articleText:
        cleaning.append(f"{textblock.text}")

    # concatenates individual textblocks into a single textblock without unnecessary website text
    contentBlock = ''
    for b in range (len(cleaning)):
        contentBlock = f"{contentBlock} {cleaning[b]}"

    # # creates a newsarticle object with:
    # # title
    # # link
    # # date - from a cleaning array textblock directly scraped
    # # content - the single contentBlock cleaned

    # newsarticle = {
    #     'title' : heading.text,
    #     'link' : heading.absolute_links,
    #     'date' : cleaning[1],
    #     'content' : contentBlock
    # }

except requests.exceptions.RequestException as e:
    print(e)
