# Loan-Default-Prediction-using-Artificial-Neural-Networks
Loan default prediction is a common problem in the financial industry, as it can help lenders or banks identify borrowers who are likely to default on their loans. This information can be further used to adjust loan terms/conditions, reserve additional funds to cover potential losses, or even deny/refuse loans to high-risk borrowers. In this article, we will develop a machine learning-based solution to predict loan default.

__Aim__ - The goal of this project is to build a __Deep Learning__ model that can predict if a person will default on the loan based on the loan and personal information provided. The model is intended to be used as a reference tool for the client and the financial institutions to help make decisions on issuing loans, so that the risk can be lowered, and the profit can be maximized.

# Steps Performed
1.	Checking for null values present in dataset.
2.	Univariate Analysis of all feature columns. Observations of same has been mentioned in source code file.
3.	Bivariate Analysis of all feature columns. Observations of same has been mentioned in source code file.
4.	Multivariate Analysis of all feature columns. Observations of same has been mentioned in source code file.
5.	Separating and Scaling the Numerical Columns of dataset using Standard Scaler.
6.	Separating the categorical columns of dataset.
7.	Concatenating Numerical and Categorical columns.
8.	Creating dummies for the ‘Purpose’ Column.
9.	Separating Features and Target variable.
10.	Applying SMOTE technique to rectify class imbalance in Target variable.
11.	Dividing the data into training and testing.
12.	ANN Model building.
13.	Analyzing accuracy, loss, precision and recall curves.
14.	Saving the model.


# Tools and Technologies used
1) __Language__ : Python
2) __IDE__ : Jupyter Notebook
3) __Pandas__ : For loading the dataset and performing data wrangling
4) __Matplotlib__: For data visualization.
5) __Seaborn__: For data visualization.
6) __NumPy__: For mathematical operations and array handling.
7) __Scikit-learn__: For preprocessing (StandardScaler), model evaluation, and train/test splitting.
8) __Imbalanced-learn__: For SMOTE (Synthetic Minority Over-sampling Technique) to handle class imbalance.
9) __TensorFlow and Keras__: For building and training the Artificial Neural Network model.
10) __Livelossplot__: For real-time visualization of training metrics during model fitting.

# Model Architecture

The Artificial Neural Network model consists of the following layers:
- **Input Layer**: 19 features (8 numerical scaled features + 11 one-hot encoded categorical features)
- **Hidden Layer 1**: 25 neurons with ReLU activation and L2 regularization
- **Batch Normalization**: Applied after each hidden layer
- **Hidden Layer 2**: 55 neurons with ReLU activation and L2 regularization
- **Hidden Layer 3**: 35 neurons with ReLU activation and L2 regularization
- **Hidden Layer 4**: 25 neurons with ReLU activation and L2 regularization
- **Output Layer**: 1 neuron with Sigmoid activation for binary classification
- **Optimizer**: Adam
- **Loss Function**: Binary Cross-entropy
- **Total Parameters**: 5,376 (21.00 KB)

# Dataset & Preprocessing

- **Classes**: Binary classification (Default: No/Yes)
- **Class Imbalance Handling**: SMOTE technique applied to balance training data
  - Original dataset - Non-default: 8,045 | Default: 1,533
  - After SMOTE - Non-default: 8,045 | Default: 8,045
- **Training/Testing Split**: 80% training (12,872 samples), 20% testing (3,218 samples)

# Model Performance

The trained model achieved the following metrics on the test set:
- **Accuracy**: 80.92%
- **Precision**: 78.58%
- **Recall**: 84.85%
- **Test Loss**: 0.47

The model shows good generalization with training accuracy reaching 86.0% and validation accuracy stabilizing around 80.9%, indicating a well-balanced model that avoids overfitting.

# Model Export

The trained model is exported in two formats:
- `Loan_default.keras` (121 KB) - Modern Keras format (recommended)
- `Loan_default.h5` (140 KB) - Legacy HDF5 format (for compatibility)

# Dataset Options

## Current Dataset
The project comes with a small synthetic dataset (`loan_data.csv`, 10,000 rows) for quick testing and learning.

## Recommended: Kaggle Lending Club Dataset
For a more comprehensive and realistic dataset, use the **Lending Club Loan Data** from Kaggle:
- **URL**: https://www.kaggle.com/datasets/wordsforthewise/lending-club
- **Size**: 648 MB (compressed), ~2.2 GB (uncompressed)
- **Records**: 2.2M+ loans (2007-2018)
- **Features**: 150+ loan and borrower attributes
- **Target**: `loan_status` (Fully Paid, Charged Off, Default, etc.)

### Steps to Use Lending Club Dataset:

1. **Install Kaggle API**:
   ```bash
   pip install kaggle
   ```

2. **Setup Kaggle Credentials**:
   - Go to https://www.kaggle.com/settings/account
   - Click "Create New API Token" (downloads `kaggle.json`)
   - Move to `~/.kaggle/kaggle.json` (or `%USERPROFILE%\.kaggle\kaggle.json` on Windows)

3. **Download Dataset**:
   ```bash
   python download_kaggle_dataset.py
   ```
   This script will:
   - Download the dataset from Kaggle
   - Decompress the gzip files
   - Extract relevant columns
   - Create a sample CSV (`loan_data_kaggle.csv`)

4. **Use in Notebooks**:
   Replace `loan_data.csv` with `loan_data_kaggle.csv` in the notebook cells.

# Setup & Execution

1. Install dependencies:
   ```bash
   pip install pandas scikit-learn imbalanced-learn tensorflow numpy livelossplot kaggle
   ```

2. **Choose your dataset**:
   - **Option A (Quick Start)**: Use the included `loan_data.csv` (10K rows, ~500 KB)
   - **Option B (Comprehensive)**: Download Lending Club data using the script above

3. Update the notebook to use your chosen dataset:
   ```python
   df = pd.read_csv('loan_data.csv')  # or 'loan_data_kaggle.csv'
   ```

4. Run the notebooks in order:
   - `EDA_Loan_Default_Prediction_Project.ipynb` - Exploratory Data Analysis
   - `Model_Building_Loan_Default_Prediction_Project.ipynb` - Model training and evaluation

# Conclusion

A Deep Learning Artificial Neural Network model has been successfully developed to predict loan default with an accuracy of **80.92%**. The model demonstrates strong recall (84.85%) for identifying potential defaulters and maintains good precision (78.58%) to minimize false positives. The use of SMOTE technique effectively addressed class imbalance, and L2 regularization with batch normalization helped achieve a well-generalized model. This model can serve as a reliable decision-support tool for financial institutions in assessing credit risk and making informed lending decisions.
