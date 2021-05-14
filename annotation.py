import os
import json

path = "D:/Git/NDDS Generated/TestCapturer"
respath = os.path.abspath('') + "\\annotations.csv"

result = open(respath, 'w')

files = os.listdir(path)
for file in files:
    if file.endswith(".cs.png"):
        number = file.replace(".cs.png", "")
        jsonpath = f"{path}/{number}.json"
        if os.path.exists(jsonpath):
            data = json.load(open(jsonpath, 'r'))
            image_path = f"{path}/{number}.png"
            if len(data["objects"]) > 0:
                bbox = data["objects"][0]["bounding_box"]

                x1 = round(bbox["top_left"][0])
                y1 = round(bbox["top_left"][1])
                x2 = round(bbox["bottom_right"][0])
                y2 = round(bbox["bottom_right"][1])
                type = "sofa"
                mask_path = f"{path}/{file}"
                
                line = f"{image_path},{x1},{y1},{x2},{y2},{type},{mask_path}\n"
                result.write(line)
            else:
                line = f"{image_path},,,,,,\n"
                result.write(line)
                
result.close()