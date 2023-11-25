from fastapi import FastAPI, HTTPException
from datetime import datetime
from database_service.database import Database
from pdf_generation_service.pdf_generator import PDFGenerator
from email_service.email_service import EmailService

app = FastAPI()

@app.post("/get_transactions")
async def generate_pdf(email: str, start_date: datetime, end_date: datetime):
# async def generate_pdf(filename:str, email: str, start_date: str, end_date: str, pdf_output_filename:str):
    params = {
        'csv_file_path': 'transactions.csv',
        'email': f'{email}',
        'search_by': 'user_email'
    }

    db_instance = Database(params)
    # print("--------------")
    # print(db_instance.extract_transactions(email=email, start_date=start_date, end_date=end_date))
    filtered_transactions = db_instance.extract_transactions(email=email, start_date=start_date, end_date=end_date)

    database_filename = 'data/transactions.csv'
    pdf_output_filename = f'{email}.pdf'
    # db = Database(database_filename, email, start_date, end_date)  # Singleton instance
    # # db = Database(filename, email, start_date, end_date)  # Singleton instance
    # transactions = db.extract_transactions(email, start_date, end_date)

    # pdf_content = PDFGenerator.generate_pdf(transactions)
    # EmailService.send_email(email, pdf_content)
    PDFGenerator(filename=pdf_output_filename, data=filtered_transactions).generate_pdf()
    return {"message": "PDF generation and email sending initiated"}