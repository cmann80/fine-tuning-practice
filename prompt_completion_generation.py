import pandas as pd

# Load the CSV file
df = pd.read_csv('language-families.csv')

# Generate the prompts and completions
df['generated_prompt'] = df['Language'].apply(lambda x: f"Which language family does {x} belong to?")
df['generated_completion'] = df.apply(lambda x: f"{x['Family']}, {x['Branch']}", axis=1)

# Add two new columns in the original data called "generated_prompt" and "generated_completion"
df['generated_prompt'] = df['generated_prompt']
df['generated_completion'] = df['generated_completion']

# Save the modified dataframe to a new CSV file called "prepareddata.csv"
df.to_csv('prepareddata.csv', index=False)

# Select only the 'generated_prompt' and 'generated_completion' columns
df = df[['generated_prompt', 'generated_completion']]

# Convert the dataframe to a JSON object
json_obj = df.to_json(orient='records')

# Save the JSON object to a new file called "prepareddata.json"
with open('prepareddata.json', 'w') as f:
    f.write(json_obj)