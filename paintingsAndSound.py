import requests
import json

#I added these after testing my MET API was tested and it works - these are used to set a theme
theme = "Ocean"

#MET API SET-UP AND TESTS 
url = "https://collectionapi.metmuseum.org/public/collection/v1.1/search"

my_data = {
    "q": theme,
    "hasImages": "true",
    "medium": "Paintings",
    "limit": 20
}
response = requests.get(url, data=my_data)
data = response.json()
# print(data)
#gets object ID 
object_id = data['objectIDs'][0]  
# get info about the painting using object ID 
object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
response2 = requests.get(object_url)
data=response2.json()
title=data['title']
artist=data['artistDisplayName']
# print(title)
# print(artist)

# FREESOUND API SET-UP AND TESTS
with open("keys/service.json", "r") as file:
    keys = json.load(file)

freesound_key = keys["FREESOUND_API_KEY"]

print("API key loaded successfully!")


response = requests.get(url, params=my_data)
response.raise_for_status()

data = response.json()

print("Theme:", theme)
print("Total results:", data["total"])
print("Object IDs:", data["objectIDs"])