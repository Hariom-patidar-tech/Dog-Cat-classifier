import streamlit as st
import os
from model import DogCatClassifier
from PIL import Image


st.set_page_config(
    page_title=" Dog vs Cat Classifier",
    page_icon="",
    layout="centered"
)


@st.cache_resource
def load_model():
    return DogCatClassifier()


UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def main():
    
    st.title(" Cat vs  Dog Classifier")
    st.write("Upload an image and I'll tell you if it's a cat or a dog!")
    
    
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        
        with st.spinner("Analyzing image..."):
            model = load_model()
            prediction, confidence = model.predict(file_path)
        
        st.header("Results")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Prediction", prediction.upper())
        
        with col2:
            st.metric("Confidence", f"{confidence*100:.2f}%")
        
        if confidence > 0.9:
            st.success(f"I'm very confident this is a {prediction}! 🎯")
        elif confidence > 0.7:
            st.info(f"I think this is a {prediction}, but I'm not entirely sure. 🤔")
        else:
            st.warning(f"This is a tricky one! I'm leaning towards {prediction}, but I'm quite uncertain. 😅")
        
        os.remove(file_path)

if __name__ == "__main__":
    main()