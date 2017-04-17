import web
import os
import sys
import subprocess
import time

urls = ('/upload', 'Upload')
 
class Upload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        render = web.template.render('static/')
        return render.index()

    def POST(self):
        x = web.input(myfile={})
        filedir = '.\\File'                                  # change this to the directory you want to store the file in.
        if 'myfile' in x:                                   # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/')    # replaces the windows-style slashes with linux ones.
            filename=filepath.split('\\')[-1]               # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'\\'+ filename,'wb')       # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read())                # writes the uploaded file to the newly created file.
            fout.close()                                    # closes the file, upload complete.
        filename = filedir+"\\"+filename
        if 'doc' or 'pdf' in filename[-4:]:                
            printer(filename)
        # else if 'pdf'in filename[-4:]: TODO finish pdf printing
        #     doc_print(filename,printer='arco')
        raise web.seeother('/upload')


if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()


                        
def printer(filename,printer='winword'):
    try:
        if printer == 'winword':
        	subprocess.run([printer,filename,"/mFilePrintDefault"],timeout=30)
        elif printer == 'acrobat':
            subprocess.run([printer,'/t',filename],timeout=30)
        os.system("del "+filename)
    except:
        os.system("del "+filename)   # Clear
        return """
                <a href="/upload">Timeout</a>
                """
