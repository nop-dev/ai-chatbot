import google.generativeai as genai
import textwrap
from IPython.display import display, Markdown

GOOGLE_API_KEY= 'AIzaSyD3i22rqClUTsqZbIUFG0OBZnRXfSq-5zk'
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5
}

safety_settings = {
   "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE"
}

model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)

chat = model.start_chat(history=[])

prompt = input('Esperando prompt: ')

while prompt != "exit":
  response = chat.send_message(prompt)
  print("Resposta:", response.text, '\n\n')

  prompt = input('Escreva seu comando: ')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# for message in chat.history: (disponível apenas para ambiente Jupyter Notebook)
  display(to_markdown(f'**{message.role}**: {message.parts[0].text}'))
  print('-------------------------------------------')
