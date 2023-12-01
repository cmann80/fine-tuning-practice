import openai
import json

# Set up the OpenAI API key
openai.api_key = "OPENAI_API_KEY"

# Load the JSON file
with open('your_file.json', 'r') as f:
    data = json.load(f)

# Fine-tune the GPT-3.5 model
model_engine = "text-davinci-002"
model_id = "YOUR_MODEL_ID"
fine_tune_data = [{"prompt": item["generated_prompt"], "completion": item["generated_completion"]} for item in data]
response = openai.Completion.create(
    engine=model_engine,
    prompt=fine_tune_data,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the response
print(response.choices[0].text)
