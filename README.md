🌐 Webpage Summarizer
---------------------
A lightweight Python tool that fetches the content of any webpage and generates a clean, concise summary using Large Language Models (LLMs).

This project demonstrates LLM integration in production-ready Python code, with support for both OpenAI API and Ollama (local LLMs).

✨ Features
-----------
📰 Fetch any webpage (removes HTML clutter, keeps only meaningful text).

🧠 Summarize content using either:

└──OpenAI API (cloud-based LLMs)

└──Ollama (local LLMs like llama3.2) via OpenAI-compatible API.

⚡ Command-line tool for quick summaries:

python summarizer_openai.py --url https://example.com

python summarizer_ollama.py --url https://example.com


🔑 .env support for API keys (only required for OpenAI).

📂 Project Structure
--------------
webpage-summarizer/

── openai_impl/

   └── summarizer_openai.py
   
   └── webpage_fetcher.py
   
── ollama_impl/

   └── summarizer_ollama.py
   
── .env

── requirements.txt

── README.md

🚀 Getting Started
-------------------
1. Clone the repository
   
------>  *git clone https://github.com/your-username/webpage-summarizer.git*

2. Navigate  to root folder
------> *cd webpage-summarizer*

3. Install dependencies
   
------> *pip install -r requirements.txt*

4. Setup .env (for OpenAI only)

------> Create a .env file in the project root:

------> OPENAI_API_KEY=sk-proj-xxxxxxxx

5. Run with OpenAI
   
------->   *python openai_impl/summarizer_openai.py --url https://example.com*

6. Run with Ollama

------->  Make sure Ollama is installed and running:

------->  *ollama run llama3.2*


Then run:

------>  *python ollama_impl.summarizer_ollama.py --url https://example.com*

🧑‍💻 Key Learnings
-----------------
This project was not just about summarizing webpages — it was about learning how to integrate LLMs effectively.

✅ LLM APIs are interchangeable:
By abstracting the fetcher and summarizer, we can swap OpenAI with Ollama seamlessly.

✅ Importance of modular design:
Splitting into webpage_fetcher and summarizer makes the project extensible. Tomorrow, we could add FAISS for long-context retrieval, or another backend like Anthropic.

✅ OpenAI vs Ollama:

OpenAI → great for production-grade accuracy and cloud scalability.

Ollama → best for local experimentation, privacy, and cost-savings.

✅ Error handling & validation:
Learned to validate .env API keys and handle cases like missing/whitespace keys.
