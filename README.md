# CloudPrint #
A cloud printer server base on [webpy](https://github.com/webpy/webpy) and winword.exe

## Procedure ##
* Use webpy to handle submission
* Use `winword.exe` to print doc/docx file
* Use `taskkill` to kill Word after printing

## Installation ##

### Prerequisite ###
* A PC with Microsoft Word installed
* Add the dir of `winword.exe` to PATH

### The server ###
* Clone/download this repository
* Run server.py

