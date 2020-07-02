
from tkinter import *
import tkinter as tk
import glob
import os
import datetime
import shutil
import tkinter.filedialog

class TransferGUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI")

        self.label = Label(master, text="File Transfer")
        self.label.pack()

        self.greet_button = Button(master, text="Origin", command=self.origin)
        self.greet_button.pack()

        self.close_button = Button(master, text="Destination", command=self.destination)
        self.close_button.pack()

        self.btn_Tran = Button(master, text ="Transfer", command =self.fileTran) 
        self.btn_Tran.pack()


    def origin(self):
        self.flist = tkinter.filedialog.askdirectory()
        self.flist2 = self.flist + '/'


    def destination(self):
        self.slist = tkinter.filedialog.askdirectory()
        self.slist2 = self.slist + '/'


    def fileTran(self):

        originPath = self.flist2
        destinationPath = self.slist2
        fileType = ".txt"

        def GetFileList(path, type):
            return glob.glob(path + "*" + type)
        fileList = GetFileList(originPath, fileType)

        for file in fileList:
            modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
            todaysDate = datetime.datetime.today()
        
            filePathList = file.split("\\")
            filename = filePathList[-1]
        
            modifyDateLimit = modifyDate + datetime.timedelta(days=1)

            if modifyDateLimit > todaysDate:
                shutil.copy2(file, destinationPath + filename)








root = Tk()
my_gui = TransferGUI(root)
root.mainloop()
