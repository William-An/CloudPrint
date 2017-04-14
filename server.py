import web
import os
import sys
import subprocess
import time

urls = ('/upload', 'Upload')
 
class Upload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return  """
                    <html><head></head><body>
					<form method="POST" enctype="multipart/form-data" action="">
					<input type="file" name="myfile" />
					<br/>
					<br/>
					<input type="submit" />
					</form>
					</body></html>
                """

    def POST(self):
        x = web.input(myfile={})
        filedir = '\\File'                                  # change this to the directory you want to store the file in.
        if 'myfile' in x:                                   # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/')    # replaces the windows-style slashes with linux ones.
            filename=filepath.split('\\')[-1]               # splits the and chooses the last part (the filename with extension)
            if 'doc' not in filename[-1:-4]:                # Check if doc, TODO integrate in HTML
                raise web.seeother('/upload')
            fout = open(filedir +'\\'+ filename,'wb')       # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read())                # writes the uploaded file to the newly created file.
            fout.close()                                    # closes the file, upload complete.
        doc_print(filedir+"\\"+filename)
        raise web.seeother('/upload')


if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()


                        
def doc_print(filename):
    try:
	   subprocess.run(["winword",filename,"/mFilePrintDefault"],timeout=5)
    except subprocess.TimeoutExpired as err:
        return  """
                <a href="/upload">Timeout</a>
                """
    # os.popen("winword "+filename+" /mFilePrintDefault")
    # time.sleep(3)
    # print("slee[")
    # os.popen("taskkill /im winword.exe")
