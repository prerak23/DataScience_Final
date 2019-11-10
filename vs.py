import pandas as pd
text=open("big_file.txt",encoding="utf8")
text_dict=eval(text.read())
pds=pd.DataFrame.from_dict(text_dict)
pds.to_pickle("big_text.pkl")
