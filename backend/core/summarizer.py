"""
Module for extracting and processing Terms & Conditions content from URLs.
"""
from openai import OpenAI
from backend.config.settings import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE, TOP_P, STORE, MAX_OUTPUT_TOKENS, SYS_PROMPT
from backend.core.extractor import TextExtractor

class TCSummarizer:
    def __init__(self):
        self.extractor = TextExtractor()
        self.client = OpenAI(api_key=OPENAI_API_KEY)
    def summarize(self, url: str) -> str:
        text = self.extractor.extract_from_url(url)
        response = self.client.responses.create(
                    model=MODEL_NAME,
                    input=[                 
                {"role": "system", "content": SYS_PROMPT}    ,
                # only take first 50000 characters
                {"role": "user", "content": text[:50000]} ],
                    reasoning={},
                    tools=[],
                    temperature=TEMPERATURE,
                    max_output_tokens=MAX_OUTPUT_TOKENS,
                    top_p=TOP_P,
                    store=STORE
            )
             
        return response.output_text

if __name__ == "__main__":
    summarizer = TCSummarizer()