import json
import os
from agentorg.workers.base import WORKER_REGISTRY

#registering all workers
import agentorg.workers.data_query_worker
import agentorg.workers.data_summary_worker
import agentorg.workers.search_worker

#loading the task plan
def load_task_plan(input_dir):
    task_path = os.path.join(input_dir, "task_plan.json")
    if not os.path.exists(task_path):
        raise FileNotFoundError(f"Missing task_plan.json at {task_path}")
    with open(task_path, "r") as f:
        return json.load(f)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required= True, 
                        help= "Directory with task_plan.json")
    args = parser.parse_args()

    task_plan = load_task_plan(args.input_dir)
    print("Chatbot ready! Type your question, or 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Bot: Goodbye! Have a great day.")
            break

        elif "total" in user_input.lower() or "sales" in user_input.lower():
            print("Bot: Analyzing sales data...")
            query_worker_cls = WORKER_REGISTRY.get("DataQueryWorker")
            summary_worker_cls = WORKER_REGISTRY.get("DataSummaryWorker")

            if not query_worker_cls or not summary_worker_cls:
                print("Bot: Required workers are not registered.")
                continue

            query_worker = query_worker_cls()
            db_result = query_worker.run({
                "query": "SELECT * FROM sales"
            })

            if db_result["status"] != "success":
                print(f"Bot: 🚨 Database query failed: {db_result.get('message')}")
                continue

            summary_worker = summary_worker_cls()
            summary_result = summary_worker.run({
                "data": db_result.get("data", [])
            })

            summary = summary_result.get("summary", {})
            print("\n Sales Summary:")
            print(f"Total Sales: ${summary.get('total_sales', 0):,.2f}")
            print("Sales by Region:")
            for region, amount in summary.get("sales_by_region", {}).items():
                print(f"  - {region}: ${amount:,.2f}")
            print()

        elif "search" in user_input.lower() or "trends" in user_input.lower():
            print("Bot: Searching for trends...")
            search_worker_cls = WORKER_REGISTRY.get("SearchWorker")

            if not search_worker_cls:
                print("Bot: SearchWorker not found in registry.")
                continue

            search_worker = search_worker_cls()
            result = search_worker.run({"query": user_input})

            if result.get("status") == "success":
                results = result.get("results", [])
                if not results:
                    print("Bot: No relevant articles found.")
                    continue

                print("\n Search Results:")
                for i, r in enumerate(results, 1):
                    title = r.get("title", "Untitled")
                    url = r.get("url", "No URL")
                    print(f"{i}. {title} — {url}")
                print()
            else:
                print("Bot: Failed to search Tavily.")

        else:
            print("Bot: I can help with sales summaries or industry trend searches.")
            print("     Try asking: 'What are the total sales?' or 'Search for data analytics trends'\n")

if __name__ == "__main__":
    main()
