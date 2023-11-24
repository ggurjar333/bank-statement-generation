class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            # Initialize database connection or file reading here
        return cls._instance

    def get_transactions(self, email, start_date, end_date):
        # Logic to read and filter transactions from CSV
        pass
