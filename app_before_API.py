from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': "Data Analist",
        'location': "AMSTERDAM_CODECAMP",
        'salary': "500$"
    },
    {
        'id': 2,
        'title': "python gui",
        'location': "BERLIN",
        'salary': "700$"
    },
    {
        'id': 3,
        'title': "USTA KEPUCESH",
        'location': "REMOTE",
        'salary': "687$"
    },
]


# WHEN A CERTAIN URL IS REQUESTED
# PATH OF URL, AFTER THE DOMAIN
#
@app.route("/")
def hello_world():
  #return print("CKEMI USTA")
  return render_template('home.html', jobs=JOBS, company_name="GrupiRushupi")


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
