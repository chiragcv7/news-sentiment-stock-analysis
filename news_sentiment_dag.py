import requests
import json
from newsapi import NewsApiClient

# ----------------------------
# CONFIG
NEWSAPI_KEY = "YOUR_NEWSAPI_KEY"   # replace with your key
OLLAMA_URL = "http://localhost:11434/v1/completions"
MODEL = "deepseek-coder"
# ----------------------------

def fetch_and_analyze_news():
    newsapi = NewsApiClient(api_key=NEWSAPI_KEY)
    
    # Fetch top 5 news articles for your chosen industry
    top_headlines = newsapi.get_everything(q='AI startup', language='en', page_size=5)
    
    results = []
    
    for article in top_headlines['articles']:
        text = article['title'] + ". " + (article.get('description') or "")
        
        # Send to deepseek-coder
        payload = {
            "model": MODEL,
            "prompt": f"Extract the following from this text: {text}\n1. Sentiment Score (-1 to 1)\n2. Primary Topic (e.g., 'M&A', 'Product Launch')\n3. Companies mentioned\nReturn as JSON only.",
            "max_tokens": 300
        }
        
        response = requests.post(OLLAMA_URL, json=payload).json()
        model_text = response["choices"][0]["text"]
        
        try:
            model_json = json.loads(model_text)
        except:
            model_json = {"error": "Could not parse JSON", "raw": model_text}
        
        results.append({
            "publishedAt": article['publishedAt'],
            "title": article['title'],
            "url": article['url'],
            "analysis": model_json
        })
    
    # Save to file for later use (or for Snowflake upload)
    with open("news_sentiment_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("Pipeline complete! Results saved to news_sentiment_results.json")

# Run pipeline
if __name__ == "__main__":
    fetch_and_analyze_news()