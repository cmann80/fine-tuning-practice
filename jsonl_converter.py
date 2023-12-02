import json

with open('linguistics_fine_tuning_set.json', 'r') as f:
    data = json.load(f)

with open('linguistics_fine_tuning_set.jsonl', 'w') as f:
    for obj in data:
        json.dump(obj, f)
        f.write('\n')
