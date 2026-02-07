import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os
import queue
import threading
import time
from pathlib import Path

st.set_page_config(page_title="Detected LEP", layout="wide")
st.title("Детектор объектов ЛЭП ⚡")


@st.cache_resource
def get_resources():
    base_dir = Path(__file__).resolve().parent.parent
    models = {
        "YOLOv8n": YOLO(
            os.path.join(base_dir, "ml_models", "best_weight_yolo8n.pt")
        ),
        "YOLOv11n": YOLO(
            os.path.join(base_dir, "ml_models", "best_weight_yolo11n.pt")
        ),
    }
    q = queue.Queue()
    return models, q, base_dir


models_dict, task_queue, base_dir = get_resources()


@st.cache_resource
def start_global_worker():
    def worker_logic():
        while True:
            task = task_queue.get()
            model_key, img, conf, result_container = task

            try:
                model = models_dict[model_key]
                results = model.predict(img, conf=conf)

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
col1, col2 = st.columns([2, 1])
with col1:
    model_type = st.selectbox(
        "Выберите архитектуру нейросети",
        ["YOLOv8n", "YOLOv11n"],
        help="YOLOv8n лучше находит гнезда на траверсах и кучи веток, "
        "но во всём остальном рекомендуем использовать YOLOv11n, "
        "чаще всего он дает результат чуть по лучше",
    )
    conf = st.slider(
        "Выберите confidence нейросети",
        min_value=0.0,
        max_value=1.0,
        value=0.25,
        step=0.1,
        help="Чем выше порог, тем меньше 'ложных' срабатываний," \
        " но модель может пропустить реальные объекты.",
    )
    uploaded_file = st.file_uploader(
        "Загрузите фото", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Ваше фото", width=300)

        if st.button("Начать анализ"):
            res_box = {"ready": False, "image": None, "error": None}

            task_queue.put((model_type, image, conf, res_box))

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
with col2:
    st.subheader("Категории объектов которые модели умеют распознавать")
    path_img_category = os.path.join(
        base_dir, "streamlit_demo", "assets", "category.png"
    )
    if os.path.exists(path_img_category):
        st.image(path_img_category, width='content')
    else:
        st.warning("Файл с таблицей не найден")
