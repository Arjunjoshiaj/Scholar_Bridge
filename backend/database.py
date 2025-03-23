import json

def get_scholarships():
    with open("data/scholarships.json", "r") as file:
        scholarships = json.load(file)
    return scholarships
