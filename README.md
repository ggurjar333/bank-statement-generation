
# Bank statement genration

This Python-based banking application allows users to request the generation of a PDF file showcasing their transactions within a specified date range.



- [Python](https://www.python.org/): The core programming language driving this application, known for its readability and versatility.
- [FastAPI](https://fastapi.tiangolo.com/): A high-performance web framework with automatic documentation and type safety, making it ideal for API development.
- [Reportlab](https://docs.reportlab.com/): A powerful library for PDF generation.

## Installation

Make sure you have Python 3.10 installed and have extracted the zip of this project. Install the required libraries using:
```bash
pip install -r requirements.txt
```
## In terminal, You can use the following command to run this project
```bash
bash ./run.sh
```

# Notes
``transactions.csv`` is located inside the root directory. It is used here as data source for this project.
You can test the APIs over [here](http://127.0.0.1:8000/docs)
## Authentication and Authorization

To enhance the security of this banking application. FastAPI provides
[OAuth2PasswordBearer](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) for token-based authentication. Users need to obtain a token by providing their username and password.
