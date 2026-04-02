import sqlite3

# Connect to the SQLite database created in step 2
conn = sqlite3.connect("news_sentiment.db")
c = conn.cursor()

# Show table names
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", c.fetchall())

# Preview the analytics table
c.execute("SELECT * FROM ANALYTICS_READY_SENTIMENT LIMIT 5;")
rows = c.fetchall()
for row in rows:
    print(row)

conn.close()