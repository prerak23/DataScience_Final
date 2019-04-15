import requests
import re
from bs4 import BeautifulSoup
page=requests.get("https://www.gutenberg.org/browse/authors/p")
soup=BeautifulSoup(page.content, 'html.parser')
main_part=soup.find_all('div',class_="pgdbbyauthor")

dicts={}
x=main_part[0].find_all('h2')
y=main_part[0].find_all('ul')
tofind=str(main_part[0]).replace('<h2>','^').replace('</h2>','^').split('^')
print(tofind)
authors_name=[]
for lx in range(len(tofind)):
    if "</li>" in tofind[lx]:
        print(tofind[lx])
        authors_name.append(re.search(">.*?.<",tofind[lx-1])[0].replace('<','').replace('>',''))


for xkl,klp in zip(authors_name,main_part[0].find_all('ul')):

    for xns in  klp.find_all('li'):

        if "(English)" in xns.get_text():

            if xkl not in dicts:
                dicts[xkl] = [(xns.get_text(),xns.select('a')[0]['href'])]

            else:
                dicts[xkl].append((xns.get_text(),xns.select('a')[0]['href']))


for xn in dicts:
    abc=[]
    for xk in dicts[xn]:
        link_for_download="https://www.gutenberg.org/"+xk[1]

        page2=requests.get(link_for_download)
        soup2=BeautifulSoup(page2.content, 'html.parser')
        tr=soup2.find_all('table',class_="files")

        if tr[0].select('tr'):
            for xpss in tr[0].select('tr'):
                if "Plain Text UTF-8" in str(xpss.select('a')[0]):
                    strss=str(xpss.select('a')[0])

                    hrefno=strss.find('href')+8
                    titleno=strss.find('title')
                    print(xn,xk[0],strss[hrefno:titleno-1])
                    xk=xk+(strss[hrefno:titleno-1],)
                    abc.append(xk)
    dicts[xn]=abc
print(dicts)
with open("links.txt","w+",encoding="utf8") as fof:
    fof.write(str(dicts))
