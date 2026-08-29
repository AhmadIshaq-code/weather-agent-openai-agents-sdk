import os
import httpx
from agents import function_tool


@function_tool
async def get_latest_news(query: str) -> str:
    """
    Search for the latest news about a topic.
    """

    api_key = os.getenv("NEWS_API_KEY")

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "apiKey": api_key,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
    }

    headers = {
        "X-Api-Key": api_key
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            params=params,
            headers=headers
        )

    response.raise_for_status()

    data = response.json()

    articles = data.get("articles", [])

    if not articles:
        return f"No recent news found about {query}."

    results = []

    for article in articles:
        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown")
        published = article.get("publishedAt", "Unknown")
        url = article.get("url", "")

        results.append(
            f"Title: {title}\n"
            f"Source: {source}\n"
            f"Published: {published}\n"
            f"URL: {url}"
        )

    return "\n\n".join(results)