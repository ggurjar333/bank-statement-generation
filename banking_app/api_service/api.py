from fastapi import FastAPI, HTTPException
from datetime import datetime

from database_service.database import Database
from pdf_generation_service.pdf_generator import PDFGenerator
from email_service.email_service import EmailService

app = FastAPI()

@app.post("/generate_pdf")
async def generate_pdf(filename:str, email: str, start_date: datetime, end_date: datetime):
    db = Database(filename, email, start_date, end_date)  # Singleton instance
    transactions = db.get_transactions(email, start_date, end_date)
    # pdf_content = PDFGenerator.generate_pdf(transactions)
    # EmailService.send_email(email, pdf_content)
    PDFGenerator.generate_pdf(transactions)
    return {"message": "PDF generation and email sending initiated"}