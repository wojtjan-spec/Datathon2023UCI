import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
from flask import Flask, render_template

# Define emotion-to-genre mapping
emotion_to_genre = {
    'happy': ['pop', 'dance'],
    'sad': ['sad', 'acoustic'],
    'angry': ['rock', 'metal'],
    'relaxed': ['ambient', 'chill'],
    'anxious': ['electronic', 'indie'],
    'energetic': ['edm', 'hip-hop'],
    'romantic': ['love', 'slow'],
}

# Define emotion weights
emotion_weights = [
    ('happy', 0.2),
    ('sad', 0.2),
    ('angry', 0.1),
    ('relaxed', 0.1),
    ('anxious', 0.1),
    ('energetic', 0.2),
    ('romantic', 0.1),
]

def weighted_choice(choices):
    total = sum(w for _, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for item, weight in choices:
        if upto + weight >= r:
            return item
        upto += weight

def recommend_tracks(sp, emotion, num_tracks=3):
    genres = emotion_to_genre[emotion]
    recommendations = sp.recommendations(seed_genres=genres, limit=num_tracks)
    track_uris = [track['uri'] for track in recommendations['tracks']]
    return track_uris

app = Flask(__name__)

@app.route('/')
def index():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='YOUR_CLIENT_ID',
                                                   client_secret='YOUR_CLIENT_SECRET',
                                                   redirect_uri='YOUR_REDIRECT_URI',
                                                   scope='user-read-playback-state,user-modify-playback-state'))
    emotion = weighted_choice(emotion_weights)
    track_uris = recommend_tracks(sp, emotion)
    return render_template('index.html', track_uris=track_uris, emotion=emotion)

if __name__ == '__main__':
    app.run(debug=True)
