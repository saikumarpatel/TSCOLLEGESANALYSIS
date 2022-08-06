from tkinter import ttk
from tkinter import *
import os
from tkinter.ttk import Combobox

import speech_recognition as sr
import pyttsx3
import pandas as pd
from PIL import Image, ImageTk
#import topdwon

background = "white"

branchdict={"OC","BC-A","BC-B","BC-C","BC-D","BC-E","SC","ST"}

def goto():
    global r,clicked,root1,category,branchbox
    caste=category.get()
    rank=l2.get()
    s = caste.replace("-", "")
    s=s.replace("_","")
    path = f"Eamcet analysis\\{branch.get()}" + "_2022.csv"
    print(path,rank,caste,branch.get())
    #Q=category.get()

    if caste=="BC_E" or  caste=="PH":
        data=pd.read_csv(path)
        count=0
        total=1
        m=100000
        M=0
        for i,j in zip(data["Eamcet Rank"],data["Category"]):
            print(type(i),i)
            if caste in j:
                m=min(m,int(i))
                M=max(M,int(i))
                if int(rank)<int(i):
                    count+=1
                total+=1
            print(count,total,m,M)
        minmum=Frame(root,width=300,height=150,background="#D3D3D3").place(x=50,y=500)
        Label(minmum,text="prediction Per%",font=("BOLD",16)).place(x=50,y=550)
        Label(minmum, text=round(count*100/total,3), font=("BOLD", 16)).place(x=250, y=550)
        #Label(minmum, text=Q, font=("BOLD", 16)).place(x=50, y=550)
        #Label(minmum, text=Q, font=("BOLD", 16)).place(x=50, y=550)


    else:
        #print(r.get())
        #category = ["OC", "BC-A", "BC-B", "BC-C", "BC-D", "SC", "ST"]

        #branches = ["CSE", "ME", "IT", "ECE", "CIVIL", "EEE"]
        OCM = []
        OCF = []
        BCAM = []
        BCAF = []
        BCBM = []
        BCBF = []
        BCCM = []
        BCCF = []
        BCDM = []
        BCDF = []
        SCM = []
        SCF = []
        STM = []
        STF = []
        dict = {"OCM": OCM, "OCF": OCF, "BCAM": BCAM, "BCAF": BCAF, "BCBM": BCBM, "BCBF": BCBF, "BCCM": BCCM, "BCCF": BCCF,
                "BCDM": BCDM, "BCDF": BCDF,
                "SCM": SCM, "SCF": SCF, "STM": STM, "STF": STF}

        data = pd.read_csv(path)
        #print(data)
        # print(data.get("Sex"))

        for i, j, k in zip(data.get("Sex"), data.get("Caste"), data.get("Eamcet Rank")):

            if i == "M":
                print(i, j, k)
                if j == "OC":
                    OCM.append(k)
                if j == "BC_A":
                    BCAM.append(k)
                if j == "BC_B":
                    BCBM.append(k)
                if j == "BC_C":
                    BCCM.append(k)
                if j == "BC_D":
                    BCDM.append(k)
                if j == "SC":
                    SCM.append(k)
                if j == "ST":
                    STM.append(k)
            else:
                print(i, j, k)
                if j == "OC":
                    OCF.append(k)
                if j == "BC_A":
                    BCAF.append(k)
                if j == "BC_B":
                    BCBF.append(k)
                if j == "BC_C":
                    BCCF.append(k)
                if j == "BC_D":
                    BCDF.append(k)
                if j == "SC":
                    SCF.append(k)
                if j == "ST":
                    STF.append(k)
        if r.get()==1:
            s=s+"M"
        else:
            s=s+"F"
        M=dict[s]
        count=0
        M=[int(i) for i in M]
        z=0
        print(M)

        for i in M:
            if int(rank)<int(i):
                count+=1
            z=round(count*100/(len(M)),3)
        if len(M)>0:
            minimum=Frame(root,width=300,height=150,background="#D3D3D3").place(x=50,y=500)
            Label(minimum,text="Highest Rank",font=("BOLD",16),borderwidth=2).place(x=50,y=500)
            Label(minimum,text=min(M),font=("BOLD",16),borderwidth=2).place(x=250,y=500)
            Label(minimum, text="Last Rank",font=("BOLD",16),borderwidth=2).place(x=50, y=550)
            Label(minimum, text=max(M),font=("BOLD",16),borderwidth=2).place(x=250, y=550)
            Label(minimum, text="Prediction Per%", font=("BOLD", 16),borderwidth=2).place(x=50, y=600)
            Label(minimum, text=z, font=("BOLD", 16),borderwidth=2).place(x=250, y=600)
        else:
            Label(root1,text="No records Available",font=("BOLD", 16)).place(x=50,y=500)
        #Label(minimum,text=len(M),font=("BOLD", 16)).place(x=50,y=650)
        #print(BCCM,BCCF)


