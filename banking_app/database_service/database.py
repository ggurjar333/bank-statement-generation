import csv
from datetime import datetime

class Database:
    _instance = None
    _transactions = None

    def __new__(cls, csv_file_path, email, start_date, end_date):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            cls._transactions = cls._instance._read_transactions(csv_file_path)
        return cls._instance

    def _read_transactions(self, csv_file_path):
        """
        Read transactions from the CSV file.

        Args:
            csv_file_path (str): Path to the CSV file.

        Returns:
            list: List of all transactions from the CSV file.
        """
        transactions = []
        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.DictReader(file)
                transactions = list(reader)
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

        return transactions

    def get_transactions(self, email, start_date, end_date):
        """
        Retrieve transactions for a specific email within a given date range.

        Args:
            email (str): The email for which transactions are retrieved.
            start_date (str): The start date of the transaction range (format: "DD-MM-YYYY").
            end_date (str): The end date of the transaction range (format: "DD-MM-YYYY").

        Returns:
            list: List of transactions matching the criteria.
        """
        filtered_transactions = []
        # Convert date strings to datetime for comparison
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")

        for row in self._transactions:
            row_date = datetime.strptime(row['date'], "%d-%m-%Y")
            if row['email'] == email and start_date <= row_date <= end_date:
                filtered_transactions.append(row)

        return filtered_transactions

# Import the Database class from the file

# Create an instance of the Database class with file path and query parameters
csv_file_path = 'transactions.csv'
email = "ggurjar333@gmail.com"
start_date = "01-01-2023"
end_date = "10-11-2023"
db = Database(csv_file_path, email, start_date, end_date)

# Call the get_transactions method
transactions = db.get_transactions(email, start_date, end_date)

# Print the transactions
for transaction in transactions:
    print(transaction)
