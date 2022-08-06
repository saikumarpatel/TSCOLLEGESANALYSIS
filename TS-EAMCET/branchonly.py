import pandas as pd
from EAMCETTOP10COLLEGES import *
#print(data)
#print(data[2:]["Branch"])

castlist=["OC","BC_A","BC_B","BC_C","BC_D","BC_E","SC","ST","EWS","PH"]
def GRIET(rank,caste,gender,preferbranch):
    m=100000
    M=0
    data=pd.read_csv(f"Eamcet analysis/Griet/{preferbranch}_2022.csv")
    specialseats=["CAP","EWS","NCC","NSS","PH"]
    for i,j,k in zip(data["Eamcet Rank"],data["Sex"],data["Category"]):
        if gender==j:
            if caste in k and all(h not in k for h in specialseats):
                m=min(m,int(i))
                M=max(M,int(i))
    if int(rank)<=m:
        print("100%")
        return '100%'
    elif m<int(rank)<=M:
        z = (M - int(rank)) * 100 // (M - m)
        print(round(z,2))
        return f'{z}%'
    else:
        return "--"
def CBIT(rank,caste,gender,branch):
    print("CBIT")

    data = pd.read_csv("Eamcet analysis\CBIT_2022.csv")
    #print(f'{caste}_{gender}_First',f'{caste}_{gender}_Last')
    for i,j,k in zip(data["Branch"],data[f'{caste}_First'],data[f"{caste}_Last"]):
        if branch in i and gender in i:
            if j in ("","__","--"," ","_","-"):
                print("CBIT NOT Availabe Data")
                return "__"
            else:
                m = int(j) - 5 * int(j) // 100
                M = int(k) + 5 * int(j) // 100
                rank = int(rank)
                if rank <= m:

                    print("CBIT 100%")
                    return "100%"
                elif m < rank <= M:
                    z=(M-rank) * 100 // (M - m)
                    print("CBIT",z)
                    return str(z)+"%"
                else:
                    print("CBIT: NOT SURE FOR THIS RANK")
                    return "__"
def Vasavi(rank,caste,gender,branch):
    print("VASAVI")
    data = pd.read_csv("Eamcet analysis\Vasavi_2022.csv")
    #print(data["Branch"], data[f'{caste}_First'], data[f"{caste}_Last"])
    for i, j, k in zip(data["Branch"], data[f'{caste}_First'], data[f"{caste}_Last"]):
        #if branch in i and gender in i:
        if branch in i and gender in i:
            if j in ("", "__", "--", " ", "_", "-"):
                print("NOT Availabe Data")
                return "__"
            else:
                m = int(j) - 5 * int(j) // 100
                M = int(k) + 5 * int(j) // 100
                rank = int(rank)
                if rank <= m:

                    print(" 100%")
                    return "100%"
                elif m < rank <= M:
                    z = (M - rank) * 100 // (M - m)
                    print( z)
                    return str(z) + "%"
                else:
                    print(" NOT SURE FOR THIS RANK")
                    return "__"


def Vardhaman(rank,caste,gender,branch):
    print("VARDHAMAN",rank,caste,gender,branch)
    data=pd.read_csv("Eamcet analysis/Vardhaman_2022.csv")
    #print(data[f'{caste}_{gender}_First'],data[f'{caste}_{gender}_Last'])
    for i,j,k in zip(data["Branch"],data[f'{caste}_{gender}_First'],data[f'{caste}_{gender}_Last']):
        if branch==i:
            if j in ("", "__", "--", " ", "_", "-"):
                print(" NOT Availabe Data")
                return "__"
            else:
                m = int(j) - 5 * int(j) // 100
                M = int(k) + 5 * int(j) // 100
                rank = int(rank)
                if rank <= m:

                    print(" 100%")
                    return "100%"
                elif m < rank <= M:
                    z = (M - rank) * 100 // (M - m)
                    print( z)
                    return str(z) + "%"
                else:
                    print(" NOT SURE FOR THIS RANK")
                    return "__"

def VNR(rank,caste,gender,branch):
    print("VNR")
    data=pd.read_csv("Eamcet analysis/VNR_2022.csv")
    for i,j,k in zip(data["Branch"],data[f'{caste}_{gender}_First'],data[f'{caste}_{gender}_Last']):
        #print(i,j,k)
        if branch==i:
            if j in ("", "__", "--", " ", "_", "-"):
                print(" NOT Availabe Data")
                return "__"
            else:
                m = int(j) - 5 * int(j) // 100
                M = int(k) + 5 * int(j) // 100
                rank = int(rank)
                if rank <= m:

                    print("100%")
                    return "100%"
                elif m < rank <= M:
                    z = (M - rank) * 100 // (M - m)
                    print( z)
                    return str(z) + "%"
                else:
                    print(": NOT SURE FOR THIS RANK")
                    return "__"

def Sreenidhi(rank,caste,gender,branch):
    print("SREENIDHI")
    data=pd.read_csv("Eamcet analysis/Sreenidhi_2022.csv")
    for i,j,k in zip(data["Branch"],data[f'{caste}_{gender}_First'],data[f'{caste}_{gender}_Last']):
        if branch==i:

            if j in ("", "__", "--", " ", "_", "-"):
                print(" NOT Availabe Data")
                return "__"
            else:
                m = int(j) - 5 * int(j) // 100
                M = int(k) + 5 * int(j) // 100
                rank = int(rank)
                if rank <= m:

                    print("CBIT 100%")
                    return "100%"
                elif m < rank <= M:
                    z = (M - rank) * 100 // (M - m)
                    print( z)
                    return str(z) + "%"
                else:
                    print(": NOT SURE FOR THIS RANK")
                    return "__"
    pass
