# api/routes/pdf_generator.py
from fastapi import APIRouter, HTTPException, status
from services.pdf_generation import PDFGenerator

router = APIRouter()

@router.post(
    path="/pdf_generation"
    name = "Transactions: pdf_generator"
)
async def pdf_generator(filename, transactions):
    try:
        generator = PDFGenerator(filename=filename, data=transactions)
        generator.generate_pdf()
        return "PDF generated successfully."
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Exception: {err}")
