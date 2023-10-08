
from cgitb import text
from tkinter import *
import tkinter as tk 
top = Tk()
top.title("ALGO data ")
from tkinter import Menu
import os
global master
from tkinter.filedialog import askopenfilename
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        master.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def algo1():
    global text
    global master
    master = Tk()
    master.title("1. LOGISTIC REGRESSION")
    master.geometry("440x520")
    #master = Tk()  
    master.geometry("300x400")  
    
    labelframe1 = LabelFrame(master, text="Details")  
    labelframe1.pack(fill="both", expand="yes")  
    
    masterlabel = Label(labelframe1, text="Train test split of 80% /20%")  
    masterlabel.pack()  
    
    labelframe2 = LabelFrame(master, text = "Confusion Matrix")  
    labelframe2.pack(fill="both", expand = "yes")  
    
    bottomlabel = Label(labelframe2,text = "[[40  3]")  
    bottomlabel1 = Label(labelframe2,text = "[ 4 13]]")  
    bottomlabel.pack()  
    bottomlabel1.pack()
    labelframe1 = LabelFrame(master, text="Accuracy_Score")  
    labelframe1.pack(fill="both", expand="yes")  
    
    masterlabel = Label(labelframe1, text="0.8833333333333333")  
    masterlabel.pack()
    master.mainloop()  


    # type area
    master.mainloop()

# img1 = PhotoImage(file='D:\project_file\HDP\outputKNN.png')
def algo2():
    global text
    global master
    master = Tk()
    master.title("2. K NEAREST NEIGHBOR")
    master.geometry("440x520")
    #master = Tk()  
    master.geometry("400x400")  
    
    labelframe1 = LabelFrame(master, text="Details")  
    labelframe1.pack(fill="both", expand="yes")  
    
    masterlabel = Label(labelframe1, text="Number of neighbors used")  
    masterlabel.pack()  
    masterlabel = Label(labelframe1, text="KNeighborsClassifier(n_neighbors=6)")  
    masterlabel.pack()  

    #img1 = PhotoImage(file='D:\project_file\HDP\outputKNN.png')
    #masterlabel2 = Label(master, image=img1)  
    #masterlabel2.pack() 
    


    labelframe2 = LabelFrame(master, text = "Confusion Matrix")  
    labelframe2.pack(fill="both", expand = "yes")  
    
    bottomlabel = Label(labelframe2,text = "[[42  1]")  
    bottomlabel1 = Label(labelframe2,text = "[ 3 14]]")  
    bottomlabel.pack()  
    bottomlabel1.pack()
    labelframe1 = LabelFrame(master, text="Accuracy_Score")  
    labelframe1.pack(fill="both", expand="yes")  
    
    masterlabel = Label(labelframe1, text="0.9333333333333333")  
    masterlabel.pack()



    master.mainloop()  


def algo3():
    global text
    global master

    master = Tk()
    master.title("3. SUPPORT VECTOR CLASSIFIER")
    master.geometry("440x520")
    #master = Tk()  
    master.geometry("300x400")  
    
    labelframe1 = LabelFrame(master, text="Details")  
    labelframe1.pack(fill="both", expand="yes")  
    
    masterlabel = Label(labelframe1, text="Number of SV used")  
    masterlabel.pack()  
    masterlabel = Label(labelframe1, text="SVC(C=0.6, random_state=0)")  
    masterlabel.pack()  
    #img = PhotoImage(file='D:\project_file\HDP\outputKNN.png')
    #masterlabel = Label(master, image=img)  
    #masterlabel.pack() 
    


    labelframe2 = LabelFrame(master, text = "Confusion Matrix")  
    labelframe2.pack(fill="both", expand = "yes")  
    
    bottomlabel = Label(labelframe2,text = "[[40  3]")  
    bottomlabel1 = Label(labelframe2,text = "[ 3 14]]")  
    bottomlabel.pack()  
    bottomlabel1.pack()
    labelframe1 = LabelFrame(master, text="Accuracy_Score")  
    labelframe1.pack(fill="both", expand="yes")  
    
    masterlabel = Label(labelframe1, text="0.9")  
    masterlabel.pack()



    master.mainloop()
