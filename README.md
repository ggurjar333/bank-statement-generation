
# Bank statement genration

This Python-based banking application allows users to request the generation of a PDF file showcasing their transactions within a specified date range.



- [Python](https://www.python.org/): The core programming language driving this application, known for its readability and versatility.
- [FastAPI](https://fastapi.tiangolo.com/): A high-performance web framework with automatic documentation and type safety, making it ideal for API development.
- [Reportlab](https://docs.reportlab.com/): A powerful library for PDF generation.

## Installation

Make sure you have Python 3.10 installed. Install the required libraries using:

```bash
pip install -r requirements.txt
bash ./run.sh
```


## Preview


## Authentication and Authorization

To enhance the security of this banking application. We can use
[OAuth2PasswordBearer](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) for token-based authentication. Users need to obtain a token by providing their username and password.