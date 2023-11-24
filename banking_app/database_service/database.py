import csv
# from database_service.database import Database

class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            # Initialize database connection or file reading here
        return cls._instance

    def get_transactions(self, email, start_date, end_date):
        transactions = []
        with open('../../data/transactions.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Assuming the CSV file has columns: email, date, amount, description
                if row[0] == email and start_date <= row[1] <= end_date:
                    transactions.append(row)
        return transactions

# Import the Database class from the file

# Create an instance of the Database class
db = Database()

# Call the get_transactions method
email = "ggurjar333@gmail.com"
start_date = "01-01-2023"
end_date = "10-11-2023"
transactions = db.get_transactions(email, start_date, end_date)

# Print the transactions
for transaction in transactions:
    print(transaction)
