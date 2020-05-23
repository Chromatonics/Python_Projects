
import sqlite3

conn = sqlite3.connect('test1.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        files_txt TEXT \
        )")
    conn.commit()
conn.close()



fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

subs = '.txt'
  
res = [i for i in fileList if subs in i]



conn = sqlite3.connect("test1.db")

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(files_txt) VALUES (?)", \
                ('Hello.txt',))
    cur.execute("INSERT INTO tbl_files(files_txt) VALUES (?)", \
                ('World.txt',))
    conn.commit()

conn.close()



print ("All files ending in .txt: " + str(res))


