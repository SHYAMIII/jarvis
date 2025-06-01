# import openai

# # Configure for local Ollama
# openai.api_base = 'http://localhost:11434/v1'
# openai.api_key = 'sk-ollama'  # Dummy key required

# response = openai.ChatCompletion.create(
#     model="tinyllama",
#     messages=[
#         {"role": "system", "content": "your name is jarvis, You're skilled in programming and polite.answer in short as you can"},
#         {"role": "user", "content": "Hello, whats your name?"}
#     ],
#     temperature=0,
#     max_tokens=100
# )

# print(response['choices'][0]['message']['content'])


import google.generativeai as genai

genai.configure(api_key="AIzaSyC0YPn6sFaBzBVgJaKpltQGUng21AF_Dvg")

model = genai.GenerativeModel("gemini-pro")

def aiChat(prompt):
    response = model.generate_content("hii")
    print(response.text.strip())
