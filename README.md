# Netflix Movies & TV Shows — Data Analysis & Recommendation System

An end-to-end **Data Analytics and Content-Based Recommendation System** developed using Python. The project analyzes Netflix Movies and TV Shows data to uncover content trends, distributions, and patterns, while also implementing a recommendation engine based on content similarity.

## Project Overview

The project combines **exploratory data analysis, data visualization, interactive dashboards, and recommendation techniques** into a single analytics application.
 
### Exploratory Data Analysis

* Performed data inspection, cleaning, and preprocessing
* Identified and handled missing values
* Removed duplicate records based on title and release year
* Analyzed content types, genres, countries, and release years
* Examined content production trends and title-length distributions
* Generated descriptive statistics and analytical visualizations

The data-cleaning pipeline is implemented in `EDA.py`.

### Interactive Analytics Dashboard

Developed an interactive dashboard using **Dash and Plotly** to present key insights through eight visualizations, including:

* Movies vs. TV Shows distribution
* Release-year distribution
* Content production trends
* Top genres
* Genre distribution
* Leading content-producing countries
* Title-length distribution
* Movie vs. TV Show trends over time

The dashboard integrates Pandas-based data processing with interactive Plotly visualizations.

### Content-Based Recommendation System

Implemented a content-based recommendation engine using **TF-IDF vectorization and cosine similarity**.

The system:

* Converts genre/category information into TF-IDF feature vectors
* Calculates cosine similarity between titles
* Ranks content according to similarity
* Supports filtering by genre, country, release year, and content type
* Returns top-N recommendations

## Technology Stack

**Languages & Frameworks**

* Python
* Flask
* Dash

**Data Analysis & Visualization**

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly

**Machine Learning / NLP**

* Scikit-learn
* TF-IDF
* Cosine Similarity

## Project Structure

```text
Netflix-Data-Analysis-Recommendation/
│
├── App.py
├── dashboard.py
├── EDA.py
└── README.md
```


## Skills Demonstrated

* Data Cleaning & Preprocessing
* Exploratory Data Analysis
* Data Visualization
* Interactive Dashboard Development
* Feature Engineering
* NLP Techniques
* TF-IDF Vectorization
* Cosine Similarity
* Content-Based Recommendation Systems
* Flask API Development
* Python Data Analytics
