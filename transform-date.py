import os
import pandas as pd

# Directories
input_dir = 'input'
output_dir = 'output'

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
            
            # Check if 'OrderDate' column exists
            if 'OrderDate' in df.columns:
                # Convert the 'OrderDate' column to the new format
                df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
                
                # Define the output path for the modified CSV file
                output_csv_path = os.path.join(output_dir, filename)
                
                # Save the modified DataFrame as a CSV file
                df.to_csv(output_csv_path, index=False, sep=';')
                
                print(f"Processed file {csv_path}")
            else:
                print(f"'OrderDate' column not found in {csv_path}")
        except Exception as e:
            print(f"Error processing file {csv_path}: {e}")

print("Processing completed!")