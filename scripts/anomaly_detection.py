import pandas as pd
import os
from sklearn.ensemble import IsolationForest

def detect_anomalies():
    print("Starting AI Anomaly Detection...")
    
    # 1. Setup paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, '..', 'data', 'processed', 'cleaned_data.csv')
    output_dir = os.path.join(script_dir, '..', 'outputs')
    output_path = os.path.join(output_dir, 'anomaly_results.csv')

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # 2. Load the cleaned data
    df = pd.read_csv(input_path)

    # 3. AI Model Setup
    # Since the dataset only has Sales, we look for abnormally high or low sales amounts
    features = ['sales']
    
    # contamination=0.02 flags the top 2% most extreme/unusual rows
    model = IsolationForest(contamination=0.02, random_state=42)

    # 4. Train the model and get predictions
    # It returns 1 for normal rows, and -1 for anomalies
    df['anomaly_flag'] = model.fit_predict(df[features])

    # 5. Filter out just the anomalies
    anomalies_df = df[df['anomaly_flag'] == -1].copy()
    
    # Save the anomalies to your outputs folder
    anomalies_df.to_csv(output_path, index=False)

    print("✅ Anomaly Detection complete!")
    print(f"Total transactions analyzed: {len(df)}")
    print(f"Suspicious transactions found: {len(anomalies_df)}")
    print(f"Results saved to: {output_path}")

if __name__ == "__main__":
    detect_anomalies()