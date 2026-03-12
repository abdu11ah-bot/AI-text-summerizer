# 🤖 AI Text Summarizer (Day 18 – Project Alpha)

An AI-powered automation tool that reads a text file, sends the content to a language model via the OpenRouter API, and generates a concise summary.

This project is part of my **Project Alpha – AI & Automation Engineer Roadmap**, where I build real-world automation tools step by step.

---

## 🚀 Features

* 📄 Reads text from an input file
* 🧠 Sends content to an AI model
* ✨ Generates a short summary
* 💾 Saves the summary to a file
* 🔐 Uses environment variables to protect API keys

---

## 📂 Project Structure

```
ai_summarizer
│
├── summarizer.py        # Main script
├── input.txt            # Text file to summarize
├── summary.txt          # Generated summary
├── requirements.txt     # Project dependencies
└── .env                 # API key (not uploaded to GitHub)
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/abdu11ah-bot/day18-ai-summarizer.git
cd day18-ai-summarizer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables

Create a `.env` file in the project folder:

```
OPENROUTER_API_KEY=your_api_key_here
```

You can get a free API key from:

https://openrouter.ai

---

## ▶️ Usage

Run the script:

```
python summarizer.py
```

The program will:

1. Read text from `input.txt`
2. Send it to the AI model
3. Generate a summary
4. Save the output to `summary.txt`

---

## 🧪 Example

### Input (`input.txt`)

```
Python is a popular programming language used for automation,
artificial intelligence, web development, and data science.
It is known for its simplicity and large ecosystem.
```

### Output (`summary.txt`)

```
Python is a versatile programming language widely used in automation,
artificial intelligence, and data science. Its simple syntax and
large ecosystem make it popular among developers.
```

---

## 🛠 Technologies Used

* Python
* OpenRouter API
* OpenAI Python SDK
* dotenv (environment variable management)

---

## 📈 Learning Goals

This project helped me learn:

* How to integrate **AI APIs with Python**
* Sending prompts to **large language models**
* Automating text processing
* Managing **API keys securely**
* Building small **AI-powered tools**

---

## 🔮 Future Improvements

* CLI support (`python summarizer.py file.txt`)
* Web interface using Flask or FastAPI
* Support for multiple documents
* Adjustable summary length

---

## 👨‍💻 Author

**Abdullah Al Mamun**

CSE Undergraduate | Aspiring AI & Automation Engineer

GitHub:
https://github.com/abdu11ah-bot

---

⭐ If you find this project useful, consider giving the repository a star!
