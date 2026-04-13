import pandas as pd
import os

def clean_sales_data():
    print("Starting data cleaning process...")
    
    # 1. Setup dynamic paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_path = os.path.join(script_dir, '..', 'data', 'raw', 'superstore.csv')
    processed_path = os.path.join(script_dir, '..', 'data', 'processed', 'cleaned_data.csv')

    # Ensure the processed directory exists before saving
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)

    # 2. Load the data
    try:
        df = pd.read_csv(raw_path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(raw_path, encoding='windows-1252')

    # 3. Standardize column names (Lowercase and replace spaces/hyphens with underscores)
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')

    # 4. Handle Missing Values & Fix Data Types
    # Drop rows with missing postal codes
    df = df.dropna(subset=['postal_code'])
    
    # Convert postal_code from float to int
    df['postal_code'] = df['postal_code'].astype(int)

    # Convert date columns with explicit handling for Day-Month-Year formats
    df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=True)
    df['ship_date'] = pd.to_datetime(df['ship_date'], format='mixed', dayfirst=True)

    # 5. Save the clean data
    df.to_csv(processed_path, index=False)
    
    print("✅ Data cleaning complete!")
    print(f"Data saved to: {processed_path}")
    print(f"Final Dataset Shape: {df.shape}")

if __name__ == "__main__":
    clean_sales_data()