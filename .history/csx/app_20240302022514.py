from flask import Flask , render_template, request

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")


# @app.route("/greet",methods=["GET", "POST"])
# def greet():
#     return render_template("greet.html", name = request.args.get("name"))

@app.register("/register", meth)