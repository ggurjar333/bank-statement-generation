from fastapi import FastAPI, HTTPException
from datetime import datetime
from database_service.database import Database
from pdf_generation_service.pdf_generator import PDFGenerator
from email_service.email_service import EmailService

app = FastAPI()

@app.post("/get_transactions")
async def generate_pdf(email: str, start_date: str, end_date: str):
    params = {
        'csv_file_path': 'transactions.csv',
        'email': email,
        'search_by': 'user_email',
        'start_date': datetime.strptime(start_date, '%Y-%m-%d').strftime('%Y-%m-%d'),
        'end_date': datetime.strptime(end_date, '%Y-%m-%d').strftime('%Y-%m-%d')
    }
    db = Database(params=params)
    transactions = db.extract()
    processed_data = db.preprocess(data=transactions)

    pdf_output_filename = f'{email}_{start_date}_to_{end_date}.pdf'
    PDFGenerator(filename=pdf_output_filename, data=processed_data).generate_pdf()
    # EmailService.send_email(email, pdf_content)

    # PDFGenerator(filename=pdf_output_filename, data=filtered_transactions).generate_pdf()
    return {
        "message": f"PDF generated {pdf_output_filename} and email sending initiated",
        "transactions": transactions
        }