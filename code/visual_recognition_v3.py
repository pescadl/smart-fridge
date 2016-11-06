import os
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from subprocess import call
import mraa
import time

#x = mraa.Gpio(103)
#x.dir(mraa.DIR_OUT)
#x.write(1)
call(["./pic"])
#x.write(0)
outFile = open('Output.txt', 'w')
visual_recognition = VisualRecognitionV3('2016-05-20', api_key='cf40138eb6764ea300b5fafe571e3369bc4f6ce9')
with open(join(dirname(__file__), 'cpp-headless-output-COLOR.png'), 'rb') as image_file:
	outFile.write(json.dumps(visual_recognition.classify(images_file=image_file), indent=2))
	outFile.close()
