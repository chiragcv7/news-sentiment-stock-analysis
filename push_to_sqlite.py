import sqlite3
import json

# Connect to a local SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("news_sentiment.db")
c = conn.cursor()

# Create tables
c.execute("""
CREATE TABLE IF NOT EXISTS RAW_NEWS_DATA (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS ANALYTICS_READY_SENTIMENT (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    published_at TEXT,
    company TEXT,
    sentiment_score REAL,
    topic TEXT
)
""")

# Load JSON results from your LLM pipeline
with open("news_sentiment_results.json") as f:
    news_data = json.load(f)

# Insert raw JSON into RAW_NEWS_DATA
for article in news_data:
    c.execute(
        "INSERT INTO RAW_NEWS_DATA (data) VALUES (?)",
        (json.dumps(article),)
    )

# Flatten data into ANALYTICS_READY_SENTIMENT
for article in news_data:
    published_at = article.get("publishedAt")
    analysis = article.get("analysis", {})
    if "error" in analysis:
        continue
    companies = analysis.get("Companies mentioned", [])
    if isinstance(companies, str):
        companies = [companies]
    for company in companies:
        c.execute(
            "INSERT INTO ANALYTICS_READY_SENTIMENT (published_at, company, sentiment_score, topic) VALUES (?, ?, ?, ?)",
            (published_at, company, analysis.get("Sentiment Score"), analysis.get("Primary Topic"))
        )

# Commit and close connection
conn.commit()
conn.close()

print("✅ Data saved locally in SQLite database (news_sentiment.db)")