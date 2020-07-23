import json
import os

dirPathInput = "./annos"
dirPathOutput = "./result"

listJsonFile = os.listdir(dirPathInput)
for path in listJsonFile:
    with open(os.path.join(dirPathInput, path)) as f:
        data = json.load(f)
    output = dict()
    items = data.items()
    for item in items:
        if type(item[1]) == dict and item[1].get("segmentation"):
            output[item[0]] = {
                "segmentation": item[1]["segmentation"]
            }
    with open(os.path.join(dirPathOutput, path), "w") as f:
        json.dump(output, f)
    print("Done:", path)


