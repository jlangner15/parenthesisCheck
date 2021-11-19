from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    #render_template() automatically searches within templates directory for html page
    return render_template('index.html')

@app.route('/string/')
def string():
    return render_template('string.html')

@app.route('/file/')
def file():
    return render_template('file.html')

if __name__ == '__main__':
    app.run()
