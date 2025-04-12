# InsightBot

**InsightBot** is an AI-powered, task-oriented chatbot, built using the modular Arklex Agent First Organization framework that helps users:
- Analyze internal sales data from a local database
- Perform real-time industry trend searches using the Tavily API
- Generate summaries via pandas

---

## Features

- Query structured data from SQLite databases  
- Retrieve real-time industry trends from Tavily  
- Modular worker-based design using LangGraph-style agents  

---

## Setup Instructions

### 1. Clone the Project

```bash
git clone https://github.com/your-username/InsightBot-data-analysis-chatbot.git
cd InsightBot-data-analysis-chatbot
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

Add your API keys:

```env
TAVILY_API_KEY=your_tavily_key
```

---

## Build and Run the Bot

### 1. Create a Task Plan

```bash
python create.py --config ./examples/data_analysis_config.json --output-dir ./examples/data_analysis
```
(When prompted, press `s` to save the task plan)

### 2. Run the Chatbot

```bash
python run.py --input-dir ./examples/data_analysis
```

---

## Usage Examples

Once the chatbot starts, you'll see:

```bash
Chatbot ready! Type your question, or 'exit' to quit.
```

### Example 1: Web Search via Tavily

**User:**
```
search for business intelligence trends
```

**Bot:**
```
Bot: Searching for trends...

 Search Results:
1. 12 Top Business Intelligence Trends In 2025 - FAIC Group — https://faicgroup.com/2025/01/12-top-business-intelligence-trends-in-2025/
2. Top 10 Business Intelligence Trends for 2025 - thoughtspot.com — https://www.thoughtspot.com/data-trends/business-intelligence/business-intelligence-trends
3. Top 10 Business Intelligence Trends for 2025 - gleecus.com — https://gleecus.com/blogs/business-intelligence-trends-2025/
4. The future of business intelligence: 10 top trends in 2025 - TechTarget — https://www.techtarget.com/searchBusinessAnalytics/feature/The-future-of-business-intelligence-Top-trends
5. Top 10 Analytics and Business Intelligence Trends For 2025 - RIB Software — https://www.rib-software.com/en/blogs/business-intelligence-trends
```

---

### Example 2: Analyze Sales Data

**User:**
```
what is the total sales amount?
```

**Bot:**
```
Bot: Analyzing sales data...

Sales Summary:
Total Sales: $735.75
Sales by Region:
  - North: $410.50
  - South: $250.00
  - East: $75.25
```

---


## Future Enhancements

- Use GPT to convert natural language into SQL  
- Add matplotlib or Plotly charts for visualization  
- Summarize Tavily results using OpenAI  
- Deploy to Replit, Hugging Face Spaces, or Streamlit  
