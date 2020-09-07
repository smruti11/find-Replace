import pandas as pd 
import os
import glob

file=input(' combined file path: ')
#C:\Users\USER\Desktop\python\exfiles\tester.xlsx
# C:\Users\USER\Desktop\python\exfiles
pth=os.path.dirname(file)
print('path is ',pth)

extension=os.path.splitext(file)[1]
print('extension is ',extension)
fileName=os.path.splitext(file)[0]
print('name of file is ',fileName)
files=glob.glob(os.path.join(pth,'*.xls*'))
newf=os.path.join(pth,"combiner.xlsx")
df=pd.DataFrame()
for f in files:
    data=pd.read_excel(f)
    df=df.append(data)

df.to_excel(newf, sheet_name='combined',index=False)
print('completed')
fnr='C:\\Users\\USER\\Desktop\\python\\fnr.py'
#os.system(fnr)