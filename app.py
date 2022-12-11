from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/coursehelp')
def coursehelp():
    return render_template('coursehelp.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/thread')
def thread():
    return render_template('thread.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/testing')
def testing():
    return render_template('testing.html')

if __name__ == "__main__":
    Flask.run(app, "0.0.0.0", 5000, True)
