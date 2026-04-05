import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

tavily_key = os.getenv("TAVILY_API_KEY")



def tavily_search(query):
    """
    Placeholder function for Tavily search.

    Args:
        query (str): The search query.

    Returns:
        str: search results joined with '.join()' method.

    """

    tool = TavilySearch(
        tavily_api_key=tavily_key,
        max_results=5
    )

    search_results = tool.invoke({"query": query})

    return "\n\n".join([result['content'] for result in search_results['results']])