from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/National_Basketball_Association')
bs = BeautifulSoup(html,'lxml')

tag = bs.findAll('table',{'class' : 'navbox wikitable','style' : 'width:100%; text-align:left'})
print(tag[0]('tr')[0](['td','th']))

#for t1 in tag[0].children:
#    print(t1)
#    #input('pausa')
