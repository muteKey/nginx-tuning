import requests
import json

def seed():
    f = open('../results.json',)
    data = json.load(f)
    results = data['results']

    for i in range(len(results)):
        result = results[i]
        response = requests.get(result['picture']['medium'])
        imageName = f"{i+1}.jpg"
        file = open(imageName, "wb")
        file.write(response.content)
        file.close()
    
if __name__ == "__main__":
    seed()
