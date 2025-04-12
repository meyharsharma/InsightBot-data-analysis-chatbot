from agentorg.workers.base import BaseWorker, register_worker
import pandas as pd

@register_worker
class DataSummaryWorker(BaseWorker):
    def run(self, task_input):
        data = task_input.get("data", [])
        df = pd.DataFrame(data, columns=["id", "amount", "region", "timestamp"])
        summary = {
            "total_sales": df["amount"].sum(),
            "sales_by_region": df.groupby("region")["amount"].sum().to_dict()
        }
        return {"status": "success", "summary": summary}