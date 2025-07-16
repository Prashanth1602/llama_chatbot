# Llama Chatbot

A Streamlit-based AI assistant chatbot powered by Llama models (Groq API or local Ollama), focused on science, technology, innovation, startups, and research & development.

## Features
- Clean, organized, and concise answers
- Supports both cloud (Groq) and local (Ollama) Llama models
- Easy to deploy on Render or run locally
- Environment variable management for API keys

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/Prashanth1602/llama_chatbot.git
cd llama_chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the `app/` directory with your API key:
```
GROQ_API_KEY=your-groq-api-key-here
```
*Do not commit your `.env` file to GitHub!*

### 4. Run locally
```bash
streamlit run app/main.py
```

## File Structure
```
llama_chatbot/
  app/
    chatbot.py
    main.py
    prompts/
      prompt.txt
  requirements.txt
  README.md
```

## Security
- Never commit secrets or API keys to the repository.
- Use environment variables for all sensitive data.

## License
MIT 
