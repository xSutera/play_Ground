from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/play')
def play():
    return render_template("index.html", color="lightblue", times=3)

@app.route('/play/<int:num>')
def play_(num):
    return render_template("index.html",color="lightblue",times=num)

@app.route('/play/<int:num>/<string:colour>')
def play__(num,colour):
    return render_template("index.html",color=colour,times=num)


if __name__ =="__main__":
        app.run(debug=True)