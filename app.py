from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from HackneClient import HackneClient

from datetime import datetime
import os

MODEL_PATH        = "best.onnx"
IMAGE_UPLOAD_PATH = "static/img"
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'JPG'}

app                         = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_UPLOAD_PATH
app.secret_key              = '123456'


client = HackneClient(MODEL_PATH)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # File Upload
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f"image.jpg"))

            return redirect("http://127.0.0.1:5000/analysis")

@app.route('/analysis')
def analysis():
    analysis_results = client.predict(f"{IMAGE_UPLOAD_PATH}/image.jpg")
    analysis_results.save(filename="static/img/result.jpg")
    severity         = len(analysis_results.boxes)

    skintype = 'dry'

    suggestion = client.get_reccomendation(severity, skintype)
    
    data = {
        'message': f"Facial Analysis of {severity} severity",
        'cleanser': suggestion[0],
        'moisturizer': suggestion[1],
        'sunscreen': suggestion[2],
    }

    return render_template('analysis.html', data=data)

    
    
if __name__ == '__main__':
    app.run(debug = True)