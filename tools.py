from langchain.tools import tool
from dotenv import load_dotenv
from tavily import TavilyClient
from bs4 import BeautifulSoup
from rich import print
import os
import requests

load_dotenv()
tavily_api_key = os.getenv("TAVILY_API_KEY")
tavily = TavilyClient(api_key = tavily_api_key)

@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets."""
    tavily_results = tavily.search(query = query , max_results= 5)

    tavliiy_response = []

    for res in tavily_results['results']:
        tavliiy_response.append(
        f"Title: {res['title']}\nURL: {res['url']}\nSnippet: {res['content'][:300]}\n")


    return "\n----\n".join(tavliiy_response)


@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"