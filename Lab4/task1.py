# <!-- 
# Task 1
# Implement following three tasks on given dataset of apple store. The Apple Store dataset contains
# detailed information about mobile applications available on the iOS App Store. It includes
# attributes such as app ID, track name, size in bytes, price, currency, user ratings, content ratings,
# supported devices, number of languages, and primary genre. This dataset is widely used for
# analyzing app trends, user preferences, and market patterns.
# 1. Read the given Apple Store dataset from the CSV file using a methodology of your
# choice. You may use Python’s built-in CSV module pandas library, or any other
# suitable approach. Ensure that the data is successfully loaded into an appropriate
# structure, and display the first few records to verify that the dataset has been read
# correctly.
# 2. Identify the top three games that are most popular among teenagers, specifically
# those with a content rating of 12+, based on their user ratings and download counts.
# 3. Generate a report on the five most downloaded applications in the ‘Social
# Networking’ category, highlighting their names, total downloads, and user ratings -->


import pandas as pd

df = pd.read_csv("AppleStore.csv")

print(df.head(10))

teen_games = df[df["cont_rating"] == "12+"]

games = teen_games[
    teen_games["prime_genre"] == "Games"
]

top_3_games = games.sort_values(
    "rating_count_tot",
    ascending=False
).head(3)

print(top_3_games[
    ["track_name", "rating_count_tot", "user_rating"]
])

social_apps = df[
    df["prime_genre"] == "Social Networking"
]

top_5_social = social_apps.sort_values(
    "rating_count_tot",
    ascending=False
).head(5)

print(
    top_5_social[
        ["track_name", "rating_count_tot", "user_rating"]
    ]
)