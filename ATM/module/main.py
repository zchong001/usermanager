
import json

with open('json_txt','r') as file:
    # json.dump({"test_json":"ddd"},file)
    d=json.load(file)
    print(d['test_json'])
