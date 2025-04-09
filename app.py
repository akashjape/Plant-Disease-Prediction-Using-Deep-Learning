import os
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, flash, redirect, url_for, session, request
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from disease_info import disease_info  # ✅ Your separate dictionary file

# Initialize Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ✅ User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# ✅ Login Required Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("You must be logged in to access this page.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ✅ Login Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))  # Already logged in

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your email and password.', 'danger')
    return render_template('login.html')

# ✅ Registration Route
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Passwords do not match.', 'danger')

    return render_template('register.html')

# ✅ Logout Route
@app.route('/logout/')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# ✅ About Page (optional login required)
@app.route('/about', methods=['GET'])
@login_required
def about():
    return render_template('index.html')

# ✅ Main Page (Protected)
@app.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('index.html')

# ✅ Load Model
model = tf.keras.models.load_model('PlantDNet.h5', compile=False)

# ✅ Prediction Logic
def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(64, 64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x.astype('float32') / 255.0
    preds = model.predict(x)
    return preds

# ✅ Prediction Route (Protected)
@app.route('/predict', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        f = request.files['file']
        
        # Save the file
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'uploads')
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        file_path = os.path.join(upload_path, secure_filename(f.filename))
        f.save(file_path)

        # Predict
        preds = model_predict(file_path, model)
        disease_class = [
            'Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'Potato___Early_blight',
            'Potato___Late_blight', 'Potato___healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight',
            'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
            'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot',
            'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy', 'weed'
        ]
        predicted_label = disease_class[np.argmax(preds)]

        # Get disease info
        info = disease_info.get(predicted_label, {
            "name": predicted_label,
            "description": "No information available for this disease.",
            "recommendations": []
        })

        return render_template('result.html', img_path=f.filename, prediction=predicted_label, info=info)

    return render_template('upload.html')

# ✅ Run App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
