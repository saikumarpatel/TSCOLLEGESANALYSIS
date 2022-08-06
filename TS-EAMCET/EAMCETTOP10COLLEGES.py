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



def goto():
    global r,root,root1,root3,root4,root5,collegebox,branchbox,category,rankbox
    caste=category.get()
    preferbranch=branchbox.get()
    preferbranch=preferbranch.replace("_","")
    prefercollege=collegebox.get()
    rank=int(rankbox.get())
    print(rank, preferbranch,prefercollege,caste, r)


    ###root5#####
    if prefercollege!="" and preferbranch=="":
        #print(type(r.get()))

        from branchonly import collegeandbranches as cb
        CSE=cb(prefercollege,"CSE",caste,r,rank)
        CSE_AIML = cb(prefercollege, "CSEAIML", caste, r, rank)
        CSE_DS = cb(prefercollege, "CSEDS", caste, r, rank)
        CSE_CSBS = cb(prefercollege, "CSECSBS", caste, r, rank)
        IT = cb(prefercollege, "IT", caste, r, rank)
        ECE= cb(prefercollege, "ECE", caste, r, rank)
        EEE = cb(prefercollege, "EEE", caste, r, rank)
        MEC = cb(prefercollege, "MEC", caste, r, rank)
        CIVIL = cb(prefercollege, "CIVIL", caste, r, rank)
        print("hi this is root 5")
        Label(root5, text=f'Prediction Per% of branches for The college  {prefercollege} with the rank of{rankbox.get()}',
              font=("BOLD", 14)).place(x=0, y=0)

        branchframe = Frame(root5, width=500, height=400, background="#d3d3d3")
        branchframe.place(x=0, y=50)
        Label(branchframe, text="BRANCHE", font=("BOLD", 16), width=25).grid(row=0, column=0)
        Label(branchframe, text="PER%", font=("BOLD", 16), width=25).grid(row=0, column=1)

        Label(branchframe, text="CSE", font=("BOLD", 16), width=25).grid(row=1, column=0)
        Label(branchframe, text=CSE, font=("BOLD", 16), width=25).grid(row=1, column=1)

        Label(branchframe, text="CSE_AIML", font=("BOLD", 16), width=25).grid(row=2, column=0)
        Label(branchframe, text=CSE_AIML, font=("BOLD", 16), width=25).grid(row=2, column=1)

        Label(branchframe, text="CSE_DS", font=("BOLD", 16), width=25).grid(row=3, column=0)
        Label(branchframe, text=CSE_DS, font=("BOLD", 16), width=25).grid(row=3, column=1)

        Label(branchframe, text="CSE_CSBS", font=("BOLD", 16), width=25).grid(row=4, column=0)
        Label(branchframe, text=CSE_CSBS, font=("BOLD", 16), width=25).grid(row=4, column=1)

        Label(branchframe, text="IT", font=("BOLD", 16), width=25).grid(row=5, column=0)
        Label(branchframe, text=IT, font=("BOLD", 16), width=25).grid(row=5, column=1)

        Label(branchframe, text="ECE", font=("BOLD", 16), width=25).grid(row=6, column=0)
        Label(branchframe, text=ECE, font=("BOLD", 16), width=25).grid(row=6, column=1)

        Label(branchframe, text="EEE", font=("BOLD", 16), width=25).grid(row=7, column=0)
        Label(branchframe, text=EEE, font=("BOLD", 16), width=25).grid(row=7, column=1)

        Label(branchframe, text="MEC", font=("BOLD", 16), width=25).grid(row=8, column=0)
        Label(branchframe, text=MEC, font=("BOLD", 16), width=25).grid(row=8, column=1)

        Label(branchframe, text="CIVIL", font=("BOLD", 16), width=25).grid(row=9, column=0)
        Label(branchframe, text=CIVIL, font=("BOLD", 16), width=25).grid(row=9, column=1)

        Button(root5, text="HOME", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
        Button(root5, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
        Button(root5, text="INFO", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=150, y=650)
        root5.tkraise()







    ####root4#####
    if prefercollege=="" and preferbranch=="":
        print("hi this is root 4")
        #Label(root4, text=f'Prediction Per% of colleges for The ALL branchs with this rank{l2.get()}',font=("BOLD", 14)).place(x=0, y=0)
        #Label(root4,text="BRANCHE",font=("BOLD",16)).grid(row=5,column=1)

        Label(root4,text="COLLEGE",font=("BOLD",10),width=10).grid(row=0,column=0,pady=10,padx=10)
        Label(root4,text="CSE",font=("BOLD",8),width=10).grid(row=0,column=1,pady=10,padx=10)
        Label(root4, text="CSE_DS", font=("BOLD", 10),width=8).grid(row=0, column=2,pady=10,padx=10)
        Label(root4, text="CSE_AIML", font=("BOLD", 10),width=8).grid(row=0, column=3,pady=10,padx=10)
        Label(root4, text="CSE_CSBS", font=("BOLD", 10),width=8).grid(row=0, column=4,pady=10,padx=10)
        Label(root4, text="IT", font=("BOLD", 8),width=10).grid(row=0, column=5,pady=10,padx=10)
        Label(root4, text="ECE", font=("BOLD", 8),width=10).grid(row=0, column=6,pady=10,padx=10)
        Label(root4, text="EEE", font=("BOLD", 8),width=10).grid(row=0, column=7,pady=10,padx=10)
        Label(root4, text="MEC", font=("BOLD", 8),width=10).grid(row=0, column=8,pady=10,padx=10)
        Label(root4, text="CIVIL", font=("BOLD", 8),width=10).grid(row=0, column=9,pady=10,padx=10)

        Label(root4, text="GRIET", font=("BOLD", 8), width=10).grid(row=1, column=0, pady=10, padx=10)
        Label(root4, text="CBIT", font=("BOLD", 8), width=10).grid(row=2, column=0, pady=10, padx=10)
        Label(root4, text="VASAVI", font=("BOLD", 8), width=10).grid(row=3, column=0, pady=10, padx=10)
        Label(root4, text="VNR", font=("BOLD", 8), width=10).grid(row=4, column=0, pady=10, padx=10)
        Label(root4, text="CVR", font=("BOLD", 8), width=10).grid(row=5, column=0, pady=10, padx=10)
        Label(root4, text="MVSR", font=("BOLD", 8), width=10).grid(row=6, column=0, pady=10, padx=10)
        Label(root4, text="SREENIDHI", font=("BOLD", 8), width=10).grid(row=7, column=0, pady=10, padx=10)
        Label(root4, text="VARDHAMAN", font=("BOLD", 8), width=10).grid(row=8, column=0, pady=10, padx=10)

        college = ["GRIET", "CBIT", "VASAVI", "VNR","CVR","MVSR", "SREENIDHI", "VARDHAMAN"]
        branchches=["CSE","CSEDS","CSEAIML","CSECSBS","IT","ECE","EEE","MEC","CIVIL"]
        from branchonly import collegeandbranches as cb
        for i in range(len(college)):
            for j in range(len(branchches)):
                #print(college[i],branchches[j])
                Label(root4,text=cb(college[i],branchches[j],caste,r,rank),width=10,font=("BOLD",10)).grid(row=i+1,column=j+1)


        Button(root4, text="HOME", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
        Button(root4, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
        Button(root4, text="INFO", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=150, y=650)

        root4.tkraise()




    #### root3#####
    if prefercollege=="" and preferbranch!="":
        import branchonly
        x=str(caste)
        caste=caste.replace("_","")
        print(x,caste)
        if r.get()==1:
            GRIET=branchonly.GRIET(int(rank),x,"M",preferbranch)
            CBIT=branchonly.CBIT(int(rank), caste,"Boys", preferbranch)
            Vasavi=branchonly.Vasavi(int(rank), caste, "Boys", preferbranch)
            VNR=branchonly.VNR(int(rank), caste,"Boys", preferbranch)
            Vardhaman=branchonly.Vardhaman(int(rank), caste,"Boys", preferbranch)
            CVR=branchonly.CVR(int(rank), caste,"Boys", preferbranch)
            Sreenidhi=branchonly.Sreenidhi(int(rank), caste,"Boys", preferbranch)
            MVSR=branchonly.MVSR(int(rank), caste,"Boys", preferbranch)
        else:
            GRIET = branchonly.GRIET(int(rank), x, "F", preferbranch)
            CBIT = branchonly.CBIT(int(rank), caste, "Girls", preferbranch)
            Vasavi = branchonly.Vasavi(int(rank), caste, "Girls", preferbranch)
            VNR = branchonly.VNR(int(rank), caste, "Girls", preferbranch)
            Vardhaman = branchonly.Vardhaman(int(rank), caste, "Girls", preferbranch)
            CVR = branchonly.CVR(int(rank), caste, "Girls", preferbranch)
            Sreenidhi = branchonly.Sreenidhi(int(rank), caste, "Girls", preferbranch)
            MVSR = branchonly.MVSR(int(rank), caste, "Girls", preferbranch)


        Label(root3, text=f'Prediction Per% of colleges for The branch  {preferbranch} with this rank{rankbox.get()}', font=("BOLD", 14)).place(x=0, y=0)

        branchframe=Frame(root3,width=500,height=400,background="#d3d3d3")
        branchframe.place(x=0,y=50)
        Label(branchframe, text="COLLEGE",font=("BOLD",16), width=25).grid(row=0, column=0)
        Label(branchframe, text="PER%", font=("BOLD",16),width=25).grid(row=0, column=1)

        Label(branchframe,text="GRIET",font=("BOLD",16),width=25).grid(row=1,column=0)
        Label(branchframe,text=GRIET,font=("BOLD",16),width=25).grid(row=1,column=1)

        Label(branchframe, text="CBIT",font=("BOLD",16),width=25).grid(row=2, column=0)
        Label(branchframe, text=CBIT, font=("BOLD",16),width=25).grid(row=2, column=1)

        Label(branchframe, text="VASAVI",font=("BOLD",16),width=25).grid(row=3, column=0)
        Label(branchframe, text=Vasavi,font=("BOLD",16), width=25).grid(row=3, column=1)

        Label(branchframe, text="VNR",font=("BOLD",16),width=25).grid(row=4, column=0)
        Label(branchframe, text=VNR,font=("BOLD",16), width=25).grid(row=4, column=1)

        Label(branchframe, text="CVR",font=("BOLD",16),width=25).grid(row=5, column=0)
        Label(branchframe, text=CVR,font=("BOLD",16), width=25).grid(row=5, column=1)

        Label(branchframe, text="MVSR",font=("BOLD",16),width=25).grid(row=6, column=0)
        Label(branchframe, text=MVSR, font=("BOLD",16),width=25).grid(row=6, column=1)

        Label(branchframe, text="Vardhaman",font=("BOLD",16),width=25).grid(row=7, column=0)
        Label(branchframe, text=Vardhaman,font=("BOLD",16), width=25).grid(row=7, column=1)

        Label(branchframe, text="Sreenidhi",font=("BOLD",16),width=25).grid(row=8, column=0)
        Label(branchframe, text=Sreenidhi, font=("BOLD",16),width=25).grid(row=8, column=1)

        Button(root3, text="HOME", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
        Button(root3, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
        Button(root3, text="INFO", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=150, y=650)
        root3.tkraise()





    ###root1####

    if prefercollege!="" and preferbranch!="":
        bothprediction="NOT AVILABLE"
        if prefercollege=="GRIET":
            gender = "M"
            if r.get() == 2:
                gender = "F"
            m = 100000
            M = 0
            data = pd.read_csv(f"Eamcet analysis/Griet/{preferbranch}_2022.csv")
            specialseats = ["CAP", "EWS", "NCC", "NSS", "PH"]
            for i, j, k in zip(data["Eamcet Rank"], data["Sex"], data["Category"]):
                if gender == j:
                    if caste in k :
                        m = min(m, int(i))
                        M = max(M, int(i))
            if int(rank) <= m:
                bothprediction=f"{prefercollege}  100%"
                #print("100%")
            elif m < int(rank) <= M:
                z = (M - int(rank)) * 100 // (M - m)
                #print(round(z, 2))
                bothprediction=f"{prefercollege}   {round(z)}%)"
            else:

                bothprediction="--"
                    #print("Not sure")
            #print(m,M,rank,gender,preferbranch,prefercollege,caste)

        if prefercollege in ("CBIT","VASAVI"):
            caste=caste.replace("_","")
            #print("hi baby")
            data=pd.read_csv(f"Eamcet analysis/{prefercollege}_2022.csv")
            gender="Boys"
            if r.get()==2:
                gender="Girls"
            for i,j,k in zip(data['Branch'],data[f"{caste}_First"],data[f"{caste}_Last"]):
                if preferbranch in i and gender in i:
                    if j in ("", "__", "--", " ", "_", "-"):
                        bothprediction=f"{prefercollege} NO Availabe Data"

                    else:
                        m = int(j) - 5 * int(j) // 100
                        M = int(k) + 5 * int(j) // 100
                        rank = int(rank)
                        if rank <= m:

                            #print(f"{prefercollege} 100%")
                            bothprediction=f"{prefercollege} 100%"
                        elif m < rank <= M:
                            z = (M - rank) * 100 // (M - m)
                            #print(f"{prefercollege}", z)
                            bothprediction=f"{prefercollege} {z}%"
                        else:
                            #print(f"{prefercollege}: NOT SURE FOR THIS RANK")
                            bothprediction=f"{prefercollege}: NOT SURE FOR THIS RANK"

        if prefercollege in("VNR","MVSR","CVR","VARDHAMAN","SREENIDHI"):
            caste=caste.replace("_","")
            data = pd.read_csv(f"Eamcet analysis/{prefercollege}_2022.csv")
            gender = "Boys"
            if r.get() == 2:
                gender = "Girls"
            for i, j, k in zip(data['Branch'], data[f"{caste}_{gender}_First"], data[f"{caste}_{gender}_Last"]):
                if preferbranch in i:
                    if j in ("", "__", "--", " ", "_", "-"):
                        #print(f"{prefercollege} NOT Availabe Data")
                        bothprediction=f"{prefercollege} NO Availabe Data"
                    else:
                        m = int(j) - 5 * int(j) // 100
                        M = int(k) + 5 * int(j) // 100
                        rank = int(rank)
                        if rank <= m:
                            #print(f"{prefercollege}100%")
                            bothprediction=f"{prefercollege} 100%"
                        elif m < rank <= M:
                            z = (M - rank) * 100 // (M - m)
                            #print(f"{prefercollege}", z)
                            bothprediction=f"{prefercollege}  {z}%"
                        else:
                            #print(f"{prefercollege}: NOT SURE FOR THIS RANK")
                            bothprediction=f"{prefercollege}: NOT SURE FOR THIS RANK"
        #predictionframe=Frame(root1,background="blue").place(x=0,y=650)
        #Label(root1, text="prediction Per%",width=30,font=("BOLD", 16)).place(x=10,y=450)
        Label(root1, text=f"prediction Per%      {bothprediction}",font=("BOLD", 16),width=50).place(x=10,y=500)













    #colleges = {"GRIET": GRIET, "CBIT":CBIT, "VASAVI":Vasavi, "VNR":VNR, "SREENIDHI": Sreenidhi, "MVSR": MVSR, "CVR": CVR, "VARDHAMAN": Vardhaman}



if __name__=="__main__":
    background="lightblue"
    root = Tk()
    root.title("EAMCET")
    w_width, w_height = 550, 700
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

    for f in (root1, root2, root3,root4,root5):
        f.grid(row=0, column=0,sticky="news")



    ###### ROOT1 #####
    Frame(root1,width=550,height=700,background=background).pack()
    G_img = Image.open("img.png")
    G_img = G_img.resize((500, 80))
    G_img = ImageTk.PhotoImage(G_img)
    Label(root1, image=G_img).place(x=10,y=10)
    l1 = Label(root1, text="Eamcet Rank",font=("BOLD",16)).place(x=50, y=120)
    rankbox=StringVar()
    rankbox = Entry(root1, width=13, font=("BOLD", 16), relief=FLAT)
    rankbox.place(x=250, y=120)
    l3 = Label(root1, text="Branch",font=("BOLD",16)).place(x=50, y=180)
    branchbox = Combobox(root1, font=("BOLD", 10))
    branchbox['values']=("", "CSE", "CSE_AIML", "CSE_DS", "CSE_CSBS", "MEC", "IT", "ECE", "EEE", "CIVIL")
    branchbox.current(0)
    branchbox.place(x=250, y=180)

    l21 = Label(root1, text="College", font=("BOLD", 16)).place(x=50, y=240)
    collegebox = Combobox(root1, font=("BOLD", 10))
    collegebox['values'] = ("","GRIET","CBIT","VASAVI","VARDHAMAN","VNR","CVR","MVSR","SREENIDHI")
    collegebox.current(0)
    collegebox.place(x=250, y=240)

    l21 = Label(root1, text="Category", font=("BOLD", 16)).place(x=50, y=300)
    category=Combobox(root1,font=("BOLD", 10))
    category['values']=("","OC","BC_A","BC_B","BC_C","BC_D","BC_E","SC","ST","EWS","PH")
    category.current(0)
    category.place(x=250,y=300)


    l5 = Label(root1, text="Gender",font=("BOLD",16)).place(x=50, y=360)
    r = IntVar()
    s = ttk.Style()
    s.configure('Wild.TRadiobutton', background=background, foreground="blue", font=('Arial Bold', 16),
                focuscolor=s.configure(".")["background"])
    genMale = ttk.Radiobutton(root1, text='Male', value=1, variable=r, style='Wild.TRadiobutton', takefocus=False)
    genMale.place(x=250, y=360)
    genFemale = ttk.Radiobutton(root1, text='Female', value=2, variable=r, style='Wild.TRadiobutton',
                                takefocus=False)
    genFemale.place(x=350, y=360)

    Button(root1,text="Search",command=goto,font=("BOLD",16)).place(x=50,y=420)
    Button(root1,text="Clear",command=lambda:root.destroy(),font=("BOLD",16)).place(x=250,y=420)
    Button(root1, text="HOME", command= lambda :root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
    Button(root1, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
    Button(root1, text="INFO", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=150, y=650)


    #### ROOT 2   #college LOGO#####

    grietlogo = ImageTk.PhotoImage(Image.open("collegeImages/griet.png").resize((550, 200)))
    cbitlogo=ImageTk.PhotoImage(Image.open("collegeImages/cbit.png").resize((550, 200)))
    vasavilogo=ImageTk.PhotoImage(Image.open("collegeImages/vasavi.png").resize((550, 200)))
    mvsrlogo=ImageTk.PhotoImage(Image.open("collegeImages/mvsr.png").resize((550, 200)))
    sreenidhilogo=ImageTk.PhotoImage(Image.open("collegeImages/sreenidhi.png").resize((550, 200)))
    vardhamanlogo=ImageTk.PhotoImage(Image.open("collegeImages/vardhaman.png").resize((550, 200)))
    vnrlogo=ImageTk.PhotoImage(Image.open("collegeImages/vnr.png").resize((550, 200)))
    cvrlogo=ImageTk.PhotoImage(Image.open("collegeImages/cvr.png").resize((550, 200)))


    collegedict={"griet":grietlogo,"cbit":cbitlogo,"vasavi":vasavilogo,"mvsr":mvsrlogo,"vnr":vnrlogo,"sreenidhi":sreenidhilogo,"cvr":cvrlogo,
                 "vardhaman":vardhamanlogo}
    ##### ROOT 2####
    collegebranches={"griet":"CSE,CSE_AIML,CSE_DS,CSE_CSBS,MEC,IT,ECE,EEE,CIVIL",
                     "cbit":"CSE,CSE_AIML,MEC,IT,ECE,EEE,CIVIL",
                     "vasavi":"CSE,CSE_AIML,MEC,IT,ECE,EEE,CIVIL",
                     "vnr":"CSE,CSE_AIML,CSE_DS,CSE_CSBS,MEC,IT,ECE,EEE,CIVIL",
                     "cvr":"CSE,CSE_AIML,CSE_DS,MEC,IT,ECE,EEE,CIVIL",
                     "mvsr":"CSE,MEC,IT,ECE,EEE,CIVIL",
                    "vardhaman":"CSE,CSE_AIML,MEC,IT,ECE,EEE,CIVIL",
                     "sreenidhi":"CSE,CSE_AIML,CSE_DS,MEC,IT,ECE,EEE,CIVIL"}

    collegename={"griet":"GOKARAJU RANGARAJU INSTITUTE OF ENGERRNING AND TECHNOLOGY",
                 "cbit":"CHAITHNYA BARATHI INSTITUTE OF TECHONOLGY",
                 "vasavi":"VASAVI",
                 "vnr":"VNR",
                 "cvr":"CVR",
                 "mvsr":"MVSR",
                 "sreenidhi":"SREENIDHI",
                 "vardhaman":"VARDHAMAN"}
    collegeadress={}
    collegeurl={}
                   # "cbit":"CSE","CSE_AIML","CSE_DS","CSE_CSBS","MEC","IT","ECE","EEE","CIVIL"}
    def collegeframe(name):
        #root2image = Frame(master=root2, width=550, height=200, background="#d3d3d3").place(x=0, y=50)

        detailFrame2 = Frame(root2)
        detailFrame2.place(x=0,y=50)
        userFrame2 = Label(detailFrame2, image=collegedict[name],width=550, height=250, relief=FLAT)
        userFrame2.pack(padx=0, pady=10)
        collegedetails=Frame(root2,bg="white")
        collegedetails.place(x=0,y=320)
        Label(collegedetails,text="COLLEGE NAME ",width=20).grid(row=0,column=0)
        Label(collegedetails, text=collegename[name],width=60).grid(row=0, column=1)

        Label(collegedetails, text="COLLEGE CODE",width=20).grid(row=1, column=0)
        Label(collegedetails, text=name, width=60).grid(row=1, column=1)

        Label(collegedetails,text="AVILABLE BRANCHES",width=20).grid(row=2,column=0)
        Label(collegedetails,text=collegebranches[name],width=60).grid(row=2,column=1)

        Label(collegedetails, text="NAAC RANK",width=20).grid(row=3, column=0)
        Label(collegedetails, text="A++", width=60).grid(row=3, column=1)


        Label(collegedetails, text="COLLEGE ADDRESS",width=20).grid(row=4, column=0)
        Label(collegedetails, text="NIZAMPET,HYDERABAD", width=60).grid(row=4, column=1)

        Label(collegedetails, text="TUTION FEE",width=20).grid(row=5, column=0)
        Label(collegedetails, text="1,30,000", width=60).grid(row=5, column=1)

        Label(collegedetails, text="HOSTEL FECILITY",width=20).grid(row=6, column=0)
        Label(collegedetails, text="GIRLS", width=60).grid(row=6, column=1)

        Label(collegedetails, text="BUS FECILITY",width=20).grid(row=5, column=0)
        Label(collegedetails, text="YES", width=60).grid(row=5, column=1)

        Label(collegedetails, text="COLLEGE URL",width=20).grid(row=8, column=0)
        Button(collegedetails, text="griet.ac.in", width=60,foreground="blue").grid(row=8, column=1)



        #Label(collegedetails, text="1").grid(row=1, column=0)
        #Label(collegedetails, text=collegebranches[name], width=50).grid(row=2, column=1)



    colleges=["GRIET","CBIT","VASAVI","VARDHAMAN","VNR","CVR","MVSR","SREENIDHI"]
    #for j in range(8):
    x=tkinter.Frame(master=root2,relief=tkinter.RAISED,background="white",border=3)
    x.grid(row=0,column=0,pady=(10,10))
    Button(master=x,text="GRIET",command=lambda :collegeframe("griet"),font=("BOLD",10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=1)
    Button(master=x, text="CBIT", command=lambda :collegeframe("cbit"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=2)
    Button(master=x, text="VASAVI", command=lambda :collegeframe("vasavi"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=3)
    Button(master=x, text="VNR", command=lambda: collegeframe("vnr"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=4)
    Button(master=x, text="SREENIDHI", command=lambda: collegeframe("sreenidhi"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=5)
    Button(master=x, text="MVSR", command=lambda: collegeframe("mvsr"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=6)
    Button(master=x, text="CVR", command=lambda: collegeframe("cvr"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=7)
    Button(master=x, text="VARDHAMAN", command=lambda: collegeframe("vardhaman"), font=("BOLD", 10)).pack()
    """detailFrame2 = Frame(root2, bd=10, bg=background)
    detailFrame2.pack(fill=X)
    userFrame2 = Frame(detailFrame2, bd=10, width=300, height=250, relief=FLAT, bg=background)
    userFrame2.pack(padx=10, pady=10)"""






    Button(root2, text="HOME", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
    Button(root2, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
    Button(root2, text="INFO", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=150, y=650)
    root1.tkraise()
    root1.mainloop()