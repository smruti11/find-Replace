import pandas as pd
import os
import xlwt
from combine_file import newf

file=newf
df = pd.DataFrame()

df=pd.read_excel(file, sheet_name="combined")
print(df)
# C:\Users\USER\Desktop\python\exfiles\combiner.xlsx
col=input('column name')
find=input('find value')
rep=input('replace with')
 
df= df.replace(to_replace=find, value=rep)

#df=df.replace(to_replace="A",value="D")

print(df)
# df.to_excel(file,sheet_name="fnr")
df.to_excel (newf, index = False, header=True)

