import os
from google import generativeai
from google import genai
from dotenv import load_dotenv

# Explicitly load the .env file from the config directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../config/.env'))

# Configure the generative AI client using the API key from the .env file
api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    raise ValueError("API key not found in the .env file.")
    
# genai.configure(api_key=api_key)

# # Initialize the client for the generative AI service
# client = genai.Client()

# # Generate content using the specified model and prompt
# response = client.models.generate_content(
#     model="gemini-2.0-flash",  # Specify the model version
#     contents="Explain math"     # Specify the content or prompt to be generated
# )

# # Print the generated content
# print(response)

from google import genai

client = genai.Client(api_key="AIzaSyCfPp7nSVRvHd4gbehMCoPZ_oWmXjDPc5s")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)