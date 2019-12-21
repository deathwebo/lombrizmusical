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

if os.environ.get('APP_LOCATION') == 'dokku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
