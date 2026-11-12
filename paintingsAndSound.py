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
response = requests.get(url, params=my_data)
response.raise_for_status()
data = response.json()
# print(data)
#gets object ID 
object_id = data['objectIDs'][0]  
# get info about the painting using object ID 
object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
response2 = requests.get(object_url)
painting_data = response2.json()
title = painting_data['title']
artist = painting_data['artistDisplayName']
# print(title)
# print(artist)
# response = requests.get(url, params=my_data)
# response.raise_for_status()

# data = response.json()

# print("Theme:", theme)
# print("Total results:", data["total"])
# print("Object IDs:", data["objectIDs"])

# FREESOUND API SET-UP AND TESTS
with open("keys/service.json", "r") as file:
    keys = json.load(file)

freesound_key = keys["FREESOUND_API_KEY"]

# print("API key works")

# FREESOUND API SEARCH TESTS
url = "https://freesound.org/apiv2/search/text/"

my_params = {
    "query": theme,
    "fields": "id,name,description,previews", #previews makes sure the sound plays 
    "page_size": 5
}

my_headers = {
    "Authorization": f"Token {freesound_key}"
}

response = requests.get(url, params=my_params, headers=my_headers)
data = response.json()

sounds = data["results"]

# im selecting the first sound that comes from the results 
first_sound = sounds[0]

#print name and audio url 
sound_name = first_sound["name"]
sound_url = first_sound["previews"]["preview-hq-mp3"]

print("Sound:", sound_name)
print("Preview URL:", sound_url)
#now we have an audio preview associated with the painting's theme

# this lib lets Python run system commands
import subprocess 

# we need to download the file, check if it downloaded successfully 
audio_response = requests.get(sound_url)
audio_response.raise_for_status()

# Create an MP3 file called preview.mp3
# "wb" means write binary, which is used for audio files
with open("preview.mp3", "wb") as file:
    file.write(audio_response.content)



print("Theme:", theme)
print("Painting:", title)
print("Artist:", artist)
print("Playing sound:", sound_name)

subprocess.run(["afplay", "preview.mp3"])

print("Finished playing!")

