
from tkinter import *
import glob
import os
import datetime
import shutil

root = Tk() 
root.geometry('200x100') 
  

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
   



btn_Tran = Button(root, text ='Transfer', command =fileTran()) 
btn_Tran.grid(row = 1, column = 1, pady = 10)




if __name__=='__main__':  
    mainloop()
