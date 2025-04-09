# 🌿 AGRODOCTOR - Plant Disease Detection using Deep Learning

AGRODOCTOR is a web-based application built with **Flask** and **TensorFlow** that helps users detect **15+ tomato-related plant diseases** by uploading an image of a leaf. This tool uses a trained Convolutional Neural Network (DenseNet) model and provides not only the prediction but also **descriptions and actionable recommendations**.

---

## 🚀 Live Demo

👉 [Click here to try it](https://plant-disease-prediction-using-deep.onrender.com)

---

## 📸 Features

- ✅ Upload a leaf image to detect plant diseases
- ✅ Supports 15+ tomato-related diseases
- ✅ Model powered by TensorFlow/Keras (`.h5` file)
- ✅ User Authentication (Register/Login)
- ✅ Smart result descriptions with care suggestions
- ✅ Mobile-responsive & professional UI
- ✅ SQLite database for storing user accounts
- ✅ Deployed on [Render]((https://plant-disease-prediction-using-deep.onrender.com))

---

## 🧠 Technologies Used

- **Python 3.10**
- **Flask (Backend)**
- **TensorFlow / Keras (Model)**
- **SQLite (Database)**
- **Bootstrap 5 (Frontend styling)**
- **Jinja2 (Templating engine)**

---

## 📁 Folder Structure

agrodoctor/ 
│ ├── app.py # Flask app entry point 
  ├── PlantDNet.h5 # Trained CNN model 
  ├── disease_info.py # Dictionary with disease descriptions 
  ├── templates/ # HTML files (login, result, register, etc.) 
  ├── static/ # CSS, JS, Images 
  ├── uploads/ # Uploaded images 
  ├── site.db # SQLite database 
  ├── requirements.txt # Python dependencies 
  ├── render.yaml # Render deployment config └──


---

## ⚙️ How to Run Locally

1. **Clone the repo:**
2. git clone ((https://github.com/akashjape/Plant-Disease-Prediction-Using-Deep-Learning/))
3 .cd agrodoctor
4. pip install -r requirements.txt
5. python app.py

👨‍🌾 Use Cases :

Agricultural labs
Farmers & agronomists
Smart farming startups
AI + Agri education demos

🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first.
