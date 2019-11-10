#!/usr/bin/env python3
import wikipedia
kl=open("links.txt")
dictio=eval(kl.read())
langs=['en','fr','de','es']
ds_with_author_summary={}
for x in dictio:
    arrs=x.split(',')
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
    print(an)
    summary_with_diffrent_lang=[]
    for y in langs:
        try:
            wikipedia.set_lang(y)
            summary=wikipedia.summary(an)
        except:
            summary=""
        print(summary)
        summary_with_diffrent_lang.append(summary)
    ds_with_author_summary[x]=summary_with_diffrent_lang

with open("summary.txt","w+",encoding='utf8') as fof:
    fof.write(str(ds_with_author_summary))


