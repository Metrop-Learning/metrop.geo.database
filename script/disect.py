# Metrop : MIT License
# This script is used to cut geojson in smaller part
# Not commplete

import json

folder = input("Please enter the folder path :")

file = input("Please enter the file name :")

with open(folder + "/" +file, "r", encoding="utf-8") as f:
    data = json.load(f)

for i, feature in enumerate(data["features"], start=1):
    one_province = {
        "type": "FeatureCollection",
        "features": [feature]
    }

    if "province_name" in feature["properties"]:
        name = feature["properties"]["province_name"].replace(" ", "_")
    else:
        name = "temp_" + str(i)
    with open(f"{folder}/{name}.geojson", "w", encoding="utf-8") as out:
        json.dump(one_province, out, indent=2, ensure_ascii=False)