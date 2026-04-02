# 📊 News Sentiment vs Stock Performance Analysis

## 🚀 Project Overview

Built an end-to-end data pipeline that analyzes how news sentiment impacts stock price movements. The system ingests real-time news data, applies LLM-based sentiment analysis, and correlates results with stock market performance.

---

## 🧠 Problem Statement

Financial markets are heavily influenced by news events such as product launches, mergers, and announcements. This project answers:

👉 *Does positive or negative news sentiment correlate with stock price movement?*

---

## ⚙️ Architecture

1. **Data Ingestion**

   * Extract news articles using NewsAPI
   * Filter by industry/topic (e.g., AI startups)

2. **LLM Sentiment Analysis**

   * Use local LLM (Ollama - DeepSeek Coder)
   * Generate structured output:

     * Sentiment Score (-1 to 1)
     * Topic (e.g., Product Launch, M&A)
     * Company names

3. **Data Storage**

   * Store raw JSON data in SQLite (`RAW_NEWS_DATA`)
   * Transform into analytics-ready format (`ANALYTICS_READY_SENTIMENT`)

4. **Stock Data Integration**

   * Fetch stock prices using `yfinance`
   * Merge with sentiment data by date and company

5. **Visualization**

   * Tableau dashboard:

     * Line chart → Stock Price
     * Bar chart → Sentiment Score
     * Dual-axis correlation view

---

## 🛠️ Tech Stack

* **Programming:** Python
* **Libraries:** pandas, requests, yfinance
* **LLM:** Ollama (DeepSeek-Coder)
* **Database:** SQLite
* **Visualization:** Tableau Public
* **Workflow Concept:** ELT Pipeline

---

## 📂 Project Structure

```
.
├── news_sentiment_pipeline.py      # Fetch + analyze news using LLM
├── push_to_sqlite.py              # Store data in SQLite
├── export_to_csv.py               # Export structured data
├── merge_sentiment_with_stock.py  # Combine sentiment with stock prices
├── analytics_ready_sentiment.csv
├── merged_sentiment_stock.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```
python3 -m pip install -r requirements.txt
```

### 2. Run news ingestion + sentiment analysis

```
python3 news_sentiment_pipeline.py
```

### 3. Store data in SQLite

```
python3 push_to_sqlite.py
```

### 4. Export structured CSV

```
python3 export_to_csv.py
```

### 5. Merge with stock price data

```
python3 merge_sentiment_with_stock.py
```

---

## 📈 Output

* `analytics_ready_sentiment.csv` → Clean sentiment dataset
* `merged_sentiment_stock.csv` → Final dataset for analysis

---

## 📊 Key Insights

* Positive sentiment events (e.g., product launches) often align with upward stock trends
* Negative sentiment shows weaker or delayed impact
* LLM-based tagging enables automated event classification at scale

---


## 🧑‍💻 Author

**Chirag Venkatesh**
Data Analyst | Data Engineering | GenAI Enthusiast

---

## 🔗 Notes

This project demonstrates practical application of:

* LLMs in data pipelines
* Sentiment analysis for financial insights
* End-to-end data engineering workflow