def MVSR(rank,caste,gender,branch):
    print("MVSR")
    data=pd.read_csv("Eamcet analysis/MVSR_2022.csv")
    for i,j,k in zip(data["Branch"],data[f'{caste}_{gender}_First'],data[f'{caste}_{gender}_Last']):
        if branch==i:

            if j in ("", "__", "--", " ", "_", "-"):
                print(" NOT Availabe Data")
                return "__"
            else:
                m = int(j) - 5 * int(j) // 100
                M = int(k) + 5 * int(j) // 100
                rank = int(rank)
                if rank <= m:

                    print(" 100%")
                    return "100%"
                elif m < rank <= M:
                    z = (M - rank) * 100 // (M - m)
                    print("CBIT", z)
                    return str(z) + "%"
                else:
                    print(": NOT SURE FOR THIS RANK")
                    return "__"
    pass
def CVR(rank,caste,gender,branch):
    print("CVR")
    data=pd.read_csv("Eamcet analysis/CVR_2022.csv")
    for i,j,k in zip(data["Branch"],data[f'{caste}_{gender}_First'],data[f'{caste}_{gender}_Last']):
        if branch==i:
            if j in ("", "__", "--", " ", "_", "-"):
                print(" NOT Availabe Data")
                return "__"
            else:
                m = int(j) - 5 * int(j) // 100
                M = int(k) + 5 * int(j) // 100
                rank = int(rank)
                if rank <= m:

                    print(" 100%")
                    return "100%"
                elif m < rank <= M:
                    z = (M - rank) * 100 // (M - m)
                    print("CBIT", z)
                    return str(z) + "%"
                else:
                    print(": NOT SURE FOR THIS RANK")
                    return "__"

def collegeandbranches(prefercollege,preferbranch,caste,r,rank):
    bothprediction="--"
    s=str(caste)
    caste=caste.replace("_","")
    preferbranch=preferbranch.replace("_","")
    if prefercollege=="GRIET":
        gender="M"
        if r.get()==2:
            gender="F"
        m = 100000
        M = 0
        data = pd.read_csv(f"Eamcet analysis/Griet/{preferbranch}_2022.csv")
        for i, j, k in zip(data["Eamcet Rank"], data["Sex"], data["Category"]):
            if gender == j:
                if s in k :
                    print(k)
                    m = min(m, int(i))
                    M = max(M, int(i))
        if int(rank) <= m:
            bothprediction="100%"
            #print("100%")
        elif m < int(rank) <= M:
            m=m-(m*5//100)
            M=M+(M*5//100)
            z = (M - rank) * 100 // (M - m)
            bothprediction=f'{z}%'
            #print(round(z, 2))
        else:#
            bothprediction="NOT SURE"
            #print("Not sure")
        print(preferbranch,m,M)

    if prefercollege in ("CBIT","VASAVI"):
        #print("hi baby")
        data=pd.read_csv(f"Eamcet analysis/{prefercollege}_2022.csv")
        gender="Boys"
        if r==2:
            gender="Girls"
        for i,j,k in zip(data['Branch'],data[f"{caste}_First"],data[f"{caste}_Last"]):
            if preferbranch in i and gender in i:
                if j in ("", "__", "--", " ", "_", "-"):
                    bothprediction="--"

                else:
                    m = int(j) - (5 * int(j) // 100)
                    M = int(k) + (5 * int(j) // 100)
                    rank = int(rank)
                    if int(rank) <= m:

                        #print(f"{prefercollege} 100%")
                        bothprediction="100%"
                    elif m < int(rank) <= M:
                        z = (M - int(rank)) * 100 // (M - m)
                        #print(f"{prefercollege}", z)
                        bothprediction=f"{round(z,2)}%"
                    else:
                        #print(f"{prefercollege}: NOT SURE FOR THIS RANK")
                        bothprediction="NOT SURE"

    if prefercollege in("VNR","MVSR","CVR","VARDHAMAN","SREENIDHI"):
        data = pd.read_csv(f"Eamcet analysis/{prefercollege}_2022.csv")
        gender = "Boys"
        if r == 2:
            gender = "Girls"
        for i, j, k in zip(data['Branch'], data[f"{caste}_{gender}_First"], data[f"{caste}_{gender}_Last"]):
            if preferbranch in i:
                if j in ("", "__", "--", " ", "_", "-"):
                    #print(f"{prefercollege} NOT Availabe Data")
                    bothprediction="--"
                else:
                    m = int(j) - 5 * int(j) // 100
                    M = int(k) + 5 * int(j) // 100
                    rank = int(rank)
                    if int(rank) <= m:
                        #print(f"{prefercollege}100%")
                        bothprediction="100%"
                    elif m < int(rank) <= M:
                        z = (M - int(rank)) * 100 // (M - m)
                        #print(f"{prefercollege}", z)
                        bothprediction=str(round(z,2))+"%"
                    else:
                        #print(f"{prefercollege}: NOT SURE FOR THIS RANK")
                        bothprediction="NOT SURE"
    return bothprediction

