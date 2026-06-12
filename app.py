import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
import numpy as np
from recommendation import cnv, dme, drusen, normal
import tempfile
from PIL import Image
import torch
import clip


@st.cache_resource
def load_clip_model():
    model, preprocess = clip.load("ViT-B/32", device="cpu")
    return model, preprocess


def is_valid_oct_scan(image_path: str) -> tuple[bool, str]:
    clip_model, preprocess = load_clip_model()

    image = preprocess(Image.open(image_path)).unsqueeze(0)
    texts = clip.tokenize([
        "an OCT retinal scan",
        "a photograph of a person",
        "a natural photograph",
        "a medical image that is not an eye scan"
    ])

    with torch.no_grad():
        logits_per_image, _ = clip_model(image, texts)
        probs = logits_per_image.softmax(dim=-1).squeeze().tolist()

    oct_prob = probs[0]

    if oct_prob < 0.5:
        return False, "This image does not appear to be an OCT retinal scan."

    return True, ""


def model_prediction(test_image_path):
    model = tf.keras.models.load_model("Trained_Model.h5", compile=False)
    img = tf.keras.utils.load_img(test_image_path, target_size=(224, 224))
    x = tf.keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    predictions = model.predict(x)
    confidence = float(np.max(predictions))
    return np.argmax(predictions), confidence


# UI
st.header("Welcome to the Human Eye Disease Prediction Platform")
test_image = st.file_uploader("Upload your retinal Optical Coherence Tomography (OCT) image:")

if test_image is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=test_image.name) as tmp_file:
        tmp_file.write(test_image.read())
        temp_file_path = tmp_file.name

if st.button("Predict") and test_image is not None:
    with st.spinner("Validating image..."):
        valid, reason = is_valid_oct_scan(temp_file_path)

    if not valid:
        st.error(
            f"⚠️ Invalid image: {reason}\n\n"
            "This platform only accepts **OCT (Optical Coherence Tomography) retinal scans**. "
            "Please upload a valid grayscale OCT image."
        )
    else:
        with st.spinner("Please Wait.."):
            result_index, confidence = model_prediction(temp_file_path)
            class_name = ['CNV', 'DME', 'DRUSEN', 'NORMAL']

        st.success(f"Model is Predicting it's a {class_name[result_index]} (Confidence: {confidence:.1%})")

        with st.expander("Learn More"):
            if result_index == 0:
                st.write("OCT scan showing *CNV with subretinal fluid.*")
                st.image(test_image)
                st.markdown(cnv)
            elif result_index == 1:
                st.write("OCT scan showing *DME with retinal thickening and intraretinal fluid.*")
                st.image(test_image)
                st.markdown(dme)
            elif result_index == 2:
                st.write("OCT scan showing *drusen deposits in early AMD.*")
                st.image(test_image)
                st.markdown(drusen)
            elif result_index == 3:
                st.write("OCT scan showing a *normal retina with preserved foveal contour.*")
                st.image(test_image)
                st.markdown(normal)