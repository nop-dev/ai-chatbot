import google.generativeai as genai

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

prompt = input("Escreva seu comando: ")

while prompt != "exit":
    response = chat.send_message(prompt)
    print("Resposta: ", response.text, "\n")
    prompt = input("Escreva seu comando: ")