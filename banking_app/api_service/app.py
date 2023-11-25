from fastapi import FastAPI, HTTPException
from datetime import datetime
from banking_app.database_service.database import Database
from banking_app.pdf_generation_service.pdf_generator import PDFGenerator
from banking_app.email_service.email_service import EmailService

from
app = FastAPI()
db = Database()  # Singleton instance

@app.post("/generate_pdf")
async def generate_pdf(email: str, start_date: datetime, end_date: datetime):
    transactions = db.get_transactions(email, start_date, end_date)
    pdf_content = PDFGenerator.generate_pdf(transactions)
    EmailService.send_email(email, pdf_content)
    return {"message": "PDF generation and email sending initiated"}