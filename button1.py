

from tkinter import *
import tkinter as tk
import glob
import os
import datetime
import shutil
 
win = tk.Tk() 
 


def origin():
    flist = os.listdir('C:/Users/Andrew Smith/Desktop/Folder_Ori/')    
    lbox = tk.Listbox(win)
    lbox.pack()

    for item in flist:
        lbox.insert(tk.END, item)
        

def destination():
    slist = os.listdir('C:/Users/Andrew Smith/Desktop/Folder_Dest/')    
    lbox = tk.Listbox(win)
    lbox.pack()

    for item in slist:
        lbox.insert(tk.END, item)

  

def fileTran():
    def GetFileList(path, type):
        return glob.glob(path + "*" + type)

    originPath = 'C:/Users/Andrew Smith/Desktop/Folder_Ori/'
    destinationPath = 'C:/Users/Andrew Smith/Desktop/Folder_Dest/'
    fileType = ".txt"


    fileList = GetFileList(originPath, fileType)

    for file in fileList:
        modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        todaysDate = datetime.datetime.today()
    
        filePathList = file.split("\\")
        filename = filePathList[-1]
    
        modifyDateLimit = modifyDate + datetime.timedelta(days=1)

        if modifyDateLimit > todaysDate:
            shutil.copy2(file, destinationPath + filename)




btn_Ori = Button(win, text ='Origin', command =origin) 
btn_Ori.pack()

btn_Des = Button(win, text ='Destination', command =destination) 
btn_Des.pack()

btn_Tran = Button(win, text ='Transfer', command =fileTran) 
btn_Tran.pack()
    





if __name__=='__main__':  
    mainloop()