from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__, static_folder="static")

df = pd.read_csv("static/MOVIES.csv", encoding="latin1", on_bad_lines="skip")

df = df.fillna("")

df["title_lower"] = df["title"].str.lower()
title_to_index = {t: i for i, t in enumerate(df["title_lower"])}

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["listed_in"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


@app.route("/")
def home():
    return send_from_directory("static", "index.html")


@app.route("/api/options")
def get_options():
    genres = sorted(set(g.strip() for x in df["listed_in"].str.split(",") for g in x))
    countries = sorted(set(c.strip() for x in df["country"].str.split(",") for c in x))

    return jsonify({
        "genres": genres,
        "countries": countries
    })

@app.route("/api/recommend", methods=["POST"])
def recommend_movies():
    data = request.get_json()

    title = data.get("title", "").lower().strip()
    genre = data.get("genre", "").strip()
    country = data.get("country", "").strip()
    year = data.get("year", "").strip()
    show_type = data.get("type", "").strip()
    top_n = int(data.get("top_n", 10))

    df_filtered = df.copy()

    similar_df = None

    if title:
        if title not in title_to_index:
            return jsonify({"results": [], "error": f"Title '{title}' not found"}), 404

        idx = title_to_index[title]
        sim_scores = cosine_sim[idx]
        df["similarity"] = sim_scores

        similar_df = df.sort_values(by="similarity", ascending=False)

        similar_df = similar_df[similar_df["title_lower"] != title]
    else:
        similar_df = df.copy()
        similar_df["similarity"] = 0.0

    if show_type and show_type.lower() != "any":
        similar_df = similar_df[similar_df["type"].str.lower() == show_type.lower()]

    if genre and genre.lower() != "any":
        similar_df = similar_df[similar_df["listed_in"].str.lower().str.contains(genre.lower())]

    if country and country.lower() != "any":
        similar_df = similar_df[similar_df["country"].str.lower().str.contains(country.lower())]

    if year:
        if year.isdigit():
            similar_df = similar_df[similar_df["release_year"] == int(year)]
        else:
            return jsonify({"results": [], "error": "Invalid year"}), 400


    final = similar_df.head(top_n)

    results = final[["title", "type", "release_year", "listed_in", "country"]].to_dict(orient="records")
    return jsonify({"results": results})



if __name__ == "__main__":
    print("Static Folder:", app.static_folder)
    app.run(debug=False)
