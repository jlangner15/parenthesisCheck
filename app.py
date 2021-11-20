from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from Brackets_Validator import check_brackets_from_string

app = Flask(__name__)
#configure a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strings.db'

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

        new_str = inputString(content=string) #creates new database item instance, assigning the column 'content' to the string passed

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
    return render_template('file.html')


if __name__ == '__main__':
    app.run()
