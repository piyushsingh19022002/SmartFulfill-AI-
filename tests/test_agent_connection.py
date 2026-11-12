import asyncio
import os

from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.contents import ChatHistory
from semantic_kernel.connectors.ai.google.google_ai import (
    GoogleAIChatCompletion,
    GoogleAIChatPromptExecutionSettings,
)


load_dotenv()


async def test_connection():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or api_key == "your_gemini_api_key_here":
        raise ValueError("GEMINI_API_KEY is missing. Check your root .env file.")

    print("Initializing Semantic Kernel...")

    kernel = Kernel()

    chat_service = GoogleAIChatCompletion(
        service_id="gemini_service",
        gemini_model_id="gemini-3.7-flash",
        api_key=api_key,
    )

    kernel.add_service(chat_service)

    print("Sending a test message to Gemini...")

    history = ChatHistory()
    history.add_user_message(
        "Reply with exactly: SmartFulfill AI connection successful!"
    )
    # Gemini requires provider-specific execution settings
    settings = GoogleAIChatPromptExecutionSettings()
    response = await chat_service.get_chat_message_contents(
        chat_history=history,
        settings=settings,
    )

    if not response or not response[0].content:
        raise RuntimeError("Gemini returned an empty response.")

    print("\nGemini response:")
    print(response[0].content)

    print("\nSUCCESS: Gemini responded through the Semantic Kernel connector!")


if __name__ == "__main__":
    asyncio.run(test_connection())
