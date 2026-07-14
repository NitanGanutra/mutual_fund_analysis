"""
Bluestock Mutual Fund Analytics

File: data_ingestion.py

Purpose:
Load raw mutual fund datasets, validate data,
and store cleaned data into SQLite database.

Author: Nitan Sharma
"""
import pandas as pd
import os

data_folder = "data/raw"

for file in os.listdir(data_folder):

    if file.endswith(".csv"):

        filepath = os.path.join(
            data_folder,
            file
        )
        df = pd.read_csv(filepath, encoding='latin1')

        print("\n" + "="*50)
        print(f"Dataset: {file}")
        print("="*50)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
       