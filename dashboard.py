# dashboard.py
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html


df = pd.read_csv("static/MOVIES.csv", encoding="latin1", on_bad_lines="skip")
df = df.fillna({
    "title": "",
    "listed_in": "",
    "country": "",
    "release_year": 0,
    "type": ""
}).copy()


df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce").fillna(0).astype(int)
df["title_length"] = df["title"].str.len()
df["genre_primary"] = df["listed_in"].str.split(",").str[0].str.strip()
df["country_primary"] = df["country"].str.split(",").str[0].str.strip()

type_counts = df["type"].value_counts()
year_counts = df["release_year"].value_counts().sort_index()
all_genres = df["listed_in"].str.split(",").explode().str.strip()
top_genres = all_genres.value_counts().head(10)
top6_genres = top_genres.head(6)
all_countries = df["country"].str.split(",").explode().str.strip()
top_countries = all_countries.value_counts().head(10)
type_year = df.groupby(["release_year", "type"]).size().unstack(fill_value=0)

neon_colors = ["#00C6FF", "#0072FF", "#7A00FF", "#C300FF", "#FF00C8"]

template_dark_neon = {
    "layout": {
        "paper_bgcolor": "rgba(10,10,10,1)",
        "plot_bgcolor": "rgba(10,10,10,1)",
        "font": {"color": "white", "family": "Arial"},
        "title": {"x": 0.02, "font": {"size": 20, "color": "#00C6FF"}},
        "xaxis": {"gridcolor": "#222"},
        "yaxis": {"gridcolor": "#222"},
        "colorway": neon_colors,
    }
}
px.defaults.template = template_dark_neon
px.defaults.color_continuous_scale = neon_colors

fig1 = px.pie(
    names=type_counts.index,
    values=type_counts.values,
    hole=0.55,
    title="Distribution: Movies vs TV Shows"
)
fig1.update_traces(textinfo="percent+label")

fig2 = px.histogram(
    df[df["release_year"] > 0],
    x="release_year",
    nbins=50,
    marginal="box",
    title="Release Year Distribution (Histogram + Box)"
)
fig2.update_traces(marker_line_width=0)

fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=year_counts.index,
    y=year_counts.values,
    mode="lines+markers",
    name="Titles per Year",
))
fig3.update_layout(title="Content Production Over Time", xaxis_title="Year", yaxis_title="Count")

fig4 = px.bar(
    x=top_genres.values[::-1],
    y=top_genres.index[::-1],
    orientation="h",
    title="Top 10 Genres"
)
fig4.update_layout(xaxis_title="Frequency")

fig5 = px.pie(
    names=top6_genres.index,
    values=top6_genres.values,
    title="Top 6 Genres (Share)"
)
fig5.update_traces(textinfo="percent+label")

fig6 = px.bar(
    x=top_countries.values[::-1],
    y=top_countries.index[::-1],
    orientation="h",
    title="Top 10 Countries Producing Content"
)
fig6.update_layout(xaxis_title="Frequency")

fig7 = px.histogram(
    df,
    x="title_length",
    nbins=30,
    title="Title Length Distribution (characters)"
)
fig7.update_traces(opacity=0.85)

fig8 = go.Figure()
idx = type_year.index
fig8.add_trace(go.Scatter(x=idx, y=type_year.get("Movie", 0), stackgroup="one", name="Movies", mode="none"))
fig8.add_trace(go.Scatter(x=idx, y=type_year.get("TV Show", 0), stackgroup="one", name="TV Shows", mode="none"))
fig8.update_layout(title="Movie vs TV Show Trend Over Time", xaxis_title="Year", yaxis_title="Count")

for fig in (fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8):
    fig.update_layout(
        template=template_dark_neon,
        margin=dict(l=10, r=10, t=40, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )


app = Dash(__name__)
app.title = "Movies & TV Shows"

card_style = {
    "backdrop-filter": "blur(8px)",
    "background": "linear-gradient(135deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01))",
    "border-radius": "14px",
    "padding": "14px",
    "border": "1px solid rgba(255,255,255,0.06)",
    "box-shadow": "0 6px 20px rgba(0,0,0,0.6)",
}

app.layout = html.Div(
    style={
        "background": "linear-gradient(180deg, #050505 0%, #0f0f0f 100%)",
        "min-height": "100vh",
        "padding": "28px",
        "font-family": "Arial, sans-serif",
    },
    children=[
        html.Div([
            html.H1("Streaming Content Dashboard", style={"color": "#00C6FF", "margin": "0", "font-size": "34px"}),
            html.P("8 visual insights", style={"color": "#B0B0B0", "margin-top": "6px"})
        ], style={"text-align": "center", "margin-bottom": "18px"}),

        html.Div(
            style={
                "display": "grid",
                "grid-template-columns": "repeat(2, 1fr)",
                "gap": "22px",
            },
            children=[
                html.Div(dcc.Graph(figure=fig1), style=card_style),
                html.Div(dcc.Graph(figure=fig2), style=card_style),
                html.Div(dcc.Graph(figure=fig3), style=card_style),
                html.Div(dcc.Graph(figure=fig4), style=card_style),
                html.Div(dcc.Graph(figure=fig5), style=card_style),
                html.Div(dcc.Graph(figure=fig6), style=card_style),
                html.Div(dcc.Graph(figure=fig7), style=card_style),
                html.Div(dcc.Graph(figure=fig8), style=card_style),
            ]
        ),

        html.Div(
            style={"marginTop": "18px", "color": "#888", "fontSize": "12px", "textAlign": "center"},
            children="Local dashboard · uses pandas + plotly + dash · data loaded from static/MOVIES.csv"
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
