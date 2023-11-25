import csv
from datetime import datetime
import csv
from typing import List

class Database:
    _instance = None
    _transactions = None

    def __new__(cls, params):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            cls._transactions = cls._instance._read_transactions(params)
            cls._email = params.get('email', '')
            
        return cls._instance

    def _read_transactions(self, params) -> List[dict]:
        transactions = []
        try:
            csv_file_path = params.get('csv_file_path', '')
            search_by = params.get('search_by', '')
            
            with open(csv_file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                
                if search_by not in reader.fieldnames:
                    raise ValueError(f"Error: Column '{search_by}' not found in the CSV file.")
                
                transactions = [row for row in reader if row.get(search_by) == params['email']]                
                if transactions:
                    self._transactions = transactions

        except FileNotFoundError:
            print(f"Error: File not found at {csv_file_path}")
        except csv.Error as e:
            print(f"CSV Error: {e}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print(self._transactions)
        return self._transactions


    def extract_transactions(self, email, start_date, end_date):
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
        
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        for row in self._transactions:
            row_date = datetime.strptime(row['date_of_transaction'], "%Y-%m-%d")
            if row['user_email'] == email and start_date <= row_date <= end_date:
                filtered_transactions.append(row)

        return filtered_transactions

# params = {
#     'csv_file_path': 'transactions.csv',
#     'email': 'ggurjar333@gmail.com',
#     'search_by': 'user_email'
# }

# db_instance = Database(params)
# print("--------------")
# print(db_instance.extract_transactions(email='ggurjar333@gmail.com', start_date='2022-01-01', end_date='2023-12-31'))
