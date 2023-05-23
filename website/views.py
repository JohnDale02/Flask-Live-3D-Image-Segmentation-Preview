from flask import Blueprint, render_template, request, flash
from flask_wtf import FlaskForm  # the actual uploading feature
from wtforms import FileField, SubmitField  # the buttons for uploading and submitting
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename
import os

global UPLOAD_FOLDER
UPLOAD_FOLDER = 'uploads'

views = Blueprint('views', __name__)

class UploadFileForm(FlaskForm):
    file = FileField("Image", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@views.route('/', methods=['GET', 'POST'])
@views.route('/index.html', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@views.route('/contacts.html')
def contacts():
    if request.method == 'POST':
        flash("Trying to get this post of contacts?")
    
    return render_template('contacts.html')

@views.route('/typography.html', methods=['POST', 'GET'])
def typo():
    form = UploadFileForm()
    if form.validate_on_submit():
        image = form.file.data
        image.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), UPLOAD_FOLDER ,secure_filename(image.filename)))
        #return render_template()
        # Start loading bar while waiting... --> run our c++ appication --> input that to OpenGL --> emscripten --> back to website
        # return the resource back --> (WebGl javascript)
    
    return render_template('typography.html', form=form)

@views.route('/about-us.html')
def about_us():
    if request.method == 'POST':
        flash("Trying to hear about us?")
    
    return render_template('about-us.html')
