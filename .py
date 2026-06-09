import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("AI Job Market Dataset.csv")

# Basic information
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Dataset statistics
print("\nSummary:")
print(df.describe(include='all'))

# Check column names first
print("\nAvailable Columns:")
for col in df.columns:
    print(col)

# Example: Top Job Titles
if 'Job_Title' in df.columns:
    print("\nTop 10 Job Titles:")
    print(df['Job_Title'].value_counts().head(10))

    plt.figure(figsize=(10,5))
    df['Job_Title'].value_counts().head(10).plot(kind='bar')
    plt.title("Top 10 Job Titles")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example: Top Locations
if 'Location' in df.columns:
    print("\nTop Locations:")
    print(df['Location'].value_counts().head(10))

    plt.figure(figsize=(10,5))
    df['Location'].value_counts().head(10).plot(kind='bar')
    plt.title("Top Hiring Locations")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Save cleaned dataset
df.to_csv("cleaned_ai_job_market.csv", index=False)

print("\nAnalysis Completed Successfully!")