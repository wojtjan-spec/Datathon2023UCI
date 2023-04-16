from flask import Flask, request, render_template, jsonify, url_for, flash
import pickle
import os

app = Flask(__name__, static_url_path='/static')
app.config["IMAGE_UPLOAD"] = "/Users/janwojtkowski/Desktop/Datathon/imgs"
#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/predict',methods=['POST'])
# def predict():
#     #mood = int(request.form["1"])
#     #song = int(request.form["2"])
#     #prediction = model.predict([[1, 2]])
#     #output = round(prediction[0], 2) 
#     img = float(request.form["image"])

#     return render_template('index.html', prßediction_text=f'From placeholder mood -> song: placeholder')

@app.route('/upload-image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.files:
            image = request.files['image']
            image.save(os.path.join(app.config['IMAGE_UPLOAD'], image.filename))
            return render_template("index.html", uploaded_image=image.filename)
        return render_template("index.html")

@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["IMAGE_UPLOAD"], filename)






if __name__ == "__main__":
    app.run()
