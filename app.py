import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model(
    "bpld_model.keras",
    compile=False
)

classes = [
    "Anthracnose",
    "Healthy",
    "Leaf Crinkle",
    "Powdery Mildew",
    "Yellow Mosaic"
]

recommendations = {
    "Anthracnose":"Remove infected leaves and use fungicide.",
    "Healthy":"Plant is healthy.",
    "Leaf Crinkle":"Remove infected plants and control insect vectors.",
    "Powdery Mildew":"Apply sulfur fungicide.",
    "Yellow Mosaic":"Control whiteflies and remove infected plants."
}

def preprocess_image(img):
    img = img.resize((224,224))
    img = np.array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

st.title("🌱 Pulse Crop Disease Detection System")

st.markdown(
    "AI-powered crop disease detection system for early identification and management of plant diseases."
    
)
uploaded_file = st.file_uploader(
    "Upload Leaf Image",
    type=["jpg","jpeg","png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image)

    processed = preprocess_image(image)

    prediction = model.predict(processed)

    predicted_class = np.argmax(prediction)

    confidence = np.max(prediction) * 100

    disease = classes[predicted_class]

    st.success(f"Disease: {disease}")

    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    st.info(recommendations[disease])