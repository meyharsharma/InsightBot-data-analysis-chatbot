from agentorg.workers.base import BaseWorker, register_worker
import sqlite3

@register_worker
class DataQueryWorker(BaseWorker):
    def run(self, task_input: dict):
        query = task_input.get("query", "SELECT * FROM sales LIMIT 5")
        try:
            conn = sqlite3.connect("data/sales.db")  # or your DB
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            return {"status": "success", "data": results}
        except Exception as e:
            return {"status": "error", "message": str(e)}