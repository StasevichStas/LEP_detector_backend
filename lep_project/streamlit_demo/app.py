import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os
from pathlib import Path

st.title("Детектор изоляторов ЛЭП")
base_dir = Path(__file__).resolve().parent.parent
model_type = st.selectbox("Выберите модель", ["YOLOv8", "YOLOv11"])
model_path = (
    os.path.join(base_dir, "ml_models", "best_weight_yolo8n.pt")
    if model_type == "YOLOv8"
    else os.path.join(base_dir, "ml_models", "best_weight_yolo11n.pt")
)


@st.cache_resource
def load_model(path):
    return YOLO(path)


model = load_model(model_path)

uploaded_file = st.file_uploader(
    "Загрузите фото ЛЭП в формате jpg, jpeg, png", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    results = model.predict(image, conf=0.25)
    res_plotted = results[0].plot()
    st.image(res_plotted, caption="Результат распознавания", width=700)
