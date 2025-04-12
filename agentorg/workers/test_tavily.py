import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TAVILY_API_KEY")

response = requests.post(
    "https://api.tavily.com/search",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"query": "data analytics trends", "num_results": 3}
)

print(response.status_code)
print(response.json())