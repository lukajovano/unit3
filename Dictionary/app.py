from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('intro.html')
    
@app.route("/dictionary")
def dictionary():
    look=""
    l=[]
    k=65
    while k<=90:
        l.append(look+chr(k))
        k=k+1

    return render_template('hello.html', l= l, look = look)
@app.route("/dictionary/<string:look>")
def words(look):
    n=len(look)
    f = open ('words.txt') 
    real= False
    words = f.read().splitlines()
    l=[]
    t=0
    for i in words:
        if i[0: n] == look:
            t=t+1
            if (len(i)==len(look)):
                real=True

    k=65  
    while k<=90:
        l.append(look+chr(k))
        k=k+1
    return render_template('main.html', l=l, look = look, t=t, real=real)