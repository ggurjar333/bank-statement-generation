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
                data = [{"date_of_transaction": entry["date_of_transaction"], "amount": entry["amount"]} for entry in filtered_records]
                print(data)
                        
        except FileNotFoundError:
            print(f"Error: File not found at {csv_file_path}")
        except csv.Error as e:
            print(f"CSV Error: {e}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return data
    
    def preprocess(self, data):
        self.data = data
        if not self.data:
            return []
        # Extract headers from the first dictionary
        headers = tuple(self.data[0].keys())
        # Extract values from each dictionary
        values = [tuple(entry.values()) for entry in self.data]
        # Preprocessed data for PDF
        preprocessed_data = [headers] + values
        return preprocessed_data    