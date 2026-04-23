# AI Research Agent 🤖🔎

An intelligent, autonomous research assistant built with modern **LangChain**, **Google Gemini**, and **Pydantic**. 

This agent takes a user query, decides which tools to use to gather information, synthesizes the findings, and outputs a perfectly formatted, typed JSON object. It also automatically logs the output to a local text file for your records.

## Features
- **Modern Agent Architecture:** Built using LangChain's latest `create_agent` ecosystem.
- **Autonomous Tool Routing:** The AI decides when to search the web or when to check Wikipedia.
- **Structured Outputs:** Enforces strict JSON formatting using `PydanticOutputParser`.
- **Custom Tools:** Includes a built-in tool using the `@tool` decorator to save research data locally.

## Tools Included
1. **DuckDuckGo Search:** For real-time web browsing and recent news.
2. **Wikipedia:** For deep-dives into historical, factual, and encyclopedic data.
3. **Local Saver:** A custom Python tool that the agent uses to write its findings to `research_output.txt`.

## Installation & Setup

1. **Clone the repository:**
Code output
README.md and .gitignore generated successfully.

```bash
   git clone [https://github.com/your-username/ai-research-agent.git](https://github.com/your-username/ai-research-agent.git)
   cd ai-research-agent
```
Create a virtual environment:

```
python -m venv venv
```
# On Windows:
```
.\\venv\\Scripts\\activate
```
# On Mac/Linux:
```
source venv/bin/activate
```
Install the dependencies:
```Bash
pip install langchain langchain-core langchain-google-genai langchain-community duckduckgo-search wikipedia pydantic python-dotenv
```
Set up your Environment Variables:
Create a .env file in the root directory and add your Google Gemini API key:
Code snippet
```
GOOGLE_API_KEY="your_google_gemini_api_key_here"
```
💻 Usage
Run the main application script:

```Bash
python main.py
```
You will be prompted: What can I help you research today?

Enter your topic (e.g., “Tell me about the history of quantum computing”).

The agent will "think", pull data from the internet, parse it into a structured Pydantic object, and save the result to research_output.txt.

📁 File Structure
main.py - The core agent initialization, prompt templates, and execution loop.

tools.py - Contains the configured DuckDuckGo, Wikipedia, and Custom File Saver tools.

.env - (Ignored by Git) Stores your API credentials securely.

research_output.txt - (Generated) The output log where the AI saves its research.

🛑 Handling Rate Limits (Free Tier)
If you are using the free tier of Google AI Studio, you may encounter a 429 RESOURCE_EXHAUSTED error. This is normal, as the free tier is limited to 15 Requests Per Minute (RPM).

Fix: Wait 60 seconds before running your next query, or add a billing account in Google AI Studio to lift the limits.
