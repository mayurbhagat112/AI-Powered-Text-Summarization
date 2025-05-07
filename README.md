# AI-Powered Text Summarizer

This is a simple Streamlit app that uses Google Gemini's generative AI model to summarize input text.

## Features

- Paste or type text to get a concise summary.
- Uses Google Gemini API for summarization.
- Error handling and caching for improved reliability and performance.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
5. Run the app:
   ```
   streamlit run app.py
   ```

## Notes

- The app uses caching to reduce repeated API calls for the same input.
- Errors from the API are displayed in the UI.
