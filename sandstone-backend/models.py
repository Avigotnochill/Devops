from sqlalchemy import Column, Integer, String
from database import Base

class Enquiry(Base):
    __tablename__ = "enquiries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    country = Column(String)
    contact_number = Column(String)
