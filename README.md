🐶🐱 Dog vs Cat Image Classifier
📌 Project Overview

The Dog vs Cat Image Classifier is a Machine Learning project that classifies an uploaded image as either a Dog or a Cat. The application is built using Python and Streamlit, providing a simple and interactive web interface where users can upload an image and instantly receive the predicted class along with the confidence score.

The project demonstrates the complete machine learning workflow including image preprocessing, feature extraction, prediction, and deployment through an easy-to-use web application.
---
🚀 Features
Upload Dog or Cat images
Automatic image preprocessing
HOG (Histogram of Oriented Gradients) feature extraction
Predicts whether the image is a Dog or Cat
Displays confidence score
Interactive Streamlit interface
Lightweight and fast prediction
Easy to deploy locally or on cloud platforms
---
📂 Project Structure
Dog-Cat-Classifier/
│
├── app.py                 # Streamlit Web Application
├── model.py               # Prediction Model
├── uploads/               # Temporary uploaded images
├── requirements.txt       # Required Libraries
├── README.md              # Project Documentation
└── assets/                # Images (Optional)
---
🛠 Technologies Used
Technology	Purpose
Python	Programming Language
Streamlit	Web Application
NumPy	Numerical Computing
Pillow (PIL)	Image Processing
Scikit-Image	Image Resizing & HOG Features
Scikit-Learn	Machine Learning Utilities
Joblib	Model Loading
📊 Machine Learning Workflow
Input Image
      │
      ▼
Image Upload
      │
      ▼
Image Preprocessing
      │
      ▼
Resize Image (128×128)
      │
      ▼
Extract HOG Features
      │
      ▼
Load Trained Model
      │
      ▼
Prediction
      │
      ▼
Dog / Cat
      │
      ▼
Confidence Score
🧠 HOG Feature Extraction

The project uses Histogram of Oriented Gradients (HOG) for extracting important image features.

HOG captures

Edge information
Object shape
Texture patterns
Gradient orientation

These extracted features are then used by the classifier to distinguish between Dogs and Cats.

📸 Application Interface

The application allows users to

Upload JPG/JPEG/PNG images
View uploaded image
Predict image class
Display confidence percentage
Show prediction message based on confidence
⚙️ Installation

Clone the repository

git clone https://github.com/Hariom-patidar-tech/Dog-Cat-classifier.git

Go to project directory

cd Dog-Cat-classifier

Create virtual environment

python -m venv venv

Activate environment

Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate

Install dependencies

pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py

The application will open in your browser automatically.

📥 Supported Image Formats
JPG
JPEG
PNG
📈 Prediction Output

The application displays

Predicted Class
Confidence Score
Prediction Status

Example

Prediction : DOG

Confidence : 95.62%
📚 Libraries Used
streamlit
numpy
Pillow
scikit-image
scikit-learn
joblib
💡 Future Improvements
CNN-based Deep Learning Model
TensorFlow/Keras Integration
MobileNetV2
ResNet50
Batch Prediction
Webcam Detection
Real-time Video Classification
Grad-CAM Visualization
Multi-class Animal Classification
🎯 Learning Outcomes

This project demonstrates

Image Classification
Computer Vision Basics
Image Preprocessing
Feature Extraction
HOG Descriptor
Streamlit Deployment
Machine Learning Pipeline
📷 Sample Workflow
Upload Image
      ↓
Preprocess Image
      ↓
Extract HOG Features
      ↓
Model Prediction
      ↓
Dog / Cat
      ↓
Display Confidence
📌 Requirements
Python 3.9+

Streamlit

NumPy

Pillow

Scikit-image

Scikit-learn

Joblib
🤝 Contributing

Contributions are welcome!

If you'd like to improve this project, feel free to fork the repository and submit a pull request.

📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Hariom Patidar

🎓 B.Tech (CSIT)

💻 Machine Learning & Deep Learning Enthusiast

🌐 GitHub: Hariom-patidar-tech

⭐ If you found this project useful, don't forget to Star the repository!
