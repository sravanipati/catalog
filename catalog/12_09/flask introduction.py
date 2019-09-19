https://github.com/SaralKumarKaviti/Flask_Project/blob/master/main.py
Flask Intrroduction
Flask variable declaration
Flask url-for
file - uploading
mail-sending
otp-generation
csv formate
Database Connection
   -crud-create,retrive,update,delete  (sqlite database)
login session with validation
project deployment using AWS


--flask introduction---


MVC - model , view ,controller
model - datalink -sqlite db
view - presentation -html,css,bootstrap(front end)
controller-application - python with Flask Frame Work
MVC is mostly depend on osi layer
i)presentation
ii)application
iii)data link
flask is a frame work in python
wsgi-web service gateway interface
--server side error
zinz2--client side error--HTML error


1)flask introduction programme

pip install flask = flask - library
from flask = flask - package
import Flask = Flask - module
every .py file is we can use as a module and package
__name__=define the project
route - key word - used to go url -
'''@app.route("/info/details")
def id():
        return"Hello Details"'''
- (localhost 5000/info/details)  - info/details is the url
- id is the user defined function
-with in the return is content

localhost:-port numbers
emil-465
db-80
mysql-3306
PYHTON-5000

---return - return the content in web page

the main programme run in cmd with the following commands
first command = python main.py
first we can add flask = set FLASK_APP=main.py
we can run the flask = flask run
every time we cant give this commands so we can use some small lines in end of the programme
---if __name__=='__main__':
           app.run(debug=True)
after just refreshing we can GET the content within the url-function 




2)Flask variable Declaration

Str-int-float
@app.route("/information/<name>/<int:age>/<float:salary>")
def sif(name,age,salary):
        return"Hello {} age {} and salary {}".format(name,age,salary)


3)url
