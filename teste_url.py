from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://google.com")
bsObj = BeautifulSoup(html,'lxml')
tag = bsObj.find("div",{'id':'pocs2'})
print(tag)
print(tag.get_text())