if __name__=="__main__":
    root=Tk()
    root.title("A.Y-2021-22 GRIET EAMCET RANK ALLOTED STUDENTS DETAILS")
    w_width, w_height = 520, 700
    s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
    root.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))  # center location of the screen
    root.configure()

    G_img=Image.open("img.png")
    G_img=G_img.resize((500,80))
    G_img=ImageTk.PhotoImage(G_img)
    root1=Frame(root,width=550,height=700,background="lightblue")
    root1.grid(row=0,column=0)
    root1.pack()
    Label(root1, image=G_img).place(x=10,y=5)
    l1 = Label(root1, text="Eamcet Rank",font=("BOLD",16)).place(x=50, y=120)
    l2=StringVar()
    l2 = Entry(root1,width=13,font=("BOLD",16),relief=FLAT)
    l2.place(x=250, y=120)
    l3 = Label(root1, text="Branch",font=("BOLD",16)).place(x=50, y=180)
    """branch=StringVar()
    branch.set("         ")"""
    branchbox = Combobox(root1, font=("BOLD", 10))
    branchbox['values']=("   ", "CSE", "CSE_AIML", "CSE_DS", "CSE_CSBS", "MEC", "IT", "ECE", "EEE", "CIVIL")
    branchbox.current(0)
    branchbox.place(x=250, y=180)
    l21 = Label(root1, text="Category", font=("BOLD", 16)).place(x=50, y=240)
    """licked = StringVar()
    clicked.set("         ")
    l22 = OptionMenu(root1, clicked, *category).place(x=250, y=280)"""
    category=Combobox(root1,font=("BOLD", 10))
    category['values']=("   ","OC","BC_A","BC_B","BC_C","BC_D","BC_E","SC","ST","PH")
    category.current(0)
    category.place(x=250,y=240)
    """Label(root1,text="Quota",font=("BOLD", 16)).place(x=50,y=300)
    Quota=Combobox(root1,font=("BOLD", 10))
    Quota['values'] = ("     ","PH", "EWS","CAP", "Other")
    Quota.current(0)
    Quota.place(x=250,y=300)"""
    l5 = Label(root1, text="Gender",font=("BOLD",16)).place(x=50, y=300)
    r = IntVar()
    s = ttk.Style()
    s.configure('Wild.TRadiobutton', background=background, foreground="blue", font=('Arial Bold', 16),
                focuscolor=s.configure(".")["background"])
    genMale = ttk.Radiobutton(root1, text='Male', value=1, variable=r, style='Wild.TRadiobutton', takefocus=False)
    genMale.place(x=250, y=300)
    genFemale = ttk.Radiobutton(root1, text='Female', value=2, variable=r, style='Wild.TRadiobutton',
                                takefocus=False)
    genFemale.place(x=350, y=300)
    #l6 = Label(root1).place(x=100, y=100)

    Button(root1,text="Search",command=goto,font=("BOLD",16)).place(x=50,y=360)
    Button(root1,text="Clear",command=lambda:root.destroy(),font=("BOLD",16)).place(x=250,y=360)

    root.mainloop()