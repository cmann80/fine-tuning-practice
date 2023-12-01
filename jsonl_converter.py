import json

with open('prepareddata.json', 'r') as f:
    data = json.load(f)

with open('prepareddata.jsonl', 'w') as f:
    for obj in data:
        json.dump(obj, f)
        f.write('\n')
