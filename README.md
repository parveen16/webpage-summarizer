📰 Webpage Summarizer

A lightweight Python tool that fetches any webpage, cleans the noise (ads, scripts, navigation menus), and generates a concise AI-powered summary in markdown.

Built with:

🌐 Requests + BeautifulSoup → Fetch and parse webpages

🤖 OpenAI GPT-4o-mini → Generate high-quality summaries

⚙️ Python + CLI → Simple and flexible command-line interface

🚀 Features

✅ Fetches webpage content and extracts only readable text

✅ Removes irrelevant HTML tags (scripts, styles, images, inputs)

✅ Uses AI to generate short, markdown-friendly summaries

✅ Simple CLI interface → run with just --url

✅ Modular design (separates fetcher and summarizer for reusability)

⚡ Installation

#Clone this repository:

git clone https://github.com/your-username/webpage-summarizer.git

cd webpage-summarizer


#Install dependencies:

pip install -r requirements.txt


Create a .env file in the root directory and add your OpenAI API key:

OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxx

🖥️ Usage

Run the summarizer with a URL:

python openai_impl/summarizer.py --url "https://cnn.com"


Output:

=== Summary ===

 CNN News Highlights
- Breaking news coverage on global events
- Featured sections on politics, economy, and tech
- Live updates with multimedia content

🛠️ Tech Stack

Python (CLI and modular design)

Requests + BeautifulSoup (web scraping & cleaning)

OpenAI GPT-4o-mini (AI summarization)

dotenv (API key management)
