class QuotationRequest:
    def __init__(self, name: str, description: str, phone: str, email: str,
                 guests_teens: int, guests_adults: int, location: str,
                 event_date: str, event_time: str, service_duration: int, id: int = None):
        self.id = id
        self.name = name
        self.description = description
        self.phone = phone
        self.email = email
        self.guests_teens = guests_teens
        self.guests_adults = guests_adults
        self.location = location
        self.event_date = event_date
        self.event_time = event_time
        self.service_duration = service_duration

    def __repr__(self):
        return f"<QuotationRequest(id={self.id}, name='{self.email}')>"
