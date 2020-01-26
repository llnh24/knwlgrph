import pandas as pd
import numpy as np  
import json
import pathlib


data_path = pathlib.Path.cwd().joinpath('linked-wikitext-2')

def open_jsonl(path):
    '''generator for everyline of a json file'''
    with open(path) as f:
        for line in f:
            j_content = json.loads(line)
            yield j_content

def open_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data

data = open_jsonl(data_path.joinpath("train.jsonl"))
for d in data:
    print(d.keys()) # ['title', 'tokens', 'entities', 'nel', 'clusters', 'annotations']
    break


n = 24
for d in data:
    print('Dictionary Structure:')
    print(f'title: {d["title"]}')
    print(f'first {n} tokens: {d["tokens"][:n]}')
    print(f'first {n} entities : {d["entities"][:n]}') # Look up the entities: https://www.wikidata.org/wiki/Q166747
    print(f'first {n-(n-2)} nel: {d["nel"][:n-(n-2)]}')
    print(f'first {n-(n-2)} clusters: {d["clusters"][:n-(n-2)]}')
    print(f'first {n-(n-10)} annotations: {d["annotations"][:n-(n-10)]}')
    break

# Interpretation:
# title: Politics of Croatia, is the entity on wikipedia: https://en.wikipedia.org/wiki/Politics_of_Croatia
# token: the tokens are the words/ signs to normalize the text on the entity on wikipedia
# token: ['@@START@@', 'The', 'politics', 'of', 'Croatia', 'are', 'defined', 'by', 'a', 'parliamentary', ',', 'representative', 'democratic']
# entities: [Q1154532, 1, 4] 1-4 position in the token-list, e.g. "The politics of Croatia" which is wikidata item: Q1154532
# entities: ['Q166747', 8, 9] 8-9 position in the token-list, e.g. "a parliamentary" which is wikidata item: Q166747
# nel: finds the token, start, end and does what? Are the nel alphabetically sorted by token name?
# clusters: ?
# annotations: ID: Q1154532 (link to entity), relation: "@@NEW@@" (probably that it doesnt exist before?)
# annotations: the span [2, 5] is shifted by one to the right compared to the entitises [Q1154532, 1, 4]
