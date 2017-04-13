import web
import os
import sys
import time, os
from subprocess import Popen

urls = ('/upload', 'Upload', '/fuck', 'Exec')


class Exec:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        filedir = r'C:\Users\Windows\Desktop\File' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('\\')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'\\'+ filename,'wb') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        Popen(filedir+"\\"+filename)
        raise web.seeother('/fuck')
    
class Upload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        filedir = r'C:\Users\Windows\Desktop\File' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('\\')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'\\'+ filename,'wb') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        doc_print(filedir+"\\"+filename)
        raise web.seeother('/upload')


if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()


                        
def doc_print(filename):
    os.popen("winword "+filename+" /mFilePrintDefault")
    time.sleep(3)
    # print("slee[")
    os.popen("taskkill /im winword.exe")
