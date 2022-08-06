import webbrowser
from tkinter import ttk
from tkinter import *
import tkinter
import os
from tkinter.ttk import Combobox

import speech_recognition as sr
import pyttsx3
import pandas as pd

from PIL import Image, ImageTk
#import topdwon

background = "white"

castlist=["OC","BC_A","BC_B","BC_C","BC_D","BC_E","SC","ST","EWS","PH"]

import pandas as pd

data=pd.read_csv("topcolleges15.csv")


def collegecodetocollegename():
    data = pd.read_csv("TSALLCOLLEGESDETAILS.csv")
    # print(data["INST CODE"])
    allcollegescode = list(set(data["INST CODE"]))
    print(len(allcollegescode))
    d = {}
    for l, i, j in zip(data.index, data["INST CODE"], data["INSTITUTE NAME"]):
        d[i] = j
    return d

def prediction(prefercollege,preferbranch,caste,rank,r):
    s=caste+" BOYS"
    if r.get()==2:
        s=caste+" GIRLS"
    for l,i,j in zip(data.index,data["INST CODE"],data["BRANCH"]):
        if prefercollege==i and preferbranch==j:
            x=int(data.loc[l,s])
            #print(x)
            x=x+x//10
            if rank<x:
                return str((x - rank) * 100 // (x))+"%"
            else:
                return "NOT SURE"
    return "--"

def goto():
    global r,root,root1,root3,root4,root5,collegebox,branchbox,category,rankbox
    #label1 = Label(root1, text="", background="",font=("BOLD", 16), width=50).place(x=10, y=500)
    try:
        caste=category.get()
        preferbranch=branchbox.get()
        prefercollege=collegebox.get()
        #print(prefercollege)
        rank=int(rankbox.get())


        if category.get()=="":
            Label(root1, text="*Please Select Category", foreground="red", background="lightblue",font=("BOLD", 16), width=50).place(x=10, y=500)
        elif r.get()==0 :
            Label(root1, text="*Please Select Gender", foreground="red", background="lightblue",font=("BOLD", 16), width=50).place(x=10, y=500)


        else:
            #print(rank, preferbranch,prefercollege,caste, r)

            ##root1###
            if prefercollege!="" and preferbranch!="":
                bothprediction="NOT AVILABLE"
                bothprediction=prediction(prefercollege,preferbranch,caste,rank,r)
                label1=Label(root1, text=f"prediction Per%     {bothprediction}",font=("BOLD", 16),width=50).place(x=10,y=500)
                pyttsx3.speak(f"prediction {bothprediction}")


            ###root5#####
            if prefercollege!="" and preferbranch=="":

                #print(type(r.get()))

                from branchonly import collegeandbranches as cb
                CSE=prediction(prefercollege,"CSE",caste,rank,r)
                CSM = prediction(prefercollege, "CSM", caste, rank, r)
                CSD= prediction(prefercollege, "CSD", caste, rank,r)
                CSB = prediction(prefercollege, "CSB", caste, rank, r)
                IT = prediction(prefercollege, "INF", caste, rank, r)
                ECE= prediction(prefercollege, "ECE", caste, rank, r)
                EEE = prediction(prefercollege, "EEE", caste, rank, r)
                MEC = prediction(prefercollege, "MEC", caste, rank, r)
                CIV = prediction(prefercollege, "CIV", caste, rank, r)
                #print("hi this is root 5")
                Label(root5, text=f'Prediction Per% of branches for The college  {prefercollege} with the rank of{rankbox.get()}',
                      font=("BOLD", 12)).place(x=0, y=0)

                branchframe = Frame(root5, width=500, height=400,background="green")
                branchframe.place(x=0, y=50)
                Label(branchframe, text="BRANCH", font=("BOLD", 16),foreground="green", width=25,background="lightblue").grid(row=0, column=0,pady=1)
                Label(branchframe, text="PER%", font=("BOLD", 16),foreground="green", width=25,background="lightblue").grid(row=0, column=1,pady=1)

                Label(branchframe, text="CSE", font=("BOLD", 16), width=25,background="lightblue").grid(row=1, column=0,pady=1)
                Label(branchframe, text=CSE, font=("BOLD", 16), width=25,background="lightblue").grid(row=1, column=1,pady=1)

                Label(branchframe, text="CSE_AIML", font=("BOLD", 16), width=25,background="lightblue").grid(row=2, column=0,pady=1)
                Label(branchframe, text=CSM, font=("BOLD", 16), width=25,background="lightblue").grid(row=2, column=1,pady=1)

                Label(branchframe, text="CSE_DS", font=("BOLD", 16), width=25,background="lightblue").grid(row=3, column=0,pady=1)
                Label(branchframe, text=CSD, font=("BOLD", 16), width=25,background="lightblue").grid(row=3, column=1,pady=1)

                Label(branchframe, text="CSE_CSBS", font=("BOLD", 16), width=25,background="lightblue").grid(row=4, column=0,pady=1)
                Label(branchframe, text=CSB, font=("BOLD", 16), width=25,background="lightblue").grid(row=4, column=1,pady=1)

                Label(branchframe, text="IT", font=("BOLD", 16), width=25,background="lightblue").grid(row=5, column=0,pady=1)
                Label(branchframe, text=IT, font=("BOLD", 16), width=25,background="lightblue").grid(row=5, column=1,pady=1)

                Label(branchframe, text="ECE", font=("BOLD", 16), width=25,background="lightblue").grid(row=6, column=0,pady=1)
                Label(branchframe, text=ECE, font=("BOLD", 16), width=25,background="lightblue").grid(row=6, column=1,pady=1)

                Label(branchframe, text="EEE", font=("BOLD", 16), width=25,background="lightblue").grid(row=7, column=0,pady=1)
                Label(branchframe, text=EEE, font=("BOLD", 16), width=25,background="lightblue").grid(row=7, column=1,pady=1)

                Label(branchframe, text="MEC", font=("BOLD", 16), width=25,background="lightblue").grid(row=8, column=0,pady=1)
                Label(branchframe, text=MEC, font=("BOLD", 16), width=25,background="lightblue").grid(row=8, column=1,pady=1)

                Label(branchframe, text="CIVIL", font=("BOLD", 16), width=25,background="lightblue").grid(row=9, column=0,pady=1)
                Label(branchframe, text=CIV, font=("BOLD", 16), width=25,background="lightblue").grid(row=9, column=1,pady=1)

                Button(root5, text="HOME", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
                Button(root5, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
                Button(root5, text="INFO", command=lambda: root6.tkraise(), font=("BOLD", 10)).place(x=150, y=650)
                root5.tkraise()







            ####root4#####
            if prefercollege=="" and preferbranch=="":
                #print("hi this is root 4")
                #Label(root4, text=f'Prediction Per% of colleges for The ALL branchs with this rank{l2.get()}',font=("BOLD", 14)).place(x=0, y=0)
                #Label(root4,text="BRANCHE",font=("BOLD",16)).grid(row=5,column=1)

                Label(root4,text="COLLEGE",foreground="blue",font=("BOLD",10),width=10).grid(row=0,column=0,pady=10,padx=10)
                Label(root4,text="CSE",foreground="blue",font=("BOLD",8),width=10).grid(row=0,column=1,pady=10,padx=10)
                Label(root4, text="CSE_DS",foreground="blue", font=("BOLD", 10),width=8).grid(row=0, column=2,pady=10,padx=10)
                Label(root4, text="CSE_AIML",foreground="blue", font=("BOLD", 10),width=8).grid(row=0, column=3,pady=10,padx=10)
                Label(root4, text="CSE_CSBS",foreground="blue", font=("BOLD", 10),width=8).grid(row=0, column=4,pady=10,padx=10)
                Label(root4, text="IT",foreground="blue", font=("BOLD", 10),width=10).grid(row=0, column=5,pady=10,padx=10)
                Label(root4, text="ECE",foreground="blue", font=("BOLD", 10),width=10).grid(row=0, column=6,pady=10,padx=10)
                Label(root4, text="EEE",foreground="blue", font=("BOLD", 10),width=10).grid(row=0, column=7,pady=10,padx=10)
                Label(root4, text="MEC",foreground="blue", font=("BOLD", 10),width=10).grid(row=0, column=8,pady=10,padx=10)
                Label(root4, text="CIVIL",foreground="blue", font=("BOLD", 10),width=10).grid(row=0, column=9,pady=10,padx=10)


                Label(root4, text="GRIET",foreground="blue", font=("BOLD", 10), width=10).grid(row=1, column=0, pady=10, padx=10)
                Label(root4, text="CBIT",foreground="blue", font=("BOLD", 10), width=10).grid(row=2, column=0, pady=10, padx=10)
                Label(root4, text="VASAVI",foreground="blue", font=("BOLD", 10), width=10).grid(row=3, column=0, pady=10, padx=10)
                Label(root4, text="VNR",foreground="blue", font=("BOLD", 10), width=10).grid(row=4, column=0, pady=10, padx=10)
                Label(root4, text="CVR",foreground="blue", font=("BOLD", 10), width=10).grid(row=5, column=0, pady=10, padx=10)
                Label(root4, text="MVSR",foreground="blue", font=("BOLD", 10), width=10).grid(row=6, column=0, pady=10, padx=10)
                Label(root4, text="SREENIDHI",foreground="blue", font=("BOLD", 10), width=10).grid(row=7, column=0, pady=10, padx=10)
                Label(root4, text="VARDHAMAN",foreground="blue", font=("BOLD", 10), width=10).grid(row=8, column=0, pady=10, padx=10)
                Label(root4, text="JNTU",foreground="blue", font=("BOLD", 10), width=10).grid(row=9, column=0, pady=10, padx=10)
                Label(root4, text="OU",foreground="blue", font=("BOLD", 10), width=10).grid(row=10, column=0, pady=10, padx=10)
                Label(root4, text="MGIT",foreground="blue", font=("BOLD", 10), width=10).grid(row=11, column=0, pady=10, padx=10)
                Label(root4, text="BVRIT",foreground="blue", font=("BOLD", 10), width=10).grid(row=12, column=0, pady=10, padx=10)
                Label(root4, text="MLRD",foreground="blue", font=("BOLD", 10), width=10).grid(row=13, column=0, pady=10, padx=10)
                Label(root4, text="CVSR",foreground="blue", font=("BOLD", 10), width=10).grid(row=14, column=0, pady=10, padx=10)
                Label(root4, text="CVRH",foreground="blue", font=("BOLD", 10), width=10).grid(row=15, column=0, pady=10, padx=10)

                college = ["GRRR","CBIT","VASV","VJEC","CVRH","MVSR","SNIS","VMEG","JNTH","OUCE","MGIT","BVRI","MLRD","CVSR","CVRH"]
                branchches=["CSE","CSD","CSM","CSB","INF","ECE","EEE","MEC","CIV"]

                for i in range(len(college)):
                    for j in range(len(branchches)):

                        Label(root4,text=prediction(college[i],branchches[j],caste,rank,r),width=10,font=("BOLD",10)).grid(row=i+1,column=j+1,padx=10,pady=10)


                Button(root4, text="HOME", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=5, y=680)
                Button(root4, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=680)
                Button(root4, text="INFO", command=lambda: root6.tkraise(), font=("BOLD", 10)).place(x=150, y=680)

                root4.tkraise()




            #### root3#####
            if prefercollege=="" and preferbranch!="":

                x=("","GRRR","CBIT","VASV","VJEC","CVRH","MVSR","VMEG","SNIS","BVRI","JNTH","OUCE","MGIT","MLRD","CVRH","CVSR")
                GRRR=prediction("GRRR",preferbranch,caste,rank,r)
                CBIT=prediction("CBIT",preferbranch,caste,rank,r)
                VASV=prediction("VASV",preferbranch,caste,rank,r)
                VJEC=prediction("VJEC",preferbranch,caste,rank,r)
                VMEG=prediction("VMEG",preferbranch,caste,rank,r)
                CVRH=prediction("CVRH",preferbranch,caste,rank,r)
                SRIS=prediction("SNIS",preferbranch,caste,rank,r)
                MVSR=prediction("MVSR",preferbranch,caste,rank,r)
                JNTH=prediction("JNTH",preferbranch,caste,rank,r)
                OUCE = prediction("OUCE", preferbranch, caste, rank, r)
                MGIT = prediction("MGIT", preferbranch, caste, rank, r)
                CVRH = prediction("CVRH", preferbranch, caste, rank, r)
                CVSR = prediction("CVSR", preferbranch, caste, rank, r)
                BVRIT = prediction("BVRI", preferbranch, caste, rank, r)
                MLRD = prediction("MLRD", preferbranch, caste, rank, r)



                Label(root3, text=f'Prediction Per% of colleges for The branch  {preferbranch} with this rank{rankbox.get()}', font=("BOLD", 14)).place(x=0, y=0)

                branchframe=Frame(root3,width=500,height=400)
                branchframe.place(x=0,y=50)
                Label(branchframe, text="COLLEGE",font=("BOLD",16),foreground="green",background="lightblue", width=25).grid(row=0, column=0,pady=1)
                Label(branchframe, text="PER%", font=("BOLD",16),foreground="green",background="lightblue",width=25).grid(row=0, column=1,pady=1)

                Label(branchframe,text="GRIET",font=("BOLD",16),background="lightblue",width=25).grid(row=1,column=0,pady=1)
                Label(branchframe,text=GRRR,font=("BOLD",16),background="lightblue",width=25).grid(row=1,column=1,pady=1)

                Label(branchframe, text="CBIT",font=("BOLD",16),background="lightblue",width=25).grid(row=2, column=0,pady=1)
                Label(branchframe, text=CBIT, font=("BOLD",16),background="lightblue",width=25).grid(row=2, column=1,pady=1)

                Label(branchframe, text="VASAVI",font=("BOLD",16),background="lightblue",width=25).grid(row=3, column=0,pady=1)
                Label(branchframe, text=VASV,font=("BOLD",16),background="lightblue", width=25).grid(row=3, column=1,pady=1)

                Label(branchframe, text="VNR",font=("BOLD",16),background="lightblue",width=25).grid(row=4, column=0,pady=1)
                Label(branchframe, text=VJEC,font=("BOLD",16),background="lightblue", width=25).grid(row=4, column=1,pady=1)

                Label(branchframe, text="CVR",font=("BOLD",16),background="lightblue",width=25).grid(row=5, column=0,pady=1)
                Label(branchframe, text=CVRH,font=("BOLD",16),background="lightblue", width=25).grid(row=5, column=1,pady=1)

                Label(branchframe, text="MVSR",font=("BOLD",16),background="lightblue",width=25).grid(row=6, column=0,pady=1)
                Label(branchframe, text=MVSR, font=("BOLD",16),background="lightblue",width=25).grid(row=6, column=1,pady=1)

                Label(branchframe, text="Vardhaman",font=("BOLD",16),background="lightblue",width=25).grid(row=7, column=0,pady=1)
                Label(branchframe, text=VMEG,font=("BOLD",16),background="lightblue", width=25).grid(row=7, column=1,pady=1)

                Label(branchframe, text="Sreenidhi",font=("BOLD",16),background="lightblue",width=25).grid(row=8, column=0,pady=1)
                Label(branchframe, text=SRIS, font=("BOLD",16),background="lightblue",width=25).grid(row=8, column=1,pady=1)

                Label(branchframe, text="JNTUH", font=("BOLD", 16),background="lightblue", width=25).grid(row=9, column=0,pady=1)
                Label(branchframe, text=JNTH, font=("BOLD", 16),background="lightblue", width=25).grid(row=9, column=1,pady=1)

                Label(branchframe, text="OU", font=("BOLD", 16),background="lightblue", width=25).grid(row=10, column=0,pady=1)
                Label(branchframe, text=OUCE, font=("BOLD", 16),background="lightblue", width=25).grid(row=10, column=1,pady=1)

                Label(branchframe, text="MGIT", font=("BOLD", 16),background="lightblue", width=25).grid(row=11, column=0,pady=1)
                Label(branchframe, text=MGIT, font=("BOLD", 16),background="lightblue", width=25).grid(row=11, column=1,pady=1)

                Label(branchframe, text="BVRIT", font=("BOLD", 16),background="lightblue", width=25).grid(row=12, column=0,pady=1)
                Label(branchframe, text=BVRIT, font=("BOLD", 16),background="lightblue", width=25).grid(row=12, column=1,pady=1)

                Label(branchframe, text="CVRH", font=("BOLD", 16),background="lightblue", width=25).grid(row=13, column=0,pady=1)
                Label(branchframe, text=CVRH, font=("BOLD", 16),background="lightblue", width=25).grid(row=13, column=1,pady=1)

                Label(branchframe, text="MRLD", font=("BOLD", 16),background="lightblue", width=25).grid(row=14, column=0,pady=1)
                Label(branchframe, text=MLRD, font=("BOLD", 16),background="lightblue", width=25).grid(row=14, column=1,pady=1)

                Label(branchframe, text="CVSR", font=("BOLD", 16),background="lightblue", width=25).grid(row=15, column=0,pady=1)
                Label(branchframe, text=CVSR, font=("BOLD", 16),background="lightblue", width=25).grid(row=15, column=1,pady=1)



                Button(root3, text="HOME", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
                Button(root3, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
                Button(root3, text="INFO", command=lambda: root6.tkraise(), font=("BOLD", 10)).place(x=150, y=650)
                root3.tkraise()
    except Exception as e:
        #print(e)
        Label(root1, text="*Please Fill Rank", foreground="red", background="lightblue", font=("BOLD", 16),
              width=50).place(x=10, y=500)







    #colleges = {"GRIET": GRIET, "CBIT":CBIT, "VASAVI":Vasavi, "VNR":VNR, "SREENIDHI": Sreenidhi, "MVSR": MVSR, "CVR": CVR, "VARDHAMAN": Vardhaman}



if __name__=="__main__":
    background="lightblue"
    root = Tk()
    root.title("EAMCET TOP 15 COLLEGES")
    w_width, w_height = 550, 750
    s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
    root.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))  # center location of the screen
    root.configure(bg=background)
    # root.attributes('-toolwindow', True)
    root1 = Frame(root, bg=background)
    root2 = Frame(root, bg=background)
    root3 = Frame(root, bg=background)
    root4 = Frame(root, bg=background)
    root5 = Frame(root, bg=background)
    root6=Frame(root,background=background)



    for f in (root1, root2, root3,root4,root5,root6):
        f.grid(row=0, column=0,sticky="news")



    ###### ROOT1 #####
    Frame(root1,width=550,height=750,background=background).pack()
    G_img = Image.open("img.png")
    G_img = G_img.resize((500, 80))
    G_img = ImageTk.PhotoImage(G_img)
    Label(root1, image=G_img).place(x=10,y=10)
    Label(root1,text="*",font=("BOLD",18),foreground="red",background="lightblue").place(x=198,y=120)
    l1 = Label(root1, text="EAMCET RANK",font=("BOLD",16),background="lightblue").place(x=50, y=120)
    rankbox=StringVar()
    rankbox = Entry(root1, width=13, font=("BOLD", 16), relief=FLAT)
    rankbox.place(x=250, y=120)
    l3 = Label(root1, text="BRANCH",font=("BOLD",16),background="lightblue").place(x=50, y=180)
    branchbox = Combobox(root1, font=("BOLD", 10))
    branchbox['values']=("", "CSE", "CSM", "CSD", "CSB", "MEC", "INF", "ECE", "EEE", "CIV")
    branchbox.current(0)
    branchbox.place(x=250, y=180)

    l21 = Label(root1, text="COLLEGE", font=("BOLD", 16),background="lightblue").place(x=50, y=240)
    collegebox = Combobox(root1, font=("BOLD", 10))
    collegebox['values'] = ("","GRRR","CBIT","VASV","VJEC","CVRH","MVSR","VMEG","SNIS","BVRIT","JNTH","OUCE","MGIT","MLRD","CVSR")
    collegebox.current(0)
    collegebox.place(x=250, y=240)
    Label(root1, text="*", font=("BOLD", 18), foreground="red", background="lightblue").place(x=168, y=300)
    l21 = Label(root1, text="CATEGORY", font=("BOLD", 16),background="lightblue").place(x=50, y=300)
    category=Combobox(root1,font=("BOLD", 10))
    category['values']=("","OC","BC_A","BC_B","BC_C","BC_D","BC_E","SC","ST","EWS")
    category.current(0)
    category.place(x=250,y=300)

    Label(root1, text="*", font=("BOLD", 18), foreground="red", background="lightblue").place(x=120, y=360)
    l5 = Label(root1, text="Gender",font=("BOLD",16),background="lightblue").place(x=50, y=360)
    r = IntVar()
    s = ttk.Style()
    s.configure('Wild.TRadiobutton', background=background, foreground="blue", font=('Arial Bold', 16),
                focuscolor=s.configure(".")["background"])
    genMale = ttk.Radiobutton(root1, text='Male', value=1, variable=r, style='Wild.TRadiobutton', takefocus=False)
    genMale.place(x=250, y=360)
    genFemale = ttk.Radiobutton(root1, text='Female', value=2, variable=r, style='Wild.TRadiobutton',
                                takefocus=False)
    genFemale.place(x=350, y=360)
    def clear():
        category.current(0)
        branchbox.current(0)
        collegebox.current(0)
        r.set(0)
        rankbox = Entry(root1, width=13, font=("BOLD", 16), relief=FLAT)
        rankbox.place(x=250, y=120)


    Button(root1,text="Search",command=goto,font=("BOLD",16)).place(x=50,y=420)
    Button(root1,text="Clear",command=clear,font=("BOLD",16)).place(x=200,y=420)
    #Button(root1,text="CLOSE",foreground="red",command=lambda :root.destroy(),font=("BOLD",15)).place(x=350,y=420)
    Button(root1, text="HOME", command= lambda :root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
    Button(root1, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
    Button(root1, text="INFO", command=lambda: root6.tkraise(), font=("BOLD", 10)).place(x=150, y=650)

    ####ROOT 6 INFO#####
    Label(root6, text="CONTACT :info@griet.ac.in\n \n ", font=("BOLD", 24), foreground="red", background="lightblue").place(x=30, y=125)
    Button(root6, text="HOME", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
    Button(root6, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
    Button(root6, text="BACK", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=150, y=650)
    #### ROOT 2   #college LOGO#####

    grietlogo = ImageTk.PhotoImage(Image.open("collegeImages/griet.png").resize((550, 200)))
    cbitlogo=ImageTk.PhotoImage(Image.open("collegeImages/cbit.png").resize((550, 200)))
    vasavilogo=ImageTk.PhotoImage(Image.open("collegeImages/vasavi.png").resize((550, 200)))
    mvsrlogo=ImageTk.PhotoImage(Image.open("collegeImages/mvsr.png").resize((550, 200)))
    sreenidhilogo=ImageTk.PhotoImage(Image.open("collegeImages/sreenidhi.png").resize((550, 200)))
    vardhamanlogo=ImageTk.PhotoImage(Image.open("collegeImages/vardhaman.png").resize((550, 200)))
    vnrlogo=ImageTk.PhotoImage(Image.open("collegeImages/vnr.png").resize((550, 200)))
    cvrlogo=ImageTk.PhotoImage(Image.open("collegeImages/cvr.png").resize((550, 200)))
    oucelogo=ImageTk.PhotoImage(Image.open("collegeImages/ou.png").resize((550, 200)))
    jntulogo=ImageTk.PhotoImage(Image.open("collegeImages/jntuh.png").resize((550, 200)))
    mgitlogo=ImageTk.PhotoImage(Image.open("collegeImages/mgit.png").resize((550, 200)))
    mlrlogo=ImageTk.PhotoImage(Image.open("collegeImages/mlrd.png").resize((550, 200)))
    cvsrlogo=ImageTk.PhotoImage(Image.open("collegeImages/cvsr.png").resize((550, 200)))
    bvritlogo=ImageTk.PhotoImage(Image.open("collegeImages/bvrit.png").resize((550, 200)))


    collegedict={"GRRR":grietlogo,"CBIT":cbitlogo,"VASV":vasavilogo,"MVSR":mvsrlogo,"VJEC":vnrlogo,"SNIS":sreenidhilogo,"CVRH":cvrlogo,
                 "VMEG":vardhamanlogo,"JNTH":jntulogo,"OUCE":oucelogo,"BVRI":bvritlogo,"MGIT":mgitlogo,"CVSR":cvsrlogo,"MLRD":mlrlogo}
    ##### ROOT 2####
    collegebranches={"griet":"CSE,CSE_AIML,CSE_DS,CSE_CSBS,MEC,IT,ECE,EEE,CIVIL",
                     "cbit":"CSE,CSE_AIML,MEC,IT,ECE,EEE,CIVIL",
                     "vasavi":"CSE,CSE_AIML,MEC,IT,ECE,EEE,CIVIL",
                     "vnr":"CSE,CSE_AIML,CSE_DS,CSE_CSBS,MEC,IT,ECE,EEE,CIVIL",
                     "cvr":"CSE,CSE_AIML,CSE_DS,MEC,IT,ECE,EEE,CIVIL",
                     "mvsr":"CSE,MEC,IT,ECE,EEE,CIVIL",
                    "vardhaman":"CSE,CSE_AIML,MEC,IT,ECE,EEE,CIVIL",
                     "sreenidhi":"CSE,CSE_AIML,CSE_DS,MEC,IT,ECE,EEE,CIVIL"}
    collegedetails = ['INST CODE', 'INSTITUTE NAME', 'PLACE', 'DIST', 'COED', 'TYPE',
                      'YEAR OF ESTB', 'BRANCH', 'BRANCH NAME', 'OC BOYS', 'OC GIRLS',
                      'BC_A BOYS', 'BC_A GIRLS', 'BC_B BOYS', 'BC_B GIRLS', 'BC_C BOYS',
                      'BC_C GIRLS', 'BC_D BOYS', 'BC_D GIRLS', 'BC_E BOYS', 'BC_E GIRLS',
                      'SC_BOYS', 'SC_GIRLS', 'ST_BOYS', 'ST_GIRLS', 'TUITION FEE',
                      'AFFILIATED']
    def collegename(name):
        for i,j in zip(data.index,data["INST CODE"]):
            if j==name:
                return data.loc[i,"INSTITUTE NAME"]
    def collegefee(name):
        for i,j in zip(data.index,data["INST CODE"]):
            if j==name:
                return data.loc[i,"TUITION FEE"]
        pass
    def collegeadress(name):
        for i,j in zip(data.index,data["INST CODE"]):
            if j==name:
                return data.loc[i,"PLACE"]+"  "+data.loc[i,"DIST"]
        pass
    def yearofestablish(name):
        for i,j in zip(data.index,data["INST CODE"]):
            if j==name:
                return data.loc[i,"YEAR OF ESTB"]
        pass
    def collegeurl(name):
        if name=="GRRR":
            return "www.griet.ac.in"
        if name=="CBIT":
            return "cbit.ac.in"
        if name=="VASV":
            return "vce.ac.in"
        if name=="VJEC":
            return "vnrvjiet.ac.in"
        if name=="SNIS":
            return "sreenidhi.edu.in"
        if name=="MVSR":
            return "mvsrec.edu.in"
        if name=="CVRH":
            return "cvr.ac.in"
        if name=="VMEG":
            return "vardhaman.org"
        if name=="JNTUH":
            return "jntuh.ac.in"
        if name=="OU":
            return "osmania.ac.in"
        if name=="MGIT":
            return "mgit.ac.in"
        if name=="BVRIT":
            return "bvrit.ac.in"
        if name=="CVSR":
            return "  "
        if name=="MLRD":
            return "mlrinstitutions.ac.in"

    def collegeaffiliated(name):
        for i,j in zip(data.index,data["INST CODE"]):
            if j==name:
                return data.loc[i,"AFFILIATED"]
        pass
    def collegebranche(name):
        b = []
        for i,j in zip(data.index,data["INST CODE"]):

            if j==name:
                if data.loc[i,"BRANCH"] not in b:
                    b.append(data.loc[i,"BRANCH"])
        return " ".join(b)
        pass
    def collegenack(name):
        if name=="GRRR":
            return "A++"
        if name=="CBIT":
            return "A"
        if name=="VASV":
            return "A++"
        if name=="VJEC":
            return "A++"
        if name=="SNIS":
            return "A+"
        if name=="MVSR":
            return "B++"
        if name=="CVRH":
            return "A"
        if name=="VMEG":
            return "A++"
        if name=="JNTUH":
            return "A"
        if name=="OU":
            return "A+"
        if name=="MGIT":
            return "A"
        if name=="BVRIT":
            return "A"
        if name=="CVSR":
            return "A"
        if name=="MLRD":
            return "A++"

    def collegehostel(name):
        for i,j in zip(data.index,data["INST CODE"]):
            if j==name:
                return "GIRLS(YES)/BOYS(NO)"
        pass
    def collegebus(name):
        for i,j in zip(data.index,data["INST CODE"]):
            if j==name:
                return "YES"
        pass

    def collegeframe(name):
        #root2image = Frame(master=root2, width=550, height=200, background="#d3d3d3").place(x=0, y=50)

        detailFrame2 = Frame(root2)
        detailFrame2.place(x=0,y=100)
        userFrame2 = Label(detailFrame2, image=collegedict[name],width=550, height=200, relief=FLAT)
        userFrame2.pack()


        collegedetails=root2
        Label(collegedetails,text="COLLEGE NAME ",width=20).place(x=0,y=300)
        Label(collegedetails, text=collegename(name),width=60).place(x=150,y=300)
        #Label(collegedetails,text="",width=1).grid(row=0,column=2)

        Label(collegedetails, text="NAAC RANK",width=20).place(x=0,y=340)
        Label(collegedetails, text=collegenack(name),width=60).place(x=150,y=340)

        Label(collegedetails,text="AVILABLE BRANCHES",width=20).place(x=0,y=380)
        Label(collegedetails,text=collegebranche(name),width=60).place(x=150,y=380)

        Label(collegedetails, text="AFFILIATED",width=20).place(x=0,y=420)
        Label(collegedetails, text=collegeaffiliated(name),width=60).place(x=150,y=420)


        Label(collegedetails, text="COLLEGE ADDRESS",width=20).place(x=0,y=460)
        Label(collegedetails, text=collegeadress(name),width=60).place(x=150,y=460)

        Label(collegedetails, text="TUTION FEE",width=20).place(x=0,y=500)
        Label(collegedetails, text=collegefee(name),width=60).place(x=150,y=500)

        Label(collegedetails, text="HOSTEL FACILITY",width=20).place(x=0,y=540)
        Label(collegedetails, text=collegehostel(name),width=60).place(x=150,y=540)

        Label(collegedetails, text="BUS FACILITY",width=20).place(x=0,y=580)
        Label(collegedetails, text=collegebus(name),width=60).place(x=150,y=580)

        Label(collegedetails, text="COLLEGE URL",width=20).place(x=0,y=620)
        Button(collegedetails, text=collegeurl(name),command=lambda :webbrowser.open(collegename(name)),width=60,foreground="blue").place(x=150,y=620)



    colleges=["GRIET","CBIT","VASAVI","VARDHAMAN","VNR","CVR","MVSR","SREENIDHI"]
    #for j in range(8):
    x=tkinter.Frame(master=root2,relief=tkinter.RAISED,background="white",border=3)
    x.grid(row=0,column=0,pady=(10,10))
    Button(master=x,text="GRRR",width=5,command=lambda :collegeframe("GRRR"),font=("BOLD",10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=1,padx=5)
    Button(master=x, text="CBIT",width=5 ,command=lambda :collegeframe("CBIT"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=2,padx=5)
    Button(master=x, text="VASV",width=5, command=lambda :collegeframe("VASV"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=3,padx=5)
    Button(master=x, text="VJEC",width=5, command=lambda: collegeframe("VJEC"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=4,padx=5)
    Button(master=x, text="SNIS",width=5, command=lambda: collegeframe("SNIS"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=5,padx=5)
    Button(master=x, text="MVSR",width=5, command=lambda: collegeframe("MVSR"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=6,padx=5)
    Button(master=x, text="CVRH",width=5, command=lambda: collegeframe("CVRH"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=7,padx=5)
    Button(master=x, text="VMEG",width=5, command=lambda: collegeframe("VMEG"), font=("BOLD", 10)).pack()

    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=1, column=0,padx=5)
    Button(master=x, text="JNTUH", width=5,command=lambda: collegeframe("JNTH"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=1, column=1,padx=5)
    Button(master=x, text="OU", width=5,command=lambda: collegeframe("OUCE"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=1, column=2,padx=5)
    Button(master=x, text="MGIT", width=5,command=lambda: collegeframe("MGIT"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=1, column=3,padx=5)
    Button(master=x, text="BVRIT",width=5, command=lambda: collegeframe("BVRI"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=1, column=4,padx=5)
    Button(master=x, text="CVSR", width=5,command=lambda: collegeframe("CVSR"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=1, column=5,padx=5)
    Button(master=x, text="CVRH", width=5,command=lambda: collegeframe("CVRH"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=1, column=6,padx=5)
    Button(master=x, text="MLRD",width=5, command=lambda: collegeframe("MLRD"), font=("BOLD", 10)).pack()


    Button(root2, text="HOME", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
    Button(root2, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
    Button(root2, text="INFO", command=lambda: root6.tkraise(), font=("BOLD", 10)).place(x=150, y=650)
    root1.tkraise()
    root1.mainloop()