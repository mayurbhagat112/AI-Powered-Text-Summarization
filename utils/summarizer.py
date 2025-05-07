import logging
from config.gemini_config import client
from functools import lru_cache
from google.api_core.exceptions import GoogleAPICallError, RetryError

logger = logging.getLogger(__name__)

@lru_cache(maxsize=128)
def summarize_text(text: str) -> str:
    """
    Sends a prompt to Google Gemini via the GenAI client and returns the summary.
    Adds error handling, logging, and caching.
    """
    if not text.strip():
        logger.warning("Empty text provided to summarize_text")
        return "Error: No text provided for summarization."

    prompt = (
        "Summarize the following text in a concise paragraph:\n\n"
        f"{text}\n\n"
        "Provide only the summary without additional commentary."
    )
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        summary = response.text.strip()
        if not summary:
            logger.error("Empty summary received from API")
            return "Error: Received empty summary from the API."
        logger.info("Summary generated successfully")
        return summary
    except (GoogleAPICallError, RetryError) as e:
        logger.error(f"API call failed: {e}")
        return f"Error: Failed to generate summary due to API error."
    except Exception as e:
        logger.error(f"Unexpected error in summarize_text: {e}")
        return "Error: An unexpected error occurred during summarization."
