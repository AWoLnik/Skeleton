#!/bin/bash
IMAGE=$1

./darknet detector test cfg/obj.data cfg/yolo-obj.cfg yolo-obj_1100.weights $IMAGE
python ocr.py $IMAGE
java -jar Render.jar json/output.json
