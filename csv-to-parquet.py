# pip install pandas
# pip install pyarrow
import os
import pandas as pd

# Directories
input_dir = 'input'
output_dir = 'output'
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
            df = pd.read_csv(csv_path, encoding='utf-8', sep=';') 
            # encoding='Latin1',
            # sep='\t'
            # names=['col1', 'col2', 'colN']
            # header=None
            # decimal=','
            
            # Define the output path for the Parquet file
            parquet_path = os.path.join(output_dir, filename.replace(extension, '.parquet'))
            
            # Save the DataFrame as a Parquet file
            df.to_parquet(parquet_path)
        except Exception as e:
            print(f"Error processing file {csv_path}: {e}")

print("Conversion completed!")