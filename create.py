import json
import os
from pathlib import Path

def load_config(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_task_plan(task_plan, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    plan_path = os.path.join(output_dir, 'task_plan.json')
    with open(plan_path, 'w') as f:
        json.dump(task_plan, f, indent=2)
    print(f"Task plan saved to {plan_path}")

def generate_task_plan_from_config(config):
    # Normally you'd call an LLM here — let's mock it
    print("Generating task plan from config...")
    return {
        "task_name": config["tasks"][0]["task_name"],
        "steps": config["tasks"][0]["steps"],
        "workers": config["tasks"][0]["workers"]
    }

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, required=True)
    parser.add_argument('--output-dir', type=str, required=True)
    args = parser.parse_args()

    config = load_config(args.config)
    task_plan = generate_task_plan_from_config(config)

    print("Generated Task Plan:")
    print(json.dumps(task_plan, indent=2))

    user_input = input("Press 's' to save this task plan and continue: ")
    if user_input.strip().lower() == 's':
        save_task_plan(task_plan, args.output_dir)
        print("🎉 TaskGraph setup completed.")
    else:
        print("Task plan not saved. Exiting.")

if __name__ == "__main__":
    main()
