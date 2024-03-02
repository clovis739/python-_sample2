from flask import Flask , render_template, request

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("success.html")


# @app.route("/greet",methods=["GET", "POST"])
# def greet():
#     return render_template("greet.html", name = request.args.get("name"))

# @app.register("/register", methods=["POST", "GET"])
# def register():
#     return render_template("success.html")

 