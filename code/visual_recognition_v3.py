import os
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from subprocess import call
import mraa
import time

THRESHOLD = .50

def fridgescanner():
    x = mraa.Gpio(26)
    x.dir(mraa.DIR_OUT)
    x.write(255)
    #time.sleep(2)
    call(['./pic'])
    x.write(0)
    outFile = open('Output.txt', 'w')
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key='cf40138eb6764ea300b5fafe571e3369bc4f6ce9')
    
    output = {}
    with open(join(dirname(__file__), 'cpp-headless-output-COLOR.png'), 'rb') as image_file:
        output = visual_recognition.classify(images_file=image_file)
        outFile.write(json.dumps(output, indent=2))
        outFile.close()
    
    
    
    inp = output.get('images')
    inp = inp[0].get('classifiers')
    
    out = []
    
    for group in inp:
        classes = []
        classes = group.get('classes')
        for desc in classes:
            if desc.get('score') >= THRESHOLD:
                out.append(desc.get('class'))
    
    print out
    outfile = open('thingy.txt', 'w')
    outfile.write('\n'.join(out))
