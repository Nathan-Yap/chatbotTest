import json
import pandas
import argparse
import math


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--file_name", type=str,
                    help="file name")
args = parser.parse_args()
file = args.file_name

df = pandas.read_csv(file)

df = df.reset_index()  # make sure indexes pair with number of rows

data = []

for index, row in df.iterrows():
    tag = row['Tag']
    patterns = row['Patterns']
    responses = row['Responses']

    try:
        patterns = patterns.split(',')
        response = responses.split(',')
        stuff = {"tag": tag, "patterns": patterns, "responses": responses}
        data.append(stuff)
    except AttributeError:
        print("Skipped {}".format(tag))
    output = {"intents": data}

with open("intents.json", 'w') as f:
    json.dump(output, f)

