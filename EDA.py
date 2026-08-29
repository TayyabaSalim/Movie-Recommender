import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# =========================================================
# THEME: CYBERPUNK NEON (Blue → Purple → Pink)
# =========================================================
plt.style.use("dark_background")

custom_cmap = [
    "#00C6FF",  # neon blue
    "#0072FF",  # deep blue
    "#7A00FF",  # purple
    "#C300FF",  # magenta
    "#FF00C8",  # neon pink
]

sns.set_theme(
    style="darkgrid",
    rc={
        "axes.facecolor": "#0A0A0A",
        "figure.facecolor": "#0A0A0A",
        "grid.color": "#2C2C2C",
        "axes.edgecolor": "#444444",
        "text.color": "white",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "font.size": 12,
    }
)

sns.set_palette(custom_cmap)

plt.ion()
plt.rcParams['figure.dpi'] = 130


print("Loading dataset...")
raw_df = pd.read_csv("static/MOVIES.csv", encoding="latin1", on_bad_lines="skip")

print("\n=== RAW DATA HEAD ===")
print(raw_df.head())

print("\n=== RAW DATA INFO ===")
print(raw_df.info())

print("\n=== MISSING VALUES (Before Cleaning) ===")
print(raw_df.isnull().sum())


df = raw_df.copy()

df = df.fillna({
    "title": "",
    "listed_in": "",
    "country": "",
    "release_year": 0,
    "type": ""
})

df["title_lower"] = df["title"].str.lower()
df["genre_clean"] = df["listed_in"].str.lower()
df["country_clean"] = df["country"].str.lower()

print("\n=== AFTER CLEANING: Missing Values ===")
print(df.isnull().sum())

before = df.shape[0]
df = df.drop_duplicates(subset=["title", "release_year"])
after = df.shape[0]

print(f"\nRemoved Duplicates: {before - after}")


print("\n=== SHAPE BEFORE CLEANING ===")
print(raw_df.shape)

print("\n=== SHAPE AFTER CLEANING ===")
print(df.shape)

print("\n=== BASIC STATISTICS ===")
print(df.describe(include="all"))



plt.figure(figsize=(6, 6))
counts = df["type"].value_counts()

plt.pie(counts, labels=counts.index, autopct='%1.1f%%',
        startangle=140, pctdistance=0.85)

centre = plt.Circle((0, 0), 0.55, color='black')
plt.gca().add_artist(centre)

plt.title("Distribution of Content Types", fontsize=13)
plt.tight_layout()
plt.savefig("plot1_content_types_donut.png", dpi=300, bbox_inches='tight')
plt.close()


plt.figure(figsize=(10, 4))
sns.kdeplot(df["release_year"], fill=True, linewidth=2)
plt.title("Release Year Trend", fontsize=13)
plt.xlabel("Year")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("plot2_release_year_kde.png", dpi=300, bbox_inches='tight')
plt.close()



year_counts = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10, 4))
plt.plot(year_counts.index, year_counts.values, marker="o", linewidth=2)
plt.title("Content Production Over Time", fontsize=13)
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("plot3_releases_per_year.png", dpi=300, bbox_inches='tight')
plt.close()



all_genres = df["listed_in"].str.split(",").explode().str.strip()
top_genres = all_genres.value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title("Top 10 Genres", fontsize=13)
plt.xlabel("Frequency")
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig("plot4_top_genres.png", dpi=300, bbox_inches='tight')
plt.close()



top6 = top_genres.head(6)

plt.figure(figsize=(6, 6))
plt.pie(top6.values, labels=top6.index, autopct='%1.1f%%', startangle=140)
plt.title("Top 6 Genres", fontsize=13)
plt.tight_layout()
plt.savefig("plot5_top6_genres_pie.png", dpi=300, bbox_inches='tight')
plt.close()



all_countries = df["country"].str.split(",").explode().str.strip()
top_countries = all_countries.value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Countries Producing Content", fontsize=13)
plt.xlabel("Frequency")
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig("plot6_top_countries.png", dpi=300, bbox_inches='tight')
plt.close()



df["title_length"] = df["title"].str.len()

plt.figure(figsize=(8, 4))
sns.histplot(df["title_length"], bins=30, kde=True)
plt.title("Title Length Distribution", fontsize=13)
plt.xlabel("Number of Characters")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("plot7_title_length_distribution.png", dpi=300, bbox_inches='tight')
plt.close()



type_year = df.groupby(["release_year", "type"]).size().unstack(fill_value=0)

plt.figure(figsize=(10, 5))
plt.stackplot(
    type_year.index,
    type_year.get("Movie", 0),
    type_year.get("TV Show", 0),
    labels=["Movies", "TV Shows"],
    alpha=0.8
)

plt.title("Movie vs TV Show Trend Over Time", fontsize=13)
plt.xlabel("Year")
plt.ylabel("Count")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("plot8_type_by_year_area.png", dpi=300, bbox_inches='tight')
plt.close()
