import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.title("Детектор изоляторов ЛЭП")

model_type = st.selectbox("Выберите модель", ["YOLOv8", "YOLOv11"])
model_path = (
    "best_weight_yolo8n.pt"
    if model_type == "YOLOv8"
    else "best_weight_yolo11n.pt"
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
    results = model.predict(image)
    res_plotted = results[0].plot()
    st.image(
        res_plotted, caption="Результат распознавания", width=700
    )
