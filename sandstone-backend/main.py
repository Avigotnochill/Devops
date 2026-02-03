from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import Enquiry
from schemas import EnquiryCreate
from database import init_db

@app.on_event("startup")
def startup():
    init_db()

app = FastAPI()
#Cors fix
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for local testing)
    allow_credentials=True,
    allow_methods=["*"],  # Allow POST, GET, OPTIONS, DELETE, etc.
    allow_headers=["*"],
)

# Create tables automatically
Base.metadata.create_all(bind=engine)

# Dependency: get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Backend is running!"}

@app.post("/enquiry")
def create_enquiry(data: EnquiryCreate, db: Session = Depends(get_db)):
    enquiry = Enquiry(
        name=data.name,
        email=data.email,
        country=data.country,
        contact_number=data.contact_number
    )
    db.add(enquiry)
    db.commit()
    db.refresh(enquiry)
    return {"success": True, "message": "Enquiry saved!"}
