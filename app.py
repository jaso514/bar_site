from flask import Flask, render_template, send_from_directory
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    current_year = datetime.now().year
    return render_template("index.html", current_year=current_year)

@app.route("/test")
def about():
    return render_template("test.html")

@app.route('/menu')
def menu():
    return send_from_directory('static/files', 'menu_2024_diciembre.pdf')

if __name__ == "__main__":
    app.run(debug=True)
