from flask import Flask
import urllib.request

app = Flask(__name__)

@app.route("/")
def is_it_raining_in_seattle():
    with urllib.request.urlopen('http://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()
    if is_it_raining_in_seattle == "true":
        return "True"
    else:
        return "False"

if __name__ == '__main__':
        app.run(debug=True)
