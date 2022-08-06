import pandas as pd
data=pd.read_csv("Eamcet analysis/ALL COLLEGES.csv")
import os
#for i,j,k in zip(data["INST CODE"],data["BRANCH"],data["BC_D BOYS"]):
 #   if i=="GRRR":


collegedetails=['INST CODE', 'INSTITUTE NAME', 'PLACE', 'DIST', 'COED', 'TYPE',
       'YEAR OF ESTB', 'BRANCH', 'BRANCH NAME', 'OC BOYS', 'OC GIRLS',
       'BC_A BOYS', 'BC_A GIRLS', 'BC_B BOYS', 'BC_B GIRLS', 'BC_C BOYS',
       'BC_C GIRLS', 'BC_D BOYS', 'BC_D GIRLS', 'BC_E BOYS', 'BC_E GIRLS',
       'SC_BOYS', 'SC_GIRLS', 'ST_BOYS', 'ST_GIRLS', 'TUITION FEE',
       'AFFILIATED']
cbitbranches=[]
collegecode = {"griet": "GRR", "cbit": "CBIT", "vasavi": "VASV", "vnr": "VJEC", "cvr": "CVRH", "mvsr": "MVSR",
               "vardhaman": "VMEG", "sreenidhi": "SNIS"}

new=data.dropna(subset=['OC BOYS', 'OC GIRLS',
       'BC_A BOYS', 'BC_A GIRLS', 'BC_B BOYS', 'BC_B GIRLS', 'BC_C BOYS',
       'BC_C GIRLS', 'BC_D BOYS', 'BC_D GIRLS', 'BC_E BOYS', 'BC_E GIRLS',
       'SC_BOYS', 'SC_GIRLS', 'ST_BOYS', 'ST_GIRLS'])
collegesdetails=pd.DataFrame(new)
# creating excel writer object
writer = pd.ExcelWriter('collegesdetails10.xlsx')
branche=[]
for i,j in zip(data.index,data["INST CODE"]):
       if data.loc[i,'BRANCH'] not in branche:
              branche.append(data.loc[i,'BRANCH'])
       if j not in("GRRR","CBIT","VASV","VJEC","CVRH","MVSR","VMEG","SNIS","BVRI","JNTH","OUCE","MGIT","MLRD","CVRH","CVSR"):
             data.drop(i,inplace=True)
#print(data.to_string())
print(branche)
data.to_excel(writer)
writer.save()

