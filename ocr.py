import sys
import json
from PIL import Image
import os
import pytesseract

image = sys.argv[1]
filename = "json/output.json"

f = open(filename, "r+")
data = json.load(f)

def format(img, obj):
        xtop = int(obj["x1"])
        ytop = int(obj["y1"])
        xbot = int(obj["x2"])
        ybot = int(obj["y2"])

        outy = img.crop((xtop, ytop, xbot, ybot))
        #print(name)
        #print("1")
        #outy.show()
        width, height = outy.size
        newOuty = outy.resize((width*2, height*2))
        name = pytesseract.image_to_string(newOuty)
        #newOuty.show()
        #print(button)
        obj["name"] = name

for i in data:
        format(Image.open(image), i)

#print("test")
#pytesseract.image_to_string(Image.open(outy))
#print("testover")
n = open(filename, 'w')
n.write(json.dumps(data))
