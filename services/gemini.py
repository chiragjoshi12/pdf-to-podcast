import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def call_gemini(prompt: str, system_message: str, history:list):
    """
    Generate a dialogue using the Gemini API.
    """
    generation_config = {
        "temperature": 0.8,
        "top_p": 0.9,
        "top_k": 40,
        "max_output_tokens": 8192,
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=system_message
    )
    
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(prompt)
    
    return response.text

def upload_to_gemini(path, mime_type=None):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file