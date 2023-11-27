import csv
from datetime import datetime
import csv
from typing import List

class Database:
    def __init__(self, params) -> None:
        self.params = params
    
    def extract(self) -> List[dict]:
        
        try:
            csv_file_path = self.params.get('csv_file_path', '')
            search_by = self.params.get('search_by', '')
            start_date = self.params.get('start_date', '')
            end_date = self.params.get('end_date', '')

            with open(csv_file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                
                if search_by not in reader.fieldnames:
                    raise ValueError(f"Error: Column '{search_by}' not found in the CSV file.")
                
                transactions = [row for row in reader if row.get(search_by) == self.params['email']]      
                filtered_records = list(filter(
                                lambda row: start_date <= row['date_of_transaction'] <= end_date, transactions
                            )
                    )
                filtered_records = [{"date_of_transaction": entry["date_of_transaction"], "amount": entry["amount"]} for entry in filtered_records]
                        
        except FileNotFoundError:
            print(f"Error: File not found at {csv_file_path}")
        except csv.Error as e:
            print(f"CSV Error: {e}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return filtered_records