from flask import Blueprint, render_template, request
from app.entities.quotation import QuotationRequest
from app.models.quotation import QuotationModel
from app.database.database import get_db
from sqlalchemy.orm import Session

bp = Blueprint('contact', __name__, url_prefix='/contact-us')

@bp.route('/', methods=["GET"])
def index():
    return render_template('contact_us.html')

@bp.route('/', methods=["POST"])
def process_data():
    # Get the form data
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    description = request.form["description"]
    location = request.form["location"]
    event_date = request.form["event_date"]
    event_time = request.form["event_time"]
    service_duration = int(request.form["service_duration"])
    guests_adults = int(request.form["guests_adult"])
    guests_teens = int(request.form["guests_teens"])

    quotation_data = QuotationRequest(name, description, phone, email,
            guests_teens, guests_adults, location,
            event_date, event_time, service_duration)

    db: Session = get_db()
    quotation_model = QuotationModel(db)
    new_quotation = quotation_model.create_quotation_request(quotation_data)

    return render_template('contact_us_message.html')