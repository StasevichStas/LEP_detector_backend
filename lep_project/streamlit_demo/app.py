import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os
import queue
import threading
import time
from pathlib import Path

st.title("Детектор объектов ЛЭП ⚡")


@st.cache_resource
def get_resources():
    base_dir = Path(__file__).resolve().parent.parent
    models = {
        "YOLOv8": YOLO(
            os.path.join(base_dir, "ml_models", "best_weight_yolo8n.pt")
        ),
        "YOLOv11": YOLO(
            os.path.join(base_dir, "ml_models", "best_weight_yolo11n.pt")
        ),
    }
    q = queue.Queue()
    return models, q


models_dict, task_queue = get_resources()


@st.cache_resource
def start_global_worker():
    def worker_logic():
        while True:
            task = task_queue.get()
            model_key, img, result_container = task

            try:
                model = models_dict[model_key]
                results = model.predict(img, conf=0.5)

                result_container["image"] = results[0].plot()
                result_container["ready"] = True
            except Exception as e:
                result_container["error"] = str(e)
                result_container["ready"] = True

            task_queue.task_done()

    t = threading.Thread(target=worker_logic, daemon=True)
    t.start()
    return t


start_global_worker()

model_type = st.selectbox(
    "Выберите архитектуру нейросети", ["YOLOv8", "YOLOv11"]
)
uploaded_file = st.file_uploader("Загрузите фото", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Ваше фото", width=300)

    if st.button("Начать анализ"):
        res_box = {"ready": False, "image": None, "error": None}

        task_queue.put((model_type, image, res_box))

        with st.spinner(
            f"В очереди... Задач перед вами: {task_queue.qsize() - 1}"
        ):
            while not res_box["ready"]:
                time.sleep(0.1)

        if res_box["error"]:
            st.error(f"Ошибка при обработке: {res_box['error']}")
        else:
            st.image(
                res_box["image"],
                caption=f"Результат ({model_type})",
                width=700,
            )
            st.success("Готово!")
