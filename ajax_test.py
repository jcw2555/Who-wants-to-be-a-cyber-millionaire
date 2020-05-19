from flask import Flask, jsonify, request, render_template, redirect, abort
from export import export_questions as export
app = Flask(__name__, template_folder="/var/www/html/", static_folder="/var/www/html/")

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/json/millionaire.json')
#def pleasedont():
#    abort(403)

@app.route('/level1')
def level1():
    #print("exporting...")
    # attempt to export from mysql to json
    export('1')
    # temp output
    return render_template('game.html')

@app.route('/level2')
def level2():
    #print("exporting...")
    # attempt to export from mysql to json
    export('2')
    # temp output
    return render_template('game.html')

@app.route('/level3')
def level3():
    #print("exporting...")
    # attempt to export from mysql to json
    export('3')
    # temp output
    return render_template('game.html')

@app.route('/level4')
def level4():
    #print("exporting...")
    # attempt to export from mysql to json
    export('4')
    # temp output
    return render_template('game.html')

@app.after_request
def add_header(r):
    """
    trying to disable caching to fix game json not updating in browser
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    r.headers['X-Frame-Options'] = 'SAMEORIGIN'
    r.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return r

#@app.before_request
#def before_request():
    #if not request.is_secure:
        #url = request.url.replace('http://', 'https://', 1)
        
        #code = 301
        #return redirect('https://wwtbacm.csec.rit.edu', code=code)

if __name__=='__main__':
    app.run(debug=True)
