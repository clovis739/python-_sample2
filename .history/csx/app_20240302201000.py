from flask import Flask , render_template, request

app = Flask(__name__)

REGISTRANTS = {}
SPORT = {
    "Basketball",
    "Football",
    ""
}

@app.route("/")
def index():

    return render_template("index.html")


# @app.route("/greet",methods=["GET", "POST"])
# def greet():
#     return render_template("greet.html", name = request.args.get("name"))

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sports = request.form.get("sports")
    REGISTRANTS[name] = sports

    return render_template("success.html")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)

if __name__ == "__main__":
    app.run(debug=True)