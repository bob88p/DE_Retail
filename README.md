# DE Retail — Data Engineering & Analysis

This repository contains a data engineering pipeline and analysis for retail sales data. It loads CSV files, cleans and standardizes data, produces cleaned CSV outputs, and writes the cleaned tables to a SQL Server database.

## Project Structure

DE\*Retail/
├─ DataSources/ # Raw CSV source files
├─ cleaned_data/ # Cleaned CSV files
├─ analysis/ # Output csv for all querys
├─ to make database loaded and analysis
├─ project_DE.ipynb # Jupyter notebook preprocessing and connect database

├─ exportQuery.py # Python script to make analysis folder(csv)
├─ requirements.txt # Python dependencies
├─ .gitignore
└─ README.md

## Features

- Clean and standardize retail CSV datasets
- Calculate derived metrics like `total_price`
- Remove duplicates, fix missing values, normalize text
- Save cleaned data as CSVs and upload to SQL Server
- Optional Jupyter notebook
- analysis requierments
