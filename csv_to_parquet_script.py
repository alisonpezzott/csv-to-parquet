# pip install pandas
# pip install pyarrow

import os
import pyarrow as pa
import pandas as pd

# Directories
input_dir = 'sample_dataset_csv'
output_dir = 'sample_dataset_parquet'
extension = '.csv'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(extension):
        # Full path of the CSV file
        csv_path = os.path.join(input_dir, filename)
        
        try:
            # Read the CSV file
            df = pd.read_csv(csv_path, encoding='utf-8', sep=';', header=0, low_memory=False) 
            # encoding='Latin1', 'utf-8', 'cp1252', 'ascii', 'utf-16', 'utf-32'
            # sep='\t', ';', ',', '|', ' '
            # names=['col1', 'col2', 'colN']
            # header=None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
            # decimal=',', '.'
            # thousands='.'. ','
            # Define the output path for the Parquet file
            parquet_path = os.path.join(output_dir, filename.replace(extension, '.parquet'))
            
            # Save the DataFrame as a Parquet file
            df.to_parquet(parquet_path)
        except Exception as e:
            print(f"Error processing file {csv_path}: {e}")

print("Conversion completed!")