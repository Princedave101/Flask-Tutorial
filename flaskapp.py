from flask import Flask

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/contact")
def contactPage():
    return "u can contact us at fuck u by ur self"

if __name__ == "__main__":
    app.run(debug=True)