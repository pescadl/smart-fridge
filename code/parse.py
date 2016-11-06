import os
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from subprocess import call
import mraa
import time

THRESHOLD = .50

infile = open('Output.txt', 'r')
output = ""

input = {}
input = json.load(infile).get("images")

infile.close()

classes = []
for bigthing in input:
    classes = input.get(bigthing).get("classes")
    for desc in classes:
        if desc.get("score") >= THRESHOLD:
            output += '\n' + desc.get("class"))

outfile = open('thingy.txt', 'w')
outfile.write(output)
