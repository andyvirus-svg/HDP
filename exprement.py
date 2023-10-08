from tkinter import *
from tkinter import Menu
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
global text
global master

master = Tk()
master.title("4. DECISION TREE CLASSIFIER")
master.geometry("440x520")
#master = Tk()  
#master.geometry("300x400")  
  
labelframe1 = LabelFrame(master, text="Accuracy_Score")  
labelframe1.pack(fill="both", expand="yes")  
  
masterlabel = Label(labelframe1, text="Logistic Regression [0.8833333333333333], KNearestNeighbours[0.9333333333333333],SupportVector[0.9]")  
masterlabel.pack()  
masterlabel = Label(labelframe1, text="DecisionTree[0.95],RandomForest[0.95],ANN[0.9166666666666666]")  
masterlabel.pack()  
#img = PhotoImage(file='D:\project_file\HDP\compere1.png')
#masterlabel = Label(master, image=img)  
#masterlabel.pack() 
 


#labelframe2 = LabelFrame(master, text = "Confusion Matrix")  
#labelframe2.pack(fill="both", expand = "yes")  
#  
#bottomlabel = Label(labelframe2,text = "[[43  0]")  
#bottomlabel1 = Label(labelframe2,text = "[ 3 14]]")  
#bottomlabel.pack()  
#bottomlabel1.pack()
#labelframe1 = LabelFrame(master, text="Accuracy_Score")  
#labelframe1.pack(fill="both", expand="yes")  
#  
#masterlabel = Label(labelframe1, text="0.95")  
#masterlabel.pack()



#master.mainloop()  


 # type area
master.mainloop()
