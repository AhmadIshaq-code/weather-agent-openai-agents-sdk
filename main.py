import os
import asyncio
from dotenv import load_dotenv

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

from tools.weather import get_weather
from tools.news import get_latest_news


load_dotenv()

set_tracing_disabled(True)


# -------------------------
# Groq Configuration
# -------------------------

groq_client = AsyncOpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


model = OpenAIChatCompletionsModel(
    model="openai/gpt-oss-20b",
    openai_client=groq_client,
)


# -------------------------
# Agent
# -------------------------

agent = Agent(
    name="Personal Information Agent",

    instructions="""
    You are a helpful personal information assistant.

    You have two tools:

    1. get_weather
       Use this when the user asks about current weather.

    2. get_latest_news
       Use this when the user asks for current or latest news.

    Always use the appropriate tool when current external
    information is required.

    Do not invent current weather or news information.
    """,

    model=model,

    tools=[
        get_weather,
        get_latest_news,
    ],
)


async def main():

    result = await Runner.run(
        agent,
        "Give me the latest news about artificial intelligence."
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())



https://github.com/AhmadIshaq-code/weather-news-agent-openai-agents-sdk.git