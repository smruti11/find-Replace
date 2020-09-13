import os
#import xlwt
import glob
import tkinter as tk
import pandas as pd

fil= ""
pth=""
global newf
df = pd.DataFrame()
d=pd.DataFrame()
root=tk.Tk()
myLabel=tk.Label(root,text="Enter absolute path of the file")
myLabel.pack()
name_var = tk.StringVar()

def getFile():
   # fil = name_var
    fil=filePath.get()
    print("hello")
    print(fil)
    pth=os.path.dirname(fil)
    print(pth)
    files=glob.glob(os.path.join(pth,'*.xls*'))
    df=pd.DataFrame()
    for f in files:
        data=pd.read_excel(f)
        df=df.append(data)
    newf=os.path.join(pth,"combiner.xlsx")
    df.to_excel(newf, sheet_name='combined',index=False)    
    df=pd.read_excel(newf, sheet_name="combined")
    print(df)
    find=e2.get()
    rep=e3.get()
    print("path to read from " + str(newf))
    df=pd.read_excel(newf, sheet_name="combined")
    print("df in fnr",df)
    d= df.replace(to_replace=find, value=rep)
    print(d)
    print('completed')
    nef=os.path.join(pth,"export_dataframe.xlsx")
    d.to_excel (nef, index = False, header=True)
 
root.title("Find and Replace")
lab1=tk.Label(root, text="Enter absolute Path")
lab1.pack()
filePath=tk.Entry(root,textvariable = name_var,width=50, font=('calibre',10,'normal')) 
filePath.pack()

lab2=tk.Label(root, text="Find Value")
e2=tk.Entry(root, width=50)
lab3=tk.Label(root, text="Replace with")
e3=tk.Entry(root, width=50)
lab2.pack()
e2.pack()
lab3.pack()
e3.pack()
butn=tk.Button(root,width=20,text="enter path", command=getFile)
butn.pack()
root.mainloop()
