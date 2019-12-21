import random
import yaml

from bottle import route, run, template

@route('/')
def tracks():
    with open(r'songs.yml') as file:
        all_tracks = yaml.load(file, Loader=yaml.FullLoader)
        tracks = random.sample(all_tracks, 5)
    return template('templates/tracks', tracks=tracks)

@route('/<track_id>')
def track(track_id):
    with open(r'songs.yml') as file:
        tracks = yaml.load(file, Loader=yaml.FullLoader)
        track = [track for track in tracks if track['id'] == track_id]
    return template('templates/track', track=track[0])

run(host='localhost', port=8080, debug=True)
