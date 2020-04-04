from flask import Flask, jsonify, request, render_template, redirect
from export import export_questions as export
app = Flask(__name__, template_folder="/home/student/Documents/capstone/", static_folder="/home/student/Documents/capstone/")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/level1')
def level1():
    #print("exporting...")
    # attempt to export from mysql to json
    export('1')
    # temp output
    return redirect('http://127.0.0.1:5000', code=302)

@app.route('/level2')
def level2():
    #print("exporting...")
    # attempt to export from mysql to json
    export('2')
    # temp output
    return "level 2 exported"

@app.route('/level3')
def level3():
    #print("exporting...")
    # attempt to export from mysql to json
    export('3')
    # temp output
    return "level 3 exported"

@app.route('/level4')
def level4():
    #print("exporting...")
    # attempt to export from mysql to json
    export('4')
    # temp output
    return "level 4 exported"

if __name__=='__main__':
    app.run(debug=True)