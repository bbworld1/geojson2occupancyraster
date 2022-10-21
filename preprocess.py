import json
import util

data = json.load(open("campus.geojson"))

for c,feature in enumerate(data["features"]):
    if "natural" in feature["properties"] and feature["properties"]["natural"] == "tree":
        coords = feature["geometry"]["coordinates"]
        points = util.create_circle_points(coords, 3)
        print(points)
        data["features"][c]["geometry"] = {
            "type": "Polygon",
            "coordinates": [ points ]
        }

json.dump(data, open("out.geojson", "w"))
