from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template( "index.html", header = "Dough & Icing Co.", content = "Welcome to the bakery!")

@app.route("/about")
def about():
  return render_template( "about.html", header = "About Us", content = "We are a family-owned bakery specializing in delicious custom sugar cookies and beautiful sourghdough bread.")

if __name__ == "__main__":
  app.run(debug=True)

