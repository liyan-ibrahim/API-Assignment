import requests
import json
from PIL import Image
from io import BytesIO
# this lib lets Python run system commands
import subprocess 

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
#gets object ID -> this used to always select the first painting but sometimes the url for that would be broken so i need the first correct url instead 
# Go through the first 20 painting IDs
for object_id in data["objectIDs"][:20]:
    # get info about the painting using object ID 
    object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    response2 = requests.get(object_url)
    painting_data = response2.json()
    # checking if the painting has an available image
    if painting_data.get("primaryImage") or painting_data.get("primaryImageSmall"):
        break
else:
    raise Exception("No paintings with images found.")
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

#lets display the image 
image_url = painting_data["primaryImage"] or painting_data["primaryImageSmall"]
print("Image URL:", image_url)



# Download the image from the Met Museum API
image_response = requests.get(image_url)
image_response.raise_for_status()

# Convert the image data into an image
painting_image = Image.open(BytesIO(image_response.content))

# Display the painting
painting_image.show()
print("Playing sound:", sound_name)

subprocess.run(["afplay", "preview.mp3"])

print("Finished playing!")