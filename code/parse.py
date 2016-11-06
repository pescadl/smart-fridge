import os
import json

THRESHOLD = .50

infile = open('Output.txt', 'r')
outfile = open('thingy.txt', 'w')

input = {}
input = json.load(infile).get("images")

infile.close()

classes = []
for bigthing in input:
    classes = input.get(bigthing).get("classes")
    for desc in classes:
        if desc.get("score") >= THRESHOLD:
            outfile.append(desc.get("class"))

outfile.close()
