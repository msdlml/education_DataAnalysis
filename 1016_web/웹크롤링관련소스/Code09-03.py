import bs4

webPage = open('C:/intel/Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

print(bsObject)