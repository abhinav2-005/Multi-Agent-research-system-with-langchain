# Multi-Agent-research-system-with-langchain
<img width="1917" height="850" alt="image" src="https://github.com/user-attachments/assets/cc112c9b-ceb5-489d-88a1-fda5ebc586ab" />

An AI-powered research assistant that uses multiple agents to search the web, retrieve detailed information, generate a research report, and review the generated report.

## 🚀 Features

* 🔎 Searches the web for recent and reliable information
* 📖 Scrapes relevant web pages for deeper information
* ✍️ Generates a structured research report
* 🧐 Reviews the generated report using an AI critic
* 🌐 Streamlit web interface
* 📥 Download the generated research report

## 🤖 Multi-Agent Workflow

The application follows a four-step research pipeline:

```text
Research Topic
      ↓
🔎 Search Agent
      ↓
📖 Reader Agent
      ↓
✍️ Writer
      ↓
🧐 Critic
      ↓
Final Research Report
```

### 1. Search Agent

The search agent uses the Tavily search tool to find recent, reliable information about the given topic.

### 2. Reader Agent

The reader agent selects a relevant URL from the search results and uses a web scraping tool to retrieve deeper content.

### 3. Writer

The writer uses the collected search results and scraped content to generate a structured research report containing:

* Introduction
* Key Findings
* Conclusion
* Sources

### 4. Critic

The critic reviews the generated report and provides:

* Score
* Strengths
* Areas to Improve
* One-line verdict

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* Mistral AI
* Tavily
* BeautifulSoup
* Requests
* python-dotenv

## 📁 Project Structure

```text
AI-Research-Agent/
│
├── app.py
├── pipeline.py
├── agents.py
├── tools.py
├── .env
└── README.md
```

## 🔑 API Keys

Create a `.env` file in the project directory.

```env
TAVILY_API_KEY=your_tavily_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

Do not upload your `.env` file or API keys to GitHub.

## 📦 Installation

Install the required dependencies:

```bash
pip install streamlit langchain langchain-core langchain-mistralai tavily-python python-dotenv beautifulsoup4 requests rich
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

Enter a research topic such as:

```text
Impact of Generative AI on Education
```

and click **Start Research**.

## 📊 Output

The application displays:

1. Search results
2. Retrieved web content
3. Generated research report
4. AI critic review

The final research report can also be downloaded as a `.txt` file.

## 🧠 Model

The project uses the Mistral model:

```text
mistral-small-2603
```

The model is used by the search agent, reader agent, writer chain, and critic chain.

## 🔧 Tools

### Web Search

The Tavily-powered search tool searches for recent information and returns titles, URLs and snippets.

### URL Scraper

The URL scraper uses Requests and BeautifulSoup to retrieve and clean webpage content before passing it to the research pipeline.

## 📚 Research Report Structure

The writer generates reports with the following structure:

```text
Introduction

Key Findings
- Finding 1
- Finding 2
- Finding 3

Conclusion

Sources
- URLs
```

## 🎯 Purpose

This project demonstrates how multiple AI agents and tools can be combined into a single research workflow where different components are responsible for searching, reading, writing and reviewing information.

```
```

