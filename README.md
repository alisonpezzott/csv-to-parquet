<!-- filepath: /path/to/README.md -->
<link rel="stylesheet" type="text/css" href="custom.css">

## CSV to Parquet Script

In this repository, I provide apps and scripts for converting CSV files to Parquet using Python.
See the modes below and use the one that is suitable for your application.

### Video on Youtube

Watch the YouTube video demonstration of this case here: soon

### Article on Linkedin

[Aumentando a performance convertendo arquivos CSV por Parquet no Power BI]()

### Modes

#### APP

![app_interface](assets\app_interface.png)

An .exe application that does not require installation, just download, configure the parameters, and run.

#### CLI
An .EXE file that can be executed via command prompt and, best of all, can be configured in Windows scheduled tasks.

##### Windows Schedule Tasks

Configure in Actions the full path of the executable file, for example:  
`C:\Users\aliso\OneDrive\Documentos\GitHub\csv-to-parquet\exe\csv_to_parquet_cli.exe`

You can use options as:  
`-i "C:\Users\aliso\OneDrive\Documentos\GitHub\csv-to-parquet\input" -o "C:\Users\aliso\OneDrive\Documentos\GitHub\csv-to-parquet\output" -e ".csv" -enc "utf-8" -s ";" -hd 0`

##### Run manually

You can run on powershell or configure a .bat file to run manually too  

```bash
cd C:\Users\aliso\OneDrive\Documentos\GitHub\csv-to-parquet\exe\
csv_to_parquet_cli.exe -i "C:\InputPath" -o "C:\OutputPath" -e ".csv" -enc "utf-8" -s ";" -hd 0
```

#### Script Python

Unlike the compiled versions above, this is a Python script that can be run in VSCode, Python interpreters, Notebooks, etc. You choose. Completely open, it gives you the freedom to create new implementations and other automations.

### Releases

|Version|Updated|Link|Release Note|
|---|---|---|:--|
|v1.0.0|2025-01-11 15:49:00|[Csv to Parquet v1.0.0](https://github.com/alisonpezzott/csv-to-parquet/releases/tag/v1.0.0)|Initial version|




