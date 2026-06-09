import pandas as pd

df = pd.read_csv(r"C:\Users\mohammed ahsan\Downloads\archive (3)\AI Job Market Dataset.csv")

print(df.head())
print(df.columns.tolist())
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\mohammed ahsan\Downloads\archive (3)\AI Job Market Dataset.csv")

print("Dataset Shape:", df.shape)

print("\nTop 10 Job Titles")
print(df["job_title"].value_counts().head(10))

plt.figure(figsize=(10,5))
df["job_title"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 AI Job Titles")
plt.tight_layout()
plt.show()

print("\nTop Countries")
print(df["country"].value_counts().head(10))

plt.figure(figsize=(10,5))
df["country"].value_counts().head(10).plot(kind="bar")
plt.title("Top Hiring Countries")
plt.tight_layout()
plt.show()

print("\nAverage Salary by Experience Level")
print(df.groupby("experience_level")["salary"].mean())

plt.figure(figsize=(8,5))
df.groupby("experience_level")["salary"].mean().plot(kind="bar")
plt.title("Average Salary by Experience")
plt.tight_layout()
plt.show()

skills = [
    "skills_python",
    "skills_sql",
    "skills_ml",
    "skills_deep_learning",
    "skills_cloud"
]

skill_counts = df[skills].sum()

print("\nSkill Demand")
print(skill_counts)

plt.figure(figsize=(8,5))
skill_counts.plot(kind="bar")
plt.title("Most Demanded Skills")
plt.tight_layout()
plt.show()

print("\nProject Completed Successfully!")