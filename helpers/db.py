import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=ACCOUNT_SampleTest;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return conn