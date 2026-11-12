import asyncio
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI
from semantic_kernel import Kernel
from semantic_kernel.contents import ChatHistory
from semantic_kernel.connectors.ai.open_ai import (
    OpenAIChatCompletion,
    OpenAIChatPromptExecutionSettings,
)

load_dotenv()


async def test_groq_connection():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing from the root .env file.")

    print("Initializing Semantic Kernel with Groq...")

    kernel = Kernel()

    client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )

    chat_service = OpenAIChatCompletion(
        service_id="groq_service",
        ai_model_id="openai/gpt-oss-20b",
        async_client=client,
    )

    kernel.add_service(chat_service)

    history = ChatHistory()
    history.add_user_message(
        "Reply with exactly: SmartFulfill AI Groq connection successful!"
    )

    settings = OpenAIChatPromptExecutionSettings()

    print("Sending test message to Groq...")

    response = await chat_service.get_chat_message_contents(
        chat_history=history,
        settings=settings,
    )

    if not response or not response[0].content:
        raise RuntimeError("Groq returned an empty response.")

    print("\nGroq response:")
    print(response[0].content)

    print("\nSUCCESS: Groq is connected through Semantic Kernel!")

    await client.close()


if __name__ == "__main__":
    asyncio.run(test_groq_connection())
