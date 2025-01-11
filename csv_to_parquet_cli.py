import os
import pandas as pd
import argparse

def convert_files(input_dir, output_dir, extension='.csv', encoding='utf-8', sep=';', header=0):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(extension):
            csv_path = os.path.join(input_dir, filename)
            try:
                df = pd.read_csv(csv_path, encoding=encoding, sep=sep, header=header, low_memory=False)
                parquet_path = os.path.join(output_dir, filename.replace(extension, '.parquet'))
                df.to_parquet(parquet_path)
                print(f"Processed file {csv_path}")
            except Exception as e:
                print(f"Error processing file {csv_path}: {e}")

    print("Conversion completed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV files to Parquet format.")

    parser.add_argument("--input", "-i", required=True, help="Input directory with CSV files")
    parser.add_argument("--output", "-o", required=True, help="Output directory for Parquet files")
    parser.add_argument("--extension", "-e", default=".csv", help="File extension to filter (default: .csv)")
    parser.add_argument("--encoding", "-enc", default="utf-8", help="File encoding (default: utf-8)")
    parser.add_argument("--separator", "-s", default=";", help="CSV separator (default: ;)")
    parser.add_argument("--header", "-hd", default=0, type=int, help="Header row (default: 0)")

    args = parser.parse_args()

    convert_files(
        input_dir=args.input,
        output_dir=args.output,
        extension=args.extension,
        encoding=args.encoding,
        sep=args.separator,
        header=args.header
    )
