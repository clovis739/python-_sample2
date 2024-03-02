from flask import Flask , render_template, request

app = Flask(__name__)

registrants = {}

@app.route("/")
def index():

    return render_template("index.html")


# @app.route("/greet",methods=["GET", "POST"])
# def greet():
#     return render_template("greet.html", name = request.args.get("name"))

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    registrants[name] = sport

    return render_template("success.html")

@app.route("/registrants")

if __name__ == "__main__":
    app.run(debug=True)