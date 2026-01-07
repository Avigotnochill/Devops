from pydantic import BaseModel

class EnquiryCreate(BaseModel):
    name: str
    email: str
    country: str
    contact_number: str
