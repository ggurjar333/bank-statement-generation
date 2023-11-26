import csv
from datetime import datetime
import csv
from typing import List

class Database:
    def __init__(self, params) -> None:
        self.params = params

    def extract(self) -> List[dict]:
        filtered_transactions = []
        try:
            csv_file_path = self.params.get('csv_file_path', '')
            search_by = self.params.get('search_by', '')

            with open(csv_file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                
                if search_by not in reader.fieldnames:
                    raise ValueError(f"Error: Column '{search_by}' not found in the CSV file.")
                
                transactions = [row for row in reader if row.get(search_by) == self.params['email']]
                # print(transactions)
                for row in transactions:
                    row_date = datetime.strptime(row['date_of_transaction'], "%Y-%m-%d").strftime('%Y-%m-%dT%H:%M:%S')
                    # if self.params.get('start_date') <= row_date <= self.params.get('end_date'):
                    #     filtered_transactions.append(row)
                    filtered_row = list(filter(
                                lambda row: self.params.get('start_date', '') <= datetime.strptime(row['date_of_transaction'], "%Y-%m-%d").strftime('%Y-%m-%dT%H:%M:%S') <= self.params.get('end_date', ''), transactions
                                )
                            )
                    print(filtered_row)
                    filtered_transactions.append(filtered_row)
                        
        except FileNotFoundError:
            print(f"Error: File not found at {csv_file_path}")
        except csv.Error as e:
            print(f"CSV Error: {e}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return filtered_transactions

params = {
    'csv_file_path': 'transactions.csv',
    'email': 'ggurjar333@gmail.com',
    'search_by': 'user_email',
    'start_date': datetime.strptime(f"{'2022-01-01'}", '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S'),
    'end_date': datetime.strptime(f"{'2023-12-31'}", '%Y-%m-%d').replace(hour=23, minute=59, second=59).strftime('%Y-%m-%dT%H:%M:%S')
}
print(params)
# params = {
#     'csv_file_path': 'transactions.csv',
#     'email': 'ggurjar333@gmail.com',
#     'search_by': 'user_email',
#     'start_date': '2022-01-01T00:00:00',
#     'end_date': '2023-12-31T23:59:59'
# }
# print(params)
load_db = Database(params=params)
# print(load_db.extract())
transactions = load_db.extract()
print("Extd Transactions: ", transactions)

