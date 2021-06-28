from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/fizzbuzz/<int:n>')
def fizzbuzz(n):
    l=[]
    i=1
    while (i<=n):
        if (i%3==0) and (i%5==0):
           l.append("FizzBuzz") 
        elif (i%3==0):
            l.append("Fizz")
        elif (i%5==0):
            l.append("Buzz")
        else:
            l.append(str(i))
        
        i=i+1
    return render_template('html.html', numbers = l)