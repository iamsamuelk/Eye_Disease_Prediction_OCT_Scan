import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
import numpy as np
from recommendation import cnv,dme,drusen,normal
import tempfile


#Tensorflow Model Prediction
def model_prediction(test_image_path):
    model = tf.keras.models.load_model("Trained_Model.h5", compile=False)
    img = tf.keras.utils.load_img(test_image_path, target_size=(224, 224))
    x = tf.keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    predictions = model.predict(x)
    return np.argmax(predictions)  # return index of max element


#Prediction Page
st.header("Welcome to the Human Eye Disease Prediction Platform")
test_image = st.file_uploader("Upload your retinal Optical Coherence Tomography (OCT) image:")
if test_image is not None:
    # Save to a temporary file and get its path
    with tempfile.NamedTemporaryFile(delete=False, suffix=test_image.name) as tmp_file:
        tmp_file.write(test_image.read())
        temp_file_path = tmp_file.name
#Predict button
if(st.button("Predict")) and test_image is not None:
    with st.spinner("Please Wait.."):
        result_index = model_prediction(temp_file_path)
        #Reading Labels
        class_name = ['CNV', 'DME', 'DRUSEN', 'NORMAL']
    st.success("Model is Predicting it's a {}".format(class_name[result_index]))

    # Recommendation
    with st.expander("Learn More"):
        #CNV
        if(result_index==0):
            st.write('''
                OCT scan showing *CNV with subretinal fluid.*
            ''')
            st.image(test_image)
            st.markdown(cnv)
    
        #DME
        elif(result_index==1):
            st.write('''
                OCT scan showing *DME with retinal thickening and intraretinal fluid.*
            ''')
            st.image(test_image)
            st.markdown(dme)

        #DRUSEN
        elif(result_index==2):
            st.write('''
                OCT scan showing *drusen deposits in early AMD.*
            ''')
            st.image(test_image)
            st.markdown(drusen)
            
        #NORMAL
        elif(result_index==3):
            st.write('''
                OCT scan showing a *normal retina with preserved foveal contour.*
            ''')
            st.image(test_image)
            st.markdown(normal)