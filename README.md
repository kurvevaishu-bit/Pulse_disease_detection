# 🌱 AI Crop Disease Detection System

An AI-powered web application that detects crop leaf diseases from uploaded images and provides disease-specific prevention recommendations. The project uses TensorFlow, MobileNetV2 Transfer Learning, and Streamlit to help farmers and agricultural professionals identify plant diseases quickly and accurately.

## Features

* 📷 Upload a crop leaf image
* 🤖 AI-based disease prediction
* 📊 Confidence score for each prediction
* 🌿 Disease prevention recommendations
* ⚡ Fast and user-friendly Streamlit interface

## Technologies Used

* Python
* TensorFlow / Keras
* MobileNetV2
* NumPy
* Pillow
* Streamlit

## Dataset

The model was trained using the Black Gram Plant Leaf Disease (BPLD) dataset containing images of:

* Anthracnose
* Healthy
* Leaf Crinkle
* Powdery Mildew
* Yellow Mosaic

## Future Enhancements

* Support for multiple pulse crops such as Tur, Chickpea, Moong, and Urad.
* Multilingual recommendations (English, Hindi, Marathi).
* Fertilizer and treatment suggestions.
* Mobile application deployment.
* Integration with weather and disease forecasting systems.

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project Goal

To provide an accessible AI-based solution for early disease detection, helping farmers reduce crop losses and improve agricultural productivity.
