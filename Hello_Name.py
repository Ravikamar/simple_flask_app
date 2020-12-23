from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route("/success/<name>")
def success(name):
    return f"welcome our {name}"


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
@app.route('/')
def index():
    return f"<html><body><h2>'Hello world '</h2></body></html>"

@app.route('/user/<user>')
def hello(user):
    return render_template("home.html",name=user)

@app.route("/result/<int:marks>")
def result(marks):
    return render_template("result.html",mark=marks)

@app.route("/subs")
def marks():
    dic = dict(physics=40, checmistry=50, mathematics=89)
    return render_template("mark.html",sub=dic)
if __name__ == "__main__":
    app.run(debug=True)
