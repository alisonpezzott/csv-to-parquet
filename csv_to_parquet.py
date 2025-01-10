import os
import pandas as pd

# Directories
input_dir = 'csv'
output_dir = 'parquet'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        # Full path of the CSV file
        csv_path = os.path.join(input_dir, filename)
        
        try:
            # Read the CSV file
            df = pd.read_csv(csv_path, encoding='utf-8', sep=';')
            
            # Define the output path for the Parquet file
            parquet_path = os.path.join(output_dir, filename.replace('.csv', '.parquet'))
            
            # Save the DataFrame as a Parquet file
            df.to_parquet(parquet_path)
        except Exception as e:
            print(f"Error processing file {csv_path}: {e}")

print("Conversion completed!")