'''
fileName:CS1122hw2.py
Programmer: Yohann Abittan
netid: yaa243
'''

import string
import urllib2
import json
import random


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def imageMaker():
    nameOfUser = raw_input("what is your name?")
    sizeOfImage = (240,270)
    nameFont = ImageFont.truetype("Arial.ttf",20)
    color = "#%06x" % random.randint(0,0xFFFFFF)
    newImage = Image.new("RGB", sizeOfImage, (0,0,0))

    coordinatesFace = (30,30,210,210)
    coordinatesRightEye = (170,90,180,100)
    coordinatesLeftEye = (60,90,70,100)
    coordinatesMouth = [(110,130),(180,140)]
    draw = ImageDraw.Draw(newImage)

    draw.rectangle(coordinatesFace,color)

    draw.ellipse(coordinatesRightEye,(250,250,250))

    draw.ellipse(coordinatesLeftEye,(250,250,250))

    draw.arc(coordinatesMouth, 10,170,(250,250,250))

    draw.text((90,240),nameOfUser,(128,128,128),nameFont)

    newImage.save("testImage","JPEG")
    print("The image has been created")

def readJsonFromURL():
    opener = urllib2.build_opener()

    request = urllib2.Request("http://elections.huffingtonpost.com/pollster/api/charts/2016-national-gop-primary")
    
    dataFile = opener.open(request)

    jsonFile = json.loads(dataFile.read())

    for index in jsonFile["estimates"]:

        if index['first_name'] != None:

            print(index['first_name'] + "  " + index['last_name'] + " : " + str(index['value']))
        else:
            print(index['choice'] + " : " + str(index['value']))

def main():
    imageMaker()
    print("_____________")
    readJsonFromURL()


if __name__ == "__main__":
    main()

