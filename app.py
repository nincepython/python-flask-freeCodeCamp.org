from flask import Flask, render_template

app = Flask(__name__)


# WHEN A CERTAIN URL IS REQUESTED
# PATH OF URL, AFTER THE DOMAIN
# 
@app.route("/")
def hello_world():
  #return print("CKEMI USTA")
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
