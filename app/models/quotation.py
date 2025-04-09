from app.database.models import MobileBarRequest
from app.entities.quotation import QuotationRequest
from app.database.database import SessionLocal
from sqlalchemy.orm import Session

class QuotationModel:
    def __init__(self, db: Session = None):
        self.db = db or SessionLocal()

    def create_quotation_request(self, quotation_data: QuotationRequest) -> MobileBarRequest:
        db_quotation = MobileBarRequest(
            name=quotation_data.name,
            description=quotation_data.description,
            phone=quotation_data.phone,
            email=quotation_data.email,
            guests_teens=quotation_data.guests_teens,
            guests_adults=quotation_data.guests_adults,
            location=quotation_data.location,
            event_date=quotation_data.event_date,
            event_time=quotation_data.event_time,
            service_duration=quotation_data.service_duration
        )
        self.db.add(db_quotation)
        self.db.commit()
        self.db.refresh(db_quotation)
        return db_quotation

    # Puedes agregar más métodos para leer, actualizar o eliminar cotizaciones