import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.google.google_ai import GoogleAIChatCompletion
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.contents import ChatHistory

# Load environment variables from .env
load_dotenv()


def build_kernel() -> Kernel:
    kernel = Kernel()

    # 1. Register Primary Service: Google Gemini
    gemini_key = os.getenv("GEMINI_API_KEY")
    if gemini_key:
        gemini_service = GoogleAIChatCompletion(
            service_id="gemini",
            gemini_model_id="gemini-3.8-flash",
            api_key=gemini_key,
        )
        kernel.add_service(gemini_service)
        print("[INIT] Registered Primary Service: Google Gemini")

    # 2. Register Fallback Service: Groq
    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key:
        groq_client = AsyncOpenAI(
            api_key=groq_key,
            base_url="https://api.groq.com/openai/v1",
        )
        groq_service = OpenAIChatCompletion(
            service_id="groq",
            ai_model_id="openai/gpt-oss-120b",
            async_client=groq_client,
        )
        kernel.add_service(groq_service)
        print("[INIT] Registered Fallback Service: Groq")

    return kernel


async def generate_with_fallback(kernel: Kernel, prompt: str) -> str:
    chat_history = ChatHistory()
    chat_history.add_user_message(prompt)

    # Order of priority: try Gemini first, fall back to Groq
    provider_priority = ["gemini", "groq"]

    for service_id in provider_priority:
        try:
            service = kernel.get_service(service_id=service_id)
            settings = service.get_prompt_execution_settings_class()(service_id=service_id)

            print(f"[EXEC] Attempting completion via '{service_id}'...")
            response = await service.get_chat_message_contents(
                chat_history=chat_history,
                settings=settings,
            )
            return f"[{service_id.upper()}] {response[0].content}"

        except Exception as e:
            print(f"[FAILOVER] '{service_id}' failed ({type(e).__name__}: {e}). Switching to next provider...")

    raise RuntimeError("All configured LLM providers failed.")


async def main():
    kernel = build_kernel()
    test_prompt = "Reply with exactly three words: SmartFulfill pipeline ready."

    print("\n--- Test 1: Normal Execution (Gemini Primary) ---")
    result = await generate_with_fallback(kernel, test_prompt)
    print(f"Result: {result}")

    print("\n--- Test 2: Simulated Primary Failure (Groq Fallback) ---")
    # Remove gemini temporarily to prove Groq takes over seamlessly
    kernel.remove_service("gemini")
    fallback_result = await generate_with_fallback(kernel, test_prompt)
    print(f"Result: {fallback_result}")


if __name__ == "__main__":
    asyncio.run(main())