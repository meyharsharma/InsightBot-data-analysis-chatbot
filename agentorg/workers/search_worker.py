from agentorg.workers.base import BaseWorker, register_worker
import requests
import os

from dotenv import load_dotenv
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

@register_worker
class SearchWorker(BaseWorker):
    def run(self, task_input: dict):
        query = task_input.get("query", "data analysis trends")
        try:
            response = requests.post(
                "https://api.tavily.com/search",
                headers={"Authorization": f"Bearer {TAVILY_API_KEY}"},
                json={"query": query, "num_results": 3}
            )
            response.raise_for_status()
            data = response.json()

            #print("Tavily Raw Response:", data)  #debug print

            return {
                "status": "success",
                "results": data.get("results", [])
            }
        except Exception as e:
            print("Tavily API error:", e) 
            return {"status": "error", "message": str(e)}