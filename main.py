from flask import Flask, redirect, url_for, request, render_template, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return render_template("welcome.html", name=user)
    else:
        user = request.args.get('nm')
        return render_template("welcome.html", name=user)


@app.route('/inputscore')
def inputscore():
    return render_template("inputscore.html")


@app.route('/res')
def result():
    return render_template("result.html", score=50)


@app.route('/user/<user>')
def hello(user):
    return render_template("welcome.html", name=user)

@app.route("/entermark")
def entermarks():
    return render_template("entermark.html")

@app.route("/subs", methods=['POST', 'GET'])
def marks():
    if request.method == 'POST':
        phy = request.form['phy']
        che = request.form['che']
        math = request.form['math']
    else:
        phy = request.args.get('phy')
        che = request.args.get('che')
        math = request.args.get('math')

    dic = dict(physics=phy, checmistry=che, mathematics=math)
    return render_template("mark.html", sub=dic)


if __name__ == "__main__":
    app.run(debug=True)
