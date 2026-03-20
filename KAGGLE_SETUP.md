# Kaggle API Setup Guide

## Step 1: Get Your Kaggle API Token

1. Go to: **https://www.kaggle.com/settings/account**
2. Scroll down to the **"API"** section
3. Click **"Create New API Token"**
   - This will download a file named `kaggle.json`
   - This file contains your Kaggle username and API key (keep it private!)

## Step 2: Place the Config File

Save `kaggle.json` in the exact location:
- **Windows**: `C:\Users\Asus\.kaggle\kaggle.json`
- **Mac/Linux**: `~/.kaggle/kaggle.json`

If the `.kaggle` folder doesn't exist, create it:
```powershell
# PowerShell (Windows)
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.kaggle"
```

## Step 3: Set Correct Permissions (Important!)

The file must have restricted permissions:
```powershell
# On Windows PowerShell
$FilePath = "$env:USERPROFILE\.kaggle\kaggle.json"
$Acl = Get-Acl $FilePath
$Acl.SetAccessRuleProtection($true, $false)
$Rule = New-Object System.Security.AccessControl.FileSystemAccessRule(
    [System.Security.Principal.WindowsIdentity]::GetCurrent().User,
    'FullControl',
    'Allow'
)
$Acl.SetAccessRule($Rule)
Set-Acl -Path $FilePath -AclObject $Acl
```

## Step 4: Verify Setup

```powershell
Test-Path "$env:USERPROFILE\.kaggle\kaggle.json"
```
Should return: `True`

## Step 5: Download the Dataset

Once credentials are set up, run:
```bash
python download_kaggle_dataset.py
```

### Expected Output:
```
============================================================
Kaggle Lending Club Dataset Downloader
============================================================
Downloading Lending Club dataset from Kaggle...
✓ Dataset downloaded successfully!
Decompressing accepted_2007_to_2018Q4.csv.gz...
✓ Saved to accepted_2007_to_2018Q4.csv

Reading loan data...
Dataset shape: (2266684, 150)

Columns: [...]

✓ Selected 16 relevant columns

Loan Status Distribution:
Fully Paid              1653361
Charged Off             611737
...

✓ Sample dataset saved: loan_data_kaggle.csv (10000 rows)

============================================================
Done! Use 'loan_data_kaggle.csv' in your notebooks
============================================================
```

## Troubleshooting

### Issue: "Permission denied" on kaggle.json
**Solution**: Ensure file permissions are set correctly (Step 3)

### Issue: Still can't find kaggle.json
**Solution**: Verify the exact path:
```powershell
# Check if file exists
ls "$env:USERPROFILE\.kaggle\"
```

### Issue: "Invalid API key"
**Solution**: Your API token may have expired or there's a typo
- Generate a new token at https://www.kaggle.com/settings/account
- Delete the old `kaggle.json` and save the new one

## Next Steps

After downloading, the script creates:
- **`accepted_2007_to_2018Q4.csv`** - Full decompressed dataset (2.2M rows, ~1 GB)
- **`loan_data_kaggle.csv`** - Sample dataset (10,000 rows for quick testing)

Update your notebook to use the new dataset:
```python
# In notebook cell 1, replace:
df = pd.read_csv('loan_data.csv')

# With:
df = pd.read_csv('loan_data_kaggle.csv')  # Use sample for testing
# OR
df = pd.read_csv('accepted_2007_to_2018Q4.csv')  # Use full dataset
```

## Security Note
⚠️ **Never commit `kaggle.json` to version control!**
Add to `.gitignore`:
```
.kaggle/
kaggle.json
```
