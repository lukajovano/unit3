from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Bad Morning"
    
    text = """It is early in the morning and you sleapt realy badly! Your Jack Russell Terrier wakes you up and wants to play"""
    image2 = "get up"
    choices = [
        ('get_up',"Go get up and make coffee"),
        ('go back to sleep',"You tell your dog to shut up and go back to sleep")
    ]
    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/get up")
def get_coffee():
    title = "You make yourself a cup of coffee and just when to start to drink it..."
    
    text = """when your phone starts ringing and you pour all the coffee on your pants jelling your lungs of you ansver the call. It's the bank new executive order has abolished all the student debt and want to inform you"""

    choices = [
        ('go_change',"Change pants and start the party early"),
        ('shower',"Good hot bath is all the party you need")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/shower")
def interview():
    end = "shower"
    title = "You put on hot tap and start showering"
    
    text = """You sing happy that you don't need to worry about all those student loans!!!"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, end = end)



@app.route("/go_change")
def home_change():
    end = "drink"
    title = "As you are changing..."
    
    text = """You remember a bottle of scotch whisky you bought a long time ago you open it up and start the party alone!"""
    
    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, end = end)