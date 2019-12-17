import pandas as pd
import numpy as np  
import json
import pathlib


data_path = pathlib.Path.cwd().joinpath('linked-wikitext-2')

def open_jsonl(path):
    with open(path) as f:
        for line in f:
            j_content = json.loads(line)
            yield j_content

def open_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data

data = open_jsonl(data_path.joinpath("test.jsonl"))
for d in data:
    print(d.keys())


# # keys in the dataset: 
# print(f'keys in the json file: {data.keys()}')
# for titl in data.keys
# print(f'for key "title": {data["title"]}')
