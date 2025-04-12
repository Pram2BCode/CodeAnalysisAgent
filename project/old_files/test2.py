import google.generativeai as genai
 
genai.configure(api_key="")
model= genai.GenerativeModel(model_name="gemini-2.0-flash")
 
print(model.generate_content("Poem on google!").text)