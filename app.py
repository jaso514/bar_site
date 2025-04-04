from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.jinja_env.cache = None

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

@app.route("/")
def index():
    current_year = datetime.now().year
    return render_template("index.html", current_year=current_year)

@app.route("/contact-us", methods=["GET"])
def contact_us():
    return render_template("contact_us.html")

@app.route("/contact", methods=["POST"])
def contact():
    if request.method == "POST":
        # Get the form data
        nombre = request.form["name"]
        telefono = request.form["phone"]
        description = request.form["description"]
        location = request.form["location"]
        event_date = request.form["event_date"]
        event_time = request.form["event_time"]
        service_duration = request.form["service_duration"]
        guests_adult = request.form["guests_adult"]
        guests_teens = request.form["guests_teens"]

        # Store the data in variables (for now)
        print("Form data:")
        print("Nombre:", nombre)
        print("Teléfono:", telefono)
        print("Descripción del Evento:", description)
        print("Ubicación:", location)
        print("Fecha del Evento:", event_date)
        print("Hora de inicio:", event_time)
        print("Duración del Servicio:", service_duration)
        print("Cantidad de Adultos:", guests_adult)
        print("Cantidad de Adolescentes:", guests_teens)

    return redirect(url_for("contact_us"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
