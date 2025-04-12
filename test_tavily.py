import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TAVILY_API_KEY")

print("🔑 Tavily API Key Loaded:", "✅" if api_key else "❌ NOT FOUND")

query = "data analytics trends"

try:
    response = requests.post(
        "https://api.tavily.com/search",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"query": query, "num_results": 3}
    )

    print("🌐 HTTP Status Code:", response.status_code)
    response.raise_for_status()

    data = response.json()
    print("✅ Response JSON:")
    for i, result in enumerate(data.get("results", []), 1):
        print(f"{i}. {result.get('title')} — {result.get('url')}")

except Exception as e:
    print("❌ Error occurred:", e)
