import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from webpage_fetcher import Website
# Keep the fetching/cleaning logic separate

# Load API key from .env
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No API key found. Check your .env file.")
elif not api_key.startswith("sk-proj-"):
    raise ValueError("API key does not start with sk-proj-.")
elif api_key.strip() != api_key:
    raise ValueError("API key has leading/trailing whitespace.")

openai = OpenAI()

# System prompt for LLM behavior
system_prompt = (
    "You are an assistant that analyzes the contents of a website "
    "and provides a short summary, ignoring text that might be navigation related. "
    "Respond in markdown."
)

# Prepare user message
def user_prompt_for(website: Website) -> str:
    prompt = f"You are looking at a website titled {website.title}\n"
    prompt += "The contents of this website is as follows; please provide a short summary in markdown.\n\n"
    prompt += website.text
    return prompt

def messages_for(website: Website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

# Summarization function
def summarize(url: str) -> str:
    website = Website(url)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_for(website)
    )
    return response.choices[0].message.content

# Main entry point
def main():
    parser = argparse.ArgumentParser(description="Webpage Summarizer using OpenAI")
    parser.add_argument("--url", required=True, help="URL of the webpage to summarize")
    args = parser.parse_args()

    summary = summarize(args.url)
    print("\n=== Summary ===\n")
    print(summary)

if __name__ == "__main__":
    main()