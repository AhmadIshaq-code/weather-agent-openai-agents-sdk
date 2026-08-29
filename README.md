# 🌦️ Weather & News AI Agent

An AI-powered assistant built with the **OpenAI Agents SDK** that can provide weather information and fetch the latest news using external APIs.

The project demonstrates how an AI agent can understand a user's request, decide which tool to use, call external APIs, and return a useful response.

## 🚀 Features

* 🤖 AI Agent powered by OpenAI Agents SDK
* 🌤️ Weather information using an external Weather API
* 📰 Latest news using an external News API
* 🔧 Custom function tools
* 🧠 Agent decides when to use available tools
* 🔐 Environment variables for API key management
* ⚡ Async execution with Python
* 🛠️ Modular project structure
* 🔌 External API integration

## 🧠 How It Works

The basic workflow is:

```text
User
  ↓
AI Agent
  ↓
Understand User Request
  ↓
Choose Appropriate Tool
  ↓
┌─────────────────┐
│                 │
Weather Tool   News Tool
│                 │
↓                 ↓
Weather API     News API
│                 │
└────────┬────────┘
         ↓
    Tool Result
         ↓
    AI Agent
         ↓
   Final Response
```

For example:

```text
User:
"What is the weather in Faisalabad?"

        ↓

AI Agent
        ↓

Weather Tool
        ↓

Weather API
        ↓

Weather Data
        ↓

AI Agent
        ↓

Final Answer
```

## 🛠️ Technologies Used

* Python
* OpenAI Agents SDK
* Groq API
* Weather API
* News API
* python-dotenv
* AsyncIO

## 📁 Project Structure

```text
Weather&News_Agent/
│
├── tools/
│   ├── weather_tool.py
│   └── news_tool.py
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> `.env` is intentionally excluded from GitHub because it contains secret API keys.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AhmadIshaq-code/weather-agent-openai-agents-sdk.git
```

### 2. Open the project

```bash
cd weather-agent-openai-agents-sdk
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_weather_api_key
NEWS_API_KEY=your_news_api_key
```

Never commit the `.env` file to GitHub.

## ▶️ Run the Agent

```bash
python main.py
```

The agent will start processing user requests and use the appropriate tools when required.

## 🔧 Example Requests

### Weather

```text
What's the weather in Faisalabad?
```

```text
Tell me the current temperature in Lahore.
```

### News

```text
What are the latest technology news?
```

```text
Give me the latest news about artificial intelligence.
```

### Combined Request

```text
What's the weather in Islamabad and tell me the latest technology news?
```

The agent can determine which tools are required to answer the request.

## 🎯 Learning Objectives

This project was built to understand and implement important concepts of the **OpenAI Agents SDK**, including:

* Agents
* Models
* Instructions
* Function Tools
* Tool Calling
* External API Integration
* Runner
* Async execution
* Environment Variables
* Agent decision-making
* Modular tool architecture

## 🔮 Future Improvements

Planned improvements include:

* Add more tools
* Add multiple specialized agents
* Implement agent handoffs
* Add guardrails
* Add sessions and memory
* Add tracing and monitoring
* Build a Chainlit interface
* Connect the agent with FastAPI
* Deploy the application to the cloud
* Add authentication
* Add more real-world APIs

## 👨‍💻 Author

**Ahmad Ishaq**

BS Computer Science Student
University of Agriculture Faisalabad

Interested in:

* Agentic AI
* AI Agents
* AI Automation
* Python
* FastAPI
* Generative AI

## ⭐ Project

If you find this project useful, consider giving it a ⭐ on GitHub.
