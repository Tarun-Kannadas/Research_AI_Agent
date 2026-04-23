from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from langchain_core.exceptions import OutputParserException

# Import your custom tools from tools.py
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

system_prompt = f"""You are a research assistant that will help generate a research paper.
Answer the user query and use necessary tools.
Wrap the output in this format and provide no other text:
{parser.get_format_instructions()}
"""

# Load both tools
tools = [search_tool, wiki_tool, save_tool]

agent = create_agent(
    model=llm, 
    tools=tools, 
    system_prompt=system_prompt
)

# Dynamic input prompt
print("========================================")
user_query = input("What can I help you research today?\n> ")

print("\nThinking...")

# Pass the dynamic user_query into the messages
raw_response = agent.invoke({
    "messages": [("user", user_query)]
})

final_output = raw_response["messages"][-1].content

print("\n--- RAW TEXT OUTPUT ---")
print(final_output)

try:
    structured_response = parser.parse(final_output)

    print("\n--- STRUCTURED PYDANTIC OBJECT ---")
    print(type(structured_response))
    print(f"Topic: {structured_response.topic}")
    print(f"Summary: {structured_response.summary}")
    print(f"Sources: {structured_response.sources}")
    print(f"Tools Used: {structured_response.tools_used}")
    
except OutputParserException as e:
    print("\n[!] Parsing Error: The AI did not return a valid JSON format.")
    print(f"Error Details: {e}")
    print(f"\n--- The Raw Text That Failed ---\n{final_output}")
    
except Exception as e:
    print(f"\n[!] An unexpected system error occurred: {e}")