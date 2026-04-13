import pandas as pd
import sqlite3
import os

def load_to_database():
    print("Starting Database Loading Phase...")
    
    # 1. Setup paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cleaned_path = os.path.join(script_dir, '..', 'data', 'processed', 'cleaned_data.csv')
    anomaly_path = os.path.join(script_dir, '..', 'outputs', 'anomaly_results.csv')
    db_path = os.path.join(script_dir, '..', 'data', 'processed', 'sales_database.db')

    # 2. Load the CSVs into Pandas
    df_clean = pd.read_csv(cleaned_path)
    df_anomalies = pd.read_csv(anomaly_path)

    # 3. Connect to SQLite (This creates the .db file automatically)
    conn = sqlite3.connect(db_path)

    # 4. Push data to SQL tables
    print("Pushing data to SQL tables...")
    df_clean.to_sql('sales_data', conn, if_exists='replace', index=False)
    df_anomalies.to_sql('anomalies', conn, if_exists='replace', index=False)

    # 5. Quick verification test using a real SQL query
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM sales_data")
    total_rows = cursor.fetchone()

    cursor.execute("SELECT COUNT(*) FROM anomalies")
    total_anomalies = cursor.fetchone()

    print("✅ Data successfully loaded into SQL database!")
    print(f"Database created at: {db_path}")
    print(f"Verified SQL Table 'sales_data' rows: {total_rows}")
    print(f"Verified SQL Table 'anomalies' rows: {total_anomalies}")
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    load_to_database()