def algo4():
    global text
    global master

    master = Tk()
    master.title("4. DECISION TREE CLASSIFIER")
    master.geometry("440x520")
    #master = Tk()  
    master.geometry("300x400")  
    
    labelframe1 = LabelFrame(master, text="Details")  
    labelframe1.pack(fill="both", expand="yes")  
    
    masterlabel = Label(labelframe1, text="Number of leaf node used")  
    masterlabel.pack()  
    masterlabel = Label(labelframe1, text="DecisionTreeClassifier(criterion='entropy', max_leaf_nodes=3, random_state=0)")  
    masterlabel.pack()  
    #img = PhotoImage(file='D:\project_file\HDP\outputKNN.png')
    #masterlabel = Label(master, image=img)  
    #masterlabel.pack() 
    


    labelframe2 = LabelFrame(master, text = "Confusion Matrix")  
    labelframe2.pack(fill="both", expand = "yes")  
    
    bottomlabel = Label(labelframe2,text = "[[43  0]")  
    bottomlabel1 = Label(labelframe2,text = "[ 3 14]]")  
    bottomlabel.pack()  
    bottomlabel1.pack()
    labelframe1 = LabelFrame(master, text="Accuracy_Score")  
    labelframe1.pack(fill="both", expand="yes")  
    
    masterlabel = Label(labelframe1, text="0.95")  
    masterlabel.pack()



    master.mainloop() 
def algo5():
        global text
        global master

        master = Tk()
        master.title("Count..")
        master.geometry("840x220")
        #master = Tk()  
        #master.geometry("300x400")  
        
        labelframe1 = LabelFrame(master, text="Accuracy_Score")  
        labelframe1.pack(fill="both", expand="yes")  
        
        masterlabel = Label(labelframe1, text="Logistic Regression [0.8833333333333333], KNearestNeighbours[0.9333333333333333],SupportVector[0.9]")  
        masterlabel.pack()  
        masterlabel = Label(labelframe1, text="DecisionTree[0.95],RandomForest[0.95],ANN[0.9166666666666666]")  
        masterlabel.pack()  
        
        master.mainloop()

#def algo6():     
       










# ifle name part 
filename = None
def UploadAction(event=None):
    filename = askopenfilename()
    # Cut path to the file off
    filename = filename.split('heart_failure_clinical_records_dataset.csv')[len(filename.split('heart_failure_clinical_records_dataset.csv'))-1]
    print('Selected:', filename)
    label1['text'] = filename


    
button1 = tk.Button(text='heart_failure_clinical_records_dataset.csv', command=UploadAction, bg='#C0C0C0', fg='black')
button1.pack(padx=2, pady=5)
label1 = tk.Label(text='Please choose a file')
label1.pack(padx=2, pady=2)
#////
#algo 
 
menubutton = Menubutton(top, text = "ALGO", relief = FLAT)  
    
  
menubutton.menu = Menu(menubutton) 
 # type: ignore  
menubutton["menu"]=menubutton.menu  
  
menubutton.menu.add_command(label = "1. LOGISTIC REGRESSION",command=algo1)  
  
menubutton.menu.add_command(label = "2. K NEAREST NEIGHBOR",command=algo2)  
menubutton.menu.add_command(label = "3. SUPPORT VECTOR CLASSIFIER",command=algo3)  
menubutton.menu.add_command(label = "4. DECISION TREE CLASSIFIER",command=algo4)
menubutton.menu.add_command(label = "5. RANDOM FOREST CLASSIFCATION")  
menubutton.menu.add_command(label = "6. ANN")
menubutton.menu.add_command(label = "COMPARE ALL",command=algo5)
menubutton.pack()  

#/////


top.mainloop()
