import json
import snowflake.connector
from datetime import datetime

# -------------------
# Snowflake config
SNOWFLAKE_USER = "YOUR_USERNAME"
SNOWFLAKE_PASSWORD = "YOUR_PASSWORD"
SNOWFLAKE_ACCOUNT = "YOUR_ACCOUNT"   # e.g., xy12345.us-east-1
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_DATABASE = "YOUR_DB"
SNOWFLAKE_SCHEMA = "PUBLIC"
# -------------------

# Connect
ctx = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)
cs = ctx.cursor()

# Load JSON from file
with open("news_sentiment_results.json") as f:
    news_data = json.load(f)

# -------------------
# 1️⃣ Insert into RAW_NEWS_DATA
cs.execute("""
CREATE TABLE IF NOT EXISTS RAW_NEWS_DATA (
    id STRING AUTOINCREMENT,
    data VARIANT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

for article in news_data:
    cs.execute(
        "INSERT INTO RAW_NEWS_DATA (data) VALUES (%s)",
        (json.dumps(article),)
    )

# -------------------
# 2️⃣ Flatten into ANALYTICS_READY_SENTIMENT
cs.execute("""
CREATE TABLE IF NOT EXISTS ANALYTICS_READY_SENTIMENT (
    published_at TIMESTAMP,
    company STRING,
    sentiment_score FLOAT,
    topic STRING
)
""")

for article in news_data:
    published_at = article.get("publishedAt")
    analysis = article.get("analysis", {})
    
    # Sometimes analysis contains errors
    if "error" in analysis:
        continue
    
    # Companies can be a list
    companies = analysis.get("Companies mentioned", [])
    if isinstance(companies, str):
        companies = [companies]
    
    for company in companies:
        cs.execute(
            "INSERT INTO ANALYTICS_READY_SENTIMENT (published_at, company, sentiment_score, topic) VALUES (%s, %s, %s, %s)",
            (published_at, company, analysis.get("Sentiment Score"), analysis.get("Primary Topic"))
        )

cs.close()
ctx.close()
print("✅ Data pushed to Snowflake successfully!")