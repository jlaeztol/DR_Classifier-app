import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import cv2

def main():
    # set up the Streamlit app
    st.title("DRTect")
    st.title("Diabetic Retinopathy Severity Classification 📷")
    st.write("Using Pre-trained Convolutional Neural Network Model, this web-app enables to identify the Severity Level of Diabetic Retinopathy of Patient.")

    @st.cache_resource
    def load_model():
        model = tf.keras.models.load_model('final3_model_2.h5')
        return model

    def import_and_predict(image_data, model):
        size=(128,128)
        image = ImageOps.fit(image_data,size, Image.LANCZOS)
        image = np.asarray(image)
        image = image / 255.0
        img_reshape = np.reshape(image, (224, 224, 3))
        prediction = model.predict(img_reshape)
        return prediction

    model = load_model()
    class_names = ["No_DR", "Mild", "Moderate", "Severe", "Proliferate_DR"]


    file = st.file_uploader("Upload Retinal Image from your computer", type=["jpg", "png", "jpeg"])

    if file is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        prediction = import_and_predict(image, model)
        class_index = np.argmax(prediction)
        class_name = class_names[class_index]
        string = "Prediction: " + class_name
        st.success(string)

if __name__ == "__main__":
    main()
