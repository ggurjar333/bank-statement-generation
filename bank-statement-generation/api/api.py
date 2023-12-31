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
        'end_date': datetime.strptime(end_date, '%Y-%m-%d').strftime('%Y-%m-%d'),
        'pdf_filename': f'{email}_{start_date}_to_{end_date}.pdf'
    }
    transactions = Database(params=params).extract()
    
    PDFGenerator(filename=params['pdf_filename'], data=transactions).generate_pdf()
    
    EmailService.send_email(email=email, pdf_content=params['pdf_filename'])

    return {
        "message": f"PDF generated and email sending initiated",
        "transactions": transactions
        }