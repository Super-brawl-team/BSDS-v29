import json

class Alliance:
    ID = [0,1]
    Name = "Mr. Whatsit? Gang"
    Thumbnail = 0
    Members = []
    Trophies = 0
    
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))
        
    def fromJSON(self, jsonData):
        for key,data in jsonData.items():
            setattr(self, key, data)