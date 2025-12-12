# DE Retail — Data Engineering & Analysis

This repository contains a data engineering pipeline and analysis for retail sales data. It loads CSV files, cleans and standardizes data, produces cleaned CSV outputs, and writes the cleaned tables to a SQL Server database.

## Project Structure
```
Retail-Data-Pipeline/
├── DataSources/  Raw CSV files
├── cleaned_data/  Cleaned datasets
├── project_DE.ipynb  extract and cleand to export  
├── database.sql  SQL database schema
├── analysis_query.sql  requierments queries
└── README.md This file
```
## Features

- Clean and standardize retail CSV datasets
- Calculate derived metrics like `total_price`
- Remove duplicates, fix missing values, normalize text
- Save cleaned data as CSVs and upload to SQL Server
- Optional Jupyter notebook
- analysis requierments

# what i do

- det Raw CSV source files
- then Cleaned CSV files by pandas
- then go to mssql and create database and make relations
- then connect to mssql and load data
- then in mssql i analysis data by sql
- then in exportQuery i get outOutput from query to csv
