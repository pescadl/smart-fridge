import os
import json
from os.path import join, dirname
from os import environ
from subprocess import call
import time

THRESHOLD = .50

infile = open('Output.txt', 'r')
output = [] 

inp = [] 
inp = json.load(infile).get("images")

infile.close()

classes = []

inp = inp[0].get("classifiers")

for group in inp:
    classes = []
    classes = group.get("classes")
    for desc in classes:
        if desc.get('score') >= THRESHOLD:
            output.append(desc.get("class"))

outfile = open('thingy.txt', 'w')
outfile.write('\n'.join(output))
