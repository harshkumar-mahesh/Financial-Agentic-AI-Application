from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Define Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Define Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Create Multi-Agent Team
multi_ai_agent = Agent(
    name="Coordinator Agent",
    role="Route the user's query to the appropriate specialized agent and return the results clearly.",
    team=[web_search_agent, finance_agent],
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    instructions=[
        "If the question is about stocks, analyst recommendations, or financials, route to Finance AI Agent.",
        "If the question requires general web information or real-time updates, route to Web Search Agent.",
        "Always include sources. Format results clearly."
    ],
    show_tool_calls=True,
    markdown=True
)

# Simple CLI Chatbot
print("🤖 Welcome to the Financial Agentic AI Chatbot!")
print("Type your query or type 'exit' to quit.")
print("=" * 60)

while True:
    user_input = input("🧑 You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    print("🤖 Agent is thinking...\n")
    try:
        multi_ai_agent.print_response(user_input, stream=True)
    except Exception as e:
        print(f"⚠️ Error: {e}")
