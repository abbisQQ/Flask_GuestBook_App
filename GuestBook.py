from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/sign')
def sign():
    return render_template("sign.html")


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    return render_template('index.html', name=name, comment=comment)


@app.route("/home", methods=['GET', 'POST'])
def my_home():
    return render_template("example.html", myvar=" estVariable")


if __name__ == "__main__":
    app.run(debug=True)