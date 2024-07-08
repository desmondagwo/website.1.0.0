from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.secret_key   = 'desmondclave'




Jobs = [
    {
    'id' : 1,
    'title' : 'splunk admin',
    'salary': '$90/hr',
    'location': 'NC, USA'
    },
    {
    'id' : 2,
    'title' : 'splunk developer',
    'salary': '$60/hr',
    'location': 'NJ, USA'
    },
    {
    'id' : 2,
    'title' : 'devops',
    'salary': '$60/hr',
    'location': 'NJ, USA'
    },
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup', methods=["POST" , "GET"])
def signup():
    return render_template("signup.html")

@app.route('/profile')
def profile():
    return render_template("profile.html", jobs=Jobs)

@app.route('/api/jobs')
def jobs():
    return jsonify(Jobs)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)


