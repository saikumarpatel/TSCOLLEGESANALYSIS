import pandas as pd
import numpy
from tkinter import *
from tkinter import ttk
from threading import Thread
import os
import speech_recognition as sr
import pyttsx3
from PIL import Image, ImageTk
from tkinter import messagebox
from time import sleep

background="white"
data=pd.read_csv("Eamcet analysis/MID_marks.csv")
x=data["Roll No"][::]
y=data["Total"][:]
#print(x,y)
result={}
for i,j in zip(x,y):
	result[i]=j

try:
    engine=pyttsx3.init()
except:
    pass
def speak(text):

    try:
        engine.say(text)
        engine.runAndWait()
    except:
        print("Try not to type more...")

def record():
	print('\nListening...')
	r = sr.Recognizer()
	r.dynamic_energy_threshold = True
	r.energy_threshold = 4000
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		said = ""
		try:
			said = r.recognize_google(audio)
			print(f"\nUser said: {said}")
		except Exception as e:
			print(e)
			# speak("I didn't get it, Say that again please...")
			if "connection failed" in str(e):
				speak("Your System is Offline...", True, True)
			return 'None'
	return said.lower()
def results():
	subjectname="cyber security"
	global textlabel
	global result
	d=UserField.get()
	print(d)
	#print(result[d])
	if d in result:
		mm = str(d)+"\n"+"Cyber security"+"\n"+str(result[d])
	else:
		mm= 'record not found  '
	pass
	root3=Tk()
	popup=Frame(root3,bd=10,width=200,height=200,relief=FLAT)
	popup.pack(pady=(10,10))
	l1=Label(popup,text="ROLL NO").place(x=10,y=10)
	l2=Label(popup,text=d).place(x=100,y=10)
	l3=Label(popup,text="Subject Name").place(x=10,y=50)
	l4=Label(popup,text=subjectname).place(x=100,y=50)
	l5=Label(popup,text="Marks").place(x=10,y=100)
	l6=Label(popup,text=result[d]).place(x=100,y=100)
	#Label(popup,text=mm,font=("bold,19"),width=20,height=20).pack()
	speak(mm)
	root3.tkraise()


if __name__=="__main__":
	root = Tk()
	root.title('results')
	w_width, w_height = 350, 700
	s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
	x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
	root.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))  # center location of the screen
	root.configure()
	root1=Frame(root)
	root1.grid(row=0,column=0,sticky="news")
	root1.pack()
	#greit=PhotoImage(file="cbit.png")
	greit=Image.open("img.png")
	greit=greit.resize((300,300))
	greit=ImageTk.PhotoImage(image=greit)
	c=Label(root1,image=greit)
	c.pack()
	greit1=Image.open("collegeImages/griet.png").resize((300, 300))
	greit1 = ImageTk.PhotoImage(image=greit1)
	Label(root1,image=greit1).pack()

	textlabel=Label(root1,text=("Enter ROLL NUMBER"),font=("BOLD",20),width=22,relief=FLAT).pack()
	UserField = Entry(root1, fg='green', bg='#203647', font=('Montserrat', 16), bd=6, width=22, relief=FLAT)
	UserField.place(x=20, y=30)
	UserField.pack()
	Button(root1,text="result",command=results).pack()
	Button(root1,text="clear",command="").pack()
	root.mainloop()

