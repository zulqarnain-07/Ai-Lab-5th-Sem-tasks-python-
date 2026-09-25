# Perform following tasks using Pandas on the given dataset of student-scores.csv in lab
#  1: Calculate and add a "Science Proficiency" column
# Add a new column called science_proficiency that categorizes students based on
# their average scores in physics, chemistry, and biology:
# High if the average is greater than 85.
# Medium if the average is between 70 and 85.
# Low if the average is below 70.
#  2: Identify students who excel in extracurricular activities and academics
# Find students who participate in extracurricular activities and have an average
# score greater than 80 across all their subjects.
#  3: Calculate average study hours based on career aspirations
# Group students by their career_aspiration and calculate the average weekly selfstudy hours for each group.
#  4: Create a "Performance Tag" based on absence and scores
# Create a new column performance_tag based on the following conditions:
# Excellent if the average score is above 85 and absence days are fewer than 3.
# Good if the average score is between 70 and 85.
# Needs Improvement if the average score is below 70 or absence days are more
# than 5

# Task 2
import pandas as pd

df = pd.read_csv("student-scores.csv")

print("\nTask 2.1")

df["science_average"] = (
    df["physics_score"]
    + df["chemistry_score"]
    + df["biology_score"]
) / 3

def get_proficiency(avg):
    if avg > 85:
        return "High"
    elif avg >= 70:
        return "Medium"
    else:
        return "Low"

df["science_proficiency"] = df["science_average"].apply(get_proficiency)
print(df[[
    "id",
    "first_name",
    "science_average",
    "science_proficiency"
]])
print("\nTask 2.2")

subjects = [
    "math_score",
    "history_score",
    "physics_score",
    "chemistry_score",
    "biology_score",
    "english_score",
    "geography_score"
]

df["average_score"] = df[subjects].mean(axis=1)

excellent_students = df[
    (df["extracurricular_activities"] == True)
    & (df["average_score"] > 80)
]

print(excellent_students[[
    "id",
    "first_name",
    "last_name",
    "average_score"
]])
print("\nTask 2.3")

study_hours = df.groupby(
    "career_aspiration",
    as_index=False
)["weekly_self_study_hours"].mean()

print(study_hours)

print("\nTask 2.4")
def get_performance(row):
    if row["average_score"] > 85 and row["absence_days"] < 3:
        return "Excellent"
    elif 70 <= row["average_score"] <= 85:
        return "Good"
    elif row["average_score"] < 70 or row["absence_days"] > 5:
        return "Needs Improvement"

df["performance_tag"] = df.apply(
    get_performance,
    axis=1
)

print(df[[
    "id",
    "first_name",
    "average_score",
    "absence_days",
    "performance_tag"
]])
