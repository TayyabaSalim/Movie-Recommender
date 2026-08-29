# Netflix Movies & TV Shows — Data Analysis & Recommendation System

An end-to-end Data Analytics and Content-Based Recommendation System developed using Python. The project analyzes Netflix Movies and TV Shows data to uncover content trends, distributions, and patterns, while implementing an NLP-driven recommendation engine based on content similarity.

---

## Project Overview

This project combines exploratory data analysis (EDA), data visualization, an interactive web dashboard, and recommendation techniques into a unified analytics application.

* **Exploratory Data Analysis**: Performs data cleaning, deduplication, missing value imputation, and feature extraction.


* **Interactive Dashboard**: Provides an eight-chart visual analysis suite powered by Plotly and Dash.


* **Recommendation Engine**: Delivers real-time recommendations filtered by genre, country, release year, and type via a Flask API.



---

## Dataset Setup

The underlying dataset (`static/MOVIES.csv`) is omitted from this repository to maintain a lightweight codebase. To run the project locally, place a compatible **Netflix Movies and TV Shows** dataset inside the `static/` directory as `MOVIES.csv`.

---

## Exploratory Data Analysis & Visual Insights

The data cleaning and statistical visualization pipeline is implemented in `EDA.py`. Key steps include:

* Cleaning missing fields across `title`, `listed_in`, `country`, and `type`.


* Removing duplicate records matching on `title` and `release_year`.


* Extracting primary genres, primary countries, and title character counts.



### Sample Visualizations

#### 1. Content Production Over Time

Analyzes historical growth trends of streaming content additions.

#### 2. Release Year Distribution

Kernel Density Estimation (KDE) plot showing content concentration over release years.

#### 3. Top 6 Genres Distribution

Percentage share across the top primary genres in the catalog.

#### 4. Title Length Distribution

Histogram and density mapping of title character lengths.

#### 5. Movie vs. TV Show Trend Over Time

Stacked area chart highlighting the evolution of movies versus TV series over time.

---

## Interactive Analytics Dashboard

The interactive UI is built with Dash and Plotly (`dashboard.py`) using a modern dark neon visual theme. The dashboard presents eight grid-based visual components:

* Movies vs. TV Shows distribution (Donut chart)


* Release-year distribution (Histogram + Box plot)


* Content production over time (Line chart)


* Top 10 content genres (Horizontal bar chart)


* Top 6 genres market share (Pie chart)


* Top 10 producing countries (Horizontal bar chart)


* Title length character distribution (Histogram)


* Movie vs. TV Show trend evolution (Stacked area chart)



---

## Content-Based Recommendation System

The recommendation backend in `App.py` utilizes **TF-IDF Vectorization** and **Cosine Similarity**:

* Converts category metadata (`listed_in`) into TF-IDF feature vectors.


* Computes similarity scores across all catalog titles using cosine distance matrix operations.


* Supports multi-param filtering across parameters: `title`, `genre`, `country`, `year`, and `type`.


* Exposes API endpoints for dynamic filter options (`/api/options`) and query execution (`/api/recommend`).



---

## Technology Stack

* **Language**: Python
* **Web Frameworks**: Flask, Dash[cite: 1, 2]
* **Data Processing**: Pandas, NumPy


* **Visualization**: Plotly, Matplotlib, Seaborn


* **Machine Learning / NLP**: Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)



---

## Project Structure

```text
Netflix-Data-Analysis-Recommendation/
│
├── App.py                        # Flask API & Recommendation Engine
├── dashboard.py                  # Dash Interactive Visualization Web App
├── EDA.py                        # Data Cleaning & Static Plot Generator
├── plot1_content_types_donut.png # Generated Visual Asset
├── plot2_release_year_kde.png    # Generated Visual Asset
├── plot3_releases_per_year.png   # Generated Visual Asset
├── plot4_top_genres.png          # Generated Visual Asset
├── plot5_top6_genres_pie.png     # Generated Visual Asset
├── plot6_top_countries.png       # Generated Visual Asset
├── plot7_title_length_distribution.png # Generated Visual Asset
├── plot8_type_by_year_area.png   # Generated Visual Asset
└── README.md                     # Documentation

```

---

## Skills Demonstrated

* Data Cleaning, Profiling & Feature Engineering


* Exploratory Data Analysis & Statistical Plotting


* Interactive Web Dashboard Development (Dash/Plotly)


* Natural Language Processing (TF-IDF Feature Extraction)


* Vector Space Models & Cosine Similarity Scoring


* RESTful API Development (Flask)
