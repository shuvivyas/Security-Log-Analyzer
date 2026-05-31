import json
from parser import parse
from detector import detect

logs = []
with open("logs/sample.log", "r", encoding = "utf-8") as file:
    for line in file:
        logs.append(parse(line))
alerts = detect(logs)

with open("alerts_triage.json", "w") as file:
    json.dump(alerts, file, indent=4)
