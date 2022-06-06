import streamlit as st 
import numpy as np  
from keras.layers import *
from keras.models import *
from keras.preprocessing import image
from PIL import Image
import base64
#stremalit title
st.title("Covid-19 cheast X_Ray image Classification 🤢")
#streamlit uploader function
uploaded_files = st.file_uploader(label="Choose a X_Ray", type=["png","jpg"])
predict = "❌Plase Enter the X_Ray image first❌❌❌"
#Load the model i save  and images to classify 
model = load_model("CNN_model.h5")

if uploaded_files is not None:
    show_image = Image.open(uploaded_files)
    st.image(show_image)
    image_data = uploaded_files.read()
    test_image = show_image.resize((224,224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image,axis = 0)
    result = model.predict(test_image)
    if result [0][0] == 1:
        predict = 'Normal'
        new_prediction = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Normal</p>'
    else:
        predict = 'Covid'
        new_prediction1 = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">Covid-19</p>'
        
else:
    st.write("Please Enter the image🖼️")
# Streamlite button for Classification
if st.button("Test The X_Ray"):
    if predict == "Normal":
        st.write(predict)
        st.markdown(new_prediction, unsafe_allow_html=True)
        image = Image.open('no covid.jpg')
        st.image(image)
        nor = '<p style="font-family:sans-serif; color:black; font-size: 42px;">This X_Ray image is Normal</p>'
        st.markdown(nor,unsafe_allow_html=True)
        st.title("This x_ray image is normal")
    else:
        st.write(predict)
        st.markdown(new_prediction1, unsafe_allow_html=True)
        image = Image.open('covid-19.png')
        st.image(image)
        cov = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">In this X_Ray image found a covid-19</p>'
        st.markdown(cov,unsafe_allow_html=True)
        
#This is extra feature to resize the streamlit button and all
k = st.markdown("""
<style>
div.stButton > button:first-child {
padding: 15px 300px;
}
</style>""", unsafe_allow_html=True)
############################################
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
.stApp {
  background-image: url("data:image/png;base64,%s");
  background-size: cover;
}
</style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('Covid.jpg')
#########################################
