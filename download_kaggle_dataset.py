"""
Script to download and prepare Kaggle Lending Club dataset for the project
"""

import os
import gzip
import shutil
import pandas as pd
from pathlib import Path

def download_lending_club_data():
    """Download Lending Club dataset from Kaggle"""
    try:
        import kaggle
        print("Downloading Lending Club dataset from Kaggle...")
        kaggle.api.dataset_download_files('wordsforthewise/lending-club', path='.', unzip=False)
        print("✓ Dataset downloaded successfully!")
        return True
    except Exception as e:
        print(f"✗ Error downloading dataset: {e}")
        print("\nTo download manually:")
        print("1. Go to: https://www.kaggle.com/datasets/wordsforthewise/lending-club")
        print("2. Click 'Download' and place the .gz files in this directory")
        return False

def decompress_gzip(gzip_file, output_file):
    """Decompress gzip file"""
    print(f"Decompressing {gzip_file}...")
    with gzip.open(gzip_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"✓ Saved to {output_file}")

def prepare_loan_data():
    """Prepare the loan data for the model"""
    try:
        # Read the accepted loans data
        print("\nReading loan data...")
        df = pd.read_csv('accepted_2007_to_2018Q4.csv', low_memory=False)
        
        print(f"Dataset shape: {df.shape}")
        print(f"\nColumns: {list(df.columns)}")
        
        # Key columns for loan default prediction
        important_cols = [
            'loan_status',  # Target variable
            'int_rate', 'grade', 'sub_grade', 'emp_length',
            'home_ownership', 'annual_inc', 'purpose',
            'dti', 'fico_range_low', 'fico_range_high',
            'open_acc', 'pub_rec', 'revol_bal', 'total_acc',
            'term', 'loan_amnt'
        ]
        
        # Select available columns
        available_cols = [col for col in important_cols if col in df.columns]
        df_subset = df[available_cols].copy()
        
        print(f"\n✓ Selected {len(available_cols)} relevant columns")
        
        # Show loan status distribution
        print(f"\nLoan Status Distribution:")
        print(df_subset['loan_status'].value_counts())
        
        # Save a sample dataset for testing
        sample_size = min(10000, len(df_subset))
        df_sample = df_subset.sample(n=sample_size, random_state=42)
        df_sample.to_csv('loan_data_kaggle.csv', index=False)
        print(f"\n✓ Sample dataset saved: loan_data_kaggle.csv ({sample_size} rows)")
        
        return True
    except Exception as e:
        print(f"✗ Error preparing data: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Kaggle Lending Club Dataset Downloader")
    print("=" * 60)
    
    # Step 1: Download
    if download_lending_club_data():
        # Step 2: Decompress
        gzip_file = 'accepted_2007_to_2018Q4.csv.gz'
        if os.path.exists(gzip_file):
            decompress_gzip(gzip_file, 'accepted_2007_to_2018Q4.csv')
            
            # Step 3: Prepare
            prepare_loan_data()
        else:
            print(f"✗ {gzip_file} not found after download")
    
    print("\n" + "=" * 60)
    print("Done! Use 'loan_data_kaggle.csv' in your notebooks")
    print("=" * 60)
