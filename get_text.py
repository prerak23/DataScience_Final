#!/usr/bin/env python3 
import requests
from bs4 import BeautifulSoup
#import pymongo
kl=open("links.txt")
dictio=eval(kl.read())
big_arr=[]
#myclient=pymongo.MongoClient('mongodb://localhost:27017/')
#mydb=myclient["exam_datascience"]
#mycol=mydb['authors_book_text']
#example={'author_name':"Prerak",'written_books':['la vie de etudiant en France'],'text_of_the_books':['Bonjour !']}
#x=mycol.insert_one(example)
#print(x)
ii=0
for x in dictio:

    arrs=x.split(',')
    text_book = []
    book_name = []
    an=""
    if len(arrs) > 1 :
        if '(' in arrs[1]:
            first_name_start=arrs[1].find('(')
            first_name_end=arrs[1].find(')')
            first_name=arrs[1][first_name_start+1:first_name_end]
            first_name_arr=first_name.split(" ")
            first_name=" ".join(first_name_arr)
            an=first_name+" "+arrs[0]
        else:
            first_name_arr = arrs[1].strip().split(" ")
            first_name = " ".join(first_name_arr)
            an=first_name+" "+ arrs[0]
    else:
        an=x
    ii+=1
    print(ii)
    print(an)
    for y in dictio[x]:
    
        ls=len(y[2])
        urlss="http://"+y[2][:ls-1]
        
        page2 = requests.get(urlss)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        the_text=soup2.get_text()
        
        goo=the_text.find('***START OF THE PROJECT GUTENBERG EBOOK')
        start_book=goo if goo > 0 else the_text.find('*** START OF THIS PROJECT GUTENBERG EBOOK')
        foo=the_text.find('*** END OF THIS PROJECT GUTENBERG EBOOK ')
        end_book=foo if foo > 0 else the_text.find('***END OF THE PROJECT GUTENBERG EBOOK ')
        the_book_text=the_text[start_book:end_book]
        print(the_book_text)
        book_name.append(y[0])
        text_book.append(the_book_text)
    #mycol.insert_one()
    big_arr.append({'author_name':an,'written_books':book_name,'text_of_the_books':text_book})
with open("big_file.txt","w+",encoding="utf8") as fof:
    fof.write(str(big_arr))
