from fastapi import FastAPI, Depends, HTTPException
from datetime import datetime
from database_service.database import Database
from pdf_generation_service.pdf_generator import PDFGenerator
from email_service.email_service import EmailService

def get_database(csv_file_path: str, email: str = Depends(lambda: "ggurjar333@gmail.com")):
    return Database(csv_file_path, email)


app = FastAPI()


@app.post("/get_transactions")
async def generate_pdf(email: str, start_date: str, end_date: str):
# async def generate_pdf(email: str, start_date: datetime, end_date: datetime):
    # params = {
    #     'csv_file_path': 'transactions.csv',
    #     'email': f'{email}',
    #     'search_by': 'user_email'
    # }
    params = {
    'csv_file_path': 'transactions.csv',
    'email': f'{email}',
    'search_by': 'user_email',
    'start_date': datetime.strptime(f'{start_date}', "%Y-%m-%d"),
    'end_date': datetime.strptime(f'{end_date}', "%Y-%m-%d")
    }

    load_db = Database(params=params)
    transactions = load_db.extract()
    return transactions
    # print("Extd Transactions: ", transactions)

    # db_instance = Database(params)
    # print(db_instance.extract_transactions(email=email, start_date=start_date, end_date=end_date))
    # filtered_transactions = db_instance.extract_transactions(email=email, start_date=start_date, end_date=end_date)
    # return filtered_transactions

    # pdf_output_filename = f'{email}.pdf'
    # pdf_content = PDFGenerator.generate_pdf(transactions)
    # EmailService.send_email(email, pdf_content)

    # PDFGenerator(filename=pdf_output_filename, data=filtered_transactions).generate_pdf()
    # return {"message": "PDF generation and email sending initiated"}
