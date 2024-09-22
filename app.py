from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Path to the folder where music files are stored, with subfolders for each person
app.config['MUSIC_FOLDER'] = 'static/music/'

@app.route('/')
def index():
    # List all directories (representing users) in the music folder
    users = [d for d in os.listdir(app.config['MUSIC_FOLDER']) if os.path.isdir(os.path.join(app.config['MUSIC_FOLDER'], d))]
    return render_template('index.html', users=users)

@app.route('/user/<username>')
def user_music(username):
    # List all music files in the user's folder
    user_folder = os.path.join(app.config['MUSIC_FOLDER'], username)
    if os.path.exists(user_folder):
        songs = [song for song in os.listdir(user_folder) if song.endswith(('.mp3', '.wav'))]
        return render_template('user_music.html', username=username, songs=songs)
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
