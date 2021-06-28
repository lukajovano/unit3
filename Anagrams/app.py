from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main1.html')


@app.route('/words/<string:word>')
def words(word):
    word= word.upper()
    l=[]
    f = open ('words.txt') 
    words = f.read().splitlines()

    for w in words:
        if sorted(w) == sorted (word):
            w= w.upper()
            l.append(w)
    return render_template('html1.html', words = l)