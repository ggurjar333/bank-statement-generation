import csv
from datetime import datetime
import csv
from typing import List

class Database:
    def __init__(self, params) -> None:
        self.params = params

    def extract(self) -> List[dict]:
        transactions = []
        filtered_transactions = []
        try:
            csv_file_path = self.params.get('csv_file_path', '')
            search_by = self.params.get('search_by', '')

            with open(csv_file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                
                if search_by not in reader.fieldnames:
                    raise ValueError(f"Error: Column '{search_by}' not found in the CSV file.")
                
                transactions = [row for row in reader if row.get(search_by) == self.params['email']]     
                start_date = datetime.strptime(self.params['start_date'], "%Y-%m-%d")
                print("start_date: ", start_date)
                print("end_date:", end_date)
                end_date = datetime.strptime(self.params['end_date'], "%Y-%m-%d")

                for row in transactions:
                    row_date = datetime.strptime(row['date_of_transaction'], "%Y-%m-%d")
                    if start_date <= row_date <= end_date:
                        filtered_transactions.append(row)

        except FileNotFoundError:
            print(f"Error: File not found at {csv_file_path}")
        except csv.Error as e:
            print(f"CSV Error: {e}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return filtered_transactions

# params = {
#     'csv_file_path': 'transactions.csv',
#     'email': 'ggurjar333@gmail.com',
#     'search_by': 'user_email',
#     'start_date': '2022-01-01',
#     'end_date': '2023-11-23'
# }
# load_db = Database(params=params)
# transactions = load_db.extract()
# print("Extd Transactions: ", transactions)

