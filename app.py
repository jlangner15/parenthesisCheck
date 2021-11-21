from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from Brackets_Validator import brackets_validator, brackets_validator_from_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
#configure a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strings.db'
app.config['UPLOAD_FOLDER'] = 'static/' #folder to save files
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 #1MB max upload size
app.config['UPLOAD_EXTENSIONS'] = ['.txt', '.py', '.cpp', '.js', '.css', '.html', '.yaml', '.json', '.c'] #supported file extensions

#init the database
database = SQLAlchemy(app)

'''
If we are going to store any strings on the website and have user input we
have to establish a database. 
Below is the class that simply creates a database for each string and associates
a unique ID to identify such string.
'''
class inputString(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    content = database.Column(database.String(1000), nullable=False) #max string length is 1000 chars
    isBalanced = database.Column(database.String(1000), nullable=False) #outcome of brackets_validator(str)

    def __repr__(self):
        return 'string %s' % self.id


@app.route('/')
def home():
    #render_template() automatically loags corresponding .html file from /templates
    return render_template('home.html')

@app.route('/string/', methods=['POST', 'GET'])
def string():
    #request gets the submission of the html form in templates/string.html
    if request.method == 'POST':

        string = request.form['content'] #get string from html form labeled as content in .html
        outcome = brackets_validator(str(string)) #check brackets_validator for outcome on string

        boolResult = ""
        if outcome == -1:
            boolResult = "True"
        else:
            boolResult = "False! Error at index: " + str(outcome)

        new_str = inputString(content=string,isBalanced=boolResult) #creates new database item instance, assigning the column 'content' to the string passed and boolResult to 'isBalanced'

        #try to add new database item instance to database
        try:
            database.session.add(new_str)
            database.session.commit()
            return redirect('/string/')
        except:
            return "Error handling string!"

    #pass the most recent database entry row into templates/string.html file to be displayed
    else:
        string = inputString.query.order_by(inputString.id.desc()).limit(1)

        return render_template('string.html', string=string)

@app.route('/file/')
def file():
    #pass in blank file and suggest upload
    return render_template('file.html',content="Please upload a file",filename="")


@app.route('/display', methods=['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file'] #get the file from request input
        filename = secure_filename(f.filename) #this removes any unecssary direcotry parenthesis

        #filename os '' when used tries to submit with no file
        if filename == '':
            return render_template('file.html',content="Please upload a file")

        filename_split = os.path.splitext(filename)[1]

        #check that the file is a supported extension
        if filename_split not in app.config['UPLOAD_EXTENSIONS']:
            return render_template('file.html', content="Please upload the correct file type")

        #save the file for the application to read
        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename, "r")
        content = file.read()

        outcome = brackets_validator(str(content)) #check bracked validator for the file content

        if outcome == -1:
            boolResult = "True"
        else:
            boolResult = "False! Error at index: " + str(outcome)

    return render_template('file.html', content=boolResult, filename=filename)


if __name__ == '__main__':
    app.run()
