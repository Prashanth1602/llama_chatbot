import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

def get_response(input_text):
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")

    model = ChatGroq(
        model_name='llama3-70b-8192', 
        groq_api_key=groq_api_key,
        max_tokens=1000,
        temperature=0.7
    )    

    prompt_path = os.path.join(os.path.dirname(__file__), 'prompts', 'prompt.txt')
    with open(prompt_path, 'r') as prompt_file:
        prompt_template = prompt_file.read()

    prompt = ChatPromptTemplate.from_messages([
        ("system", prompt_template),
        ("user", "{input_text}")
    ])

    chain = prompt | model

    response = chain.invoke({"input_text": input_text})
    return response.content
