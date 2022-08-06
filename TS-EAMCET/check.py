from tkinter import *


import pandas as pd
import toallcolleges
from toallcolleges import prediction
data=pd.read_csv("TSALLCOLLEGESDETAILS.csv")
#print(data["INST CODE"])
allcollegescode=list(set(data["INST CODE"]))
print(len(allcollegescode))
d={}
for l,i,j in zip(data.index,data["INST CODE"],data["INSTITUTE NAME"]):
    d[i]=j
l=[]
for i in d:
    l.append(f'{d[i]}({i})')
#print(l)
def hi(i,k):
    return i*k
employee_list=[]
for i in d:
    employee_list.append((d[i],i,hi(9,8)))

# create root window
root=Tk()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
mylist=Listbox(root,yscrollcommand=Scrollbar.set(self=scrollbar,first=0,last=1),width=100,height=200)
for i in employee_list:
    mylist.insert(END,i)
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
root.mainloop()