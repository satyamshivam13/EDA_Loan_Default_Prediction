"""
Alternative: Manual Download Guide
For users who prefer to download directly from Kaggle website
"""

# MANUAL DOWNLOAD METHOD (No API Key Required)
# =============================================

# Step 1: Download via Web Browser
# 1. Go to: https://www.kaggle.com/datasets/wordsforthewise/lending-club
# 2. Click the blue "Download" button (requires Kaggle login)
# 3. This downloads: lending-club.zip (~648 MB)
# 4. Extract it to this project directory
#    You'll get two .gz files:
#    - accepted_2007_to_2018Q4.csv.gz
#    - rejected_2007_to_2018Q4.csv.gz

# Step 2: Process the Downloaded Files
# Once you have the .gz files, run this script:

import gzip
import shutil
import pandas as pd
import os

def decompress_and_prepare():
    """Decompress and prepare manually downloaded Kaggle files"""
    
    gzip_file = 'accepted_2007_to_2018Q4.csv.gz'
    csv_file = 'accepted_2007_to_2018Q4.csv'
    
    if not os.path.exists(gzip_file):
        print(f"✗ Error: {gzip_file} not found")
        print(f"   Please download from: https://www.kaggle.com/datasets/wordsforthewise/lending-club")
        return False
    
    # Decompress
    print(f"Decompressing {gzip_file}...")
    try:
        with gzip.open(gzip_file, 'rb') as f_in:
            with open(csv_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"✓ Decompressed to {csv_file}")
    except Exception as e:
        print(f"✗ Decompression failed: {e}")
        return False
    
    # Read and sample
    print(f"\nReading loan data...")
    try:
        df = pd.read_csv(csv_file, low_memory=False)
        print(f"✓ Dataset loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")
        
        # Create sample
        sample_size = min(10000, len(df))
        df_sample = df.sample(n=sample_size, random_state=42)
        df_sample.to_csv('loan_data_kaggle.csv', index=False)
        print(f"✓ Sample created: loan_data_kaggle.csv ({sample_size:,} rows)")
        
        # Show target distribution
        if 'loan_status' in df.columns:
            print(f"\nLoan Status Distribution:")
            print(df['loan_status'].value_counts())
        
        return True
    except Exception as e:
        print(f"✗ Error processing data: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Kaggle Lending Club - Manual Download Processing")
    print("=" * 60)
    decompress_and_prepare()

# INSTRUCTIONS FOR QUICK TEST (No Download Needed)
# ================================================

# If you want to test quickly without downloading the large dataset,
# use the small sample dataset included in the project:
# 
#   df = pd.read_csv('loan_data.csv')
#
# This is sufficient for model development and testing.
# Switch to the full Kaggle dataset later for production use.
