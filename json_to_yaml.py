import json
import yaml

yml_data = []
with open('songs.json') as json_file:
    data = json.load(json_file)
    for item in data['items']:
        artists = [artist['name'] for artist in item['track']['artists']]
        artists_str = ", ".join(artists)
        track = {
            "name": item['track']['name'],
            "id": item['track']['id'],
            "artists": artists_str
        }
        yml_data.append(track)

with open(r'songs.yml', 'w') as file:
    yaml.dump(yml_data, file)