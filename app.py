from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

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
def hello_world():
    #render_template() automatically searches within templates directory for html page
    return render_template('index.html')

@app.route('/string/', methods=['POST', 'GET'])
def string():
    if request.method == 'POST':
        #get string from html form
        string = request.form['content']
        new_str = inputString(content=string)

        try:
            database.session.add(new_str)
            database.session.commit()
            return redirect('/string/')
        except:
            return "Error handling string!"

    else:
        string = inputString.query.order_by(inputString.id.desc()).limit(1)
        return render_template('string.html', string=string)

@app.route('/file/')
def file():
    return render_template('file.html')


if __name__ == '__main__':
    app.run()
