from datetime import datetime
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper

# Use the 'tool' decorator for custom functions
from langchain_core.tools import tool 

# 1. DuckDuckGo Web Search
search_tool = DuckDuckGoSearchRun(
    name="search",
    description="Search the web for recent information and news"
)

# 2. Save Tool (Using the @tool decorator)
@tool
def save_tool(data: str, filename: str = "research_output.txt") -> str:
    """Saves structured research data to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

# 3. Wikipedia Search
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1500)
wiki_tool = WikipediaQueryRun(
    api_wrapper=wiki_wrapper,
    name="wikipedia",
    description="Search Wikipedia for historical and factual information"
)