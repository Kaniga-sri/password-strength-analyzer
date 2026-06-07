from flask import Flask, render_template, request
from core import check_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":
        password = request.form["password"]
        result = check_password(password)

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)