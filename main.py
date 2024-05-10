import google.generativeai as genai

GOOGLE_API_KEY= 'AIzaSyD3i22rqClUTsqZbIUFG0OBZnRXfSq-5zk'
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

generation_config = {
    "candidates_count": 1,
    "temperature": 0.5
}

safety_settings = {
   "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE"
}

model - genai.GenerativeModel(model_name="gemini-1.0-pro-", generation_config=generation_config, safety_settings=safety_settings)

response = model.generate_content("Me diga 10 cores diferente")
print(response.text)