import json
import platform

path = ""
if platform.system() == "Linux":
    path = f'/home/config.json'
elif platform.system() == "Windows":
    path = f"config.json"

sampleconf = {
              "port" : 65532,
              "ip" : "192.168.0.2",
              "subnet-range":"1-254-1-254",
              "word-dict" : {"word": "slovo", "question": "otazka", "sentence": "veta", "paragraph": "odstavec", "document": "dokument"}}

with open(path, "w") as file:
    json.dump(sampleconf, file)
