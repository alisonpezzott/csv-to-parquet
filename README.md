<!-- filepath: /path/to/README.md -->
<link rel="stylesheet" type="text/css" href="custom.css">

## CSV to Parquet Script

### Comparision beetwen file formats

|<h5 align="center">File Formats</h5>|<h5 align="center">Size</h5>|<h5 align="center">Reduction</h5>|
|:------|-------:|-------:|
| csv    | 138.0 MB | |
| csv (zipped) | 22.0 MB | -84.0% |
| parquet | 20.4 MB | -85.2% |



```bash
csv_to_parquet_cli.exe -i "C:\Caminho\CSV" -o "C:\Caminho\Parquet" -e ".csv" -enc "utf-8" -s ";" -hd 0
```
Options
-i "C:\Users\aliso\OneDrive\Documentos\GitHub\csv-to-parquet\input" -o "C:\Users\aliso\OneDrive\Documentos\GitHub\csv-to-parquet\output" -e ".csv" -enc "utf-8" -s ";" -hd 0

