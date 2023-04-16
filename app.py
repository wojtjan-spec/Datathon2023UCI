from flask import Flask, request, render_template, jsonify, url_for, flash
import pickle
import os

app = Flask(__name__, static_url_path='/static')
app.config["IMAGE_UPLOAD"] = "/Users/janwojtkowski/Desktop/Datathon/static/images"
#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload-image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.files:
            image = request.files['image']
            image.save(os.path.join(app.config['IMAGE_UPLOAD'], image.filename))
            return render_template("index.html", uploaded_image=image.filename)
        return render_template("index.html")

# TODO
# this can be merged with the method below (route) 
# to perfrom file upload and predictions after one button press
@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["IMAGE_UPLOAD"], filename)

@app.route("/search")
def get_song():
    image = "/static/images/image.png"
    
    # TODO
    # load model

    # TODO
    # predict mood based on face expression

    #mood = model_images.predict([image])
    #output_mood = round(mood[0], 2)

    # TODO
    # predict song from mood valiance

    #song_valiance = model_songs.predict([output_mood])
    #output_song_valiance = round(song_valiance[0], 2)

    # TODO
    # return new index with Spotify API

if __name__ == "__main__":
    app.run()