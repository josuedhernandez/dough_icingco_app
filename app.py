from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<h1>Dough & Icing Co.</h1><p>Welcome to the bakery!</p>"

if __name__ == "__main__":
  app.run(debug=True)